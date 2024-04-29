# models.py
from django.db import models
from django.db.models import Q

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)  # Hashed password

    def has_latest_consent_granted(self):
        """
        Checks if the user's latest consent log entry is GRANTED.
        """
        try:
            latest_consent = self.consentlog_set.latest('timestamp')
            return latest_consent.consent_type == 'GRANTED'
        except ConsentLog.DoesNotExist:
            return False

    def has_latest_consent_granted_and_older_than_six_months(self):
        """
        Checks if the user's latest consent is GRANTED and older than 6 months.
        """
        try:
            latest_consent = self.consentlog_set.latest('timestamp')
            return latest_consent.consent_type == 'GRANTED' and latest_consent.timestamp < timezone.now() - timezone.timedelta(days=365 // 2)
        except ConsentLog.DoesNotExist:
            return False


class CreditReport(models.Model):
    credit_report_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data = models.BinaryField()
    download_timestamp = models.DateTimeField()

class ConsentLog(models.Model):
    consent_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consent_type = models.CharField(max_length=7, choices=[('GRANTED', 'GRANTED'), ('REVOKED', 'REVOKED')])
    timestamp = models.DateTimeField()


# download_credit_report.py
def download_report(user_id):
    # Simulate downloading report data
    return b"Sample Credit Report Data"

# views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, CreditReport, ConsentLog
from .serializers import UserSerializer, CreditReportSerializer, ConsentLogSerializer
from .download_credit_report import download_report  # Replace with your download logic


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Require authentication for all actions

    def update(self, request, pk, partial=False):
        user = self.get_object(pk)
        serializer = self.get_serializer(user, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def grant_consent(self, request, pk):
        user = self.get_object(pk)
        self.handle_consent_change(user, 'GRANTED')
        return Response({'message': 'Consent granted successfully'})

    @action(detail=True, methods=['post'])
    def revoke_consent(self, request, pk):
        user = self.get_object(pk)
        self.handle_consent_change(user, 'REVOKED')
        return Response({'message': 'Consent revoked successfully'})

    def handle_consent_change(self, user, consent_type):
        if consent_type == 'GRANTED':
            # Download credit report
            report_data = download_report(user.user_id)
            if report_data:
                # Save credit report and consent log
                credit_report, created = CreditReport.objects.get_or_create(user=user)
                credit_report.data = report_data
                credit_report.save()
                ConsentLog.objects.create(user=user, consent_type=consent_type)
            else:
                # Handle download error
                return Response({'error': 'Failed to download credit report'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        elif consent_type == 'REVOKED':
            # Delete credit report and create consent log
            CreditReport.objects.filter(user=user).delete()
            ConsentLog.objects.create(user=user, consent_type=consent_type)
        else:
            # Handle invalid consent type
            return Response({'error': 'Invalid consent type'}, status=status.HTTP_400_BAD_REQUEST)

        return



# management/commands/remove_stale_reports.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from logging import getLogger
from .models import User, CreditReport, ConsentLog

logger = getLogger(__name__)

class Command(BaseCommand):
    help = 'Deletes credit reports for users with consent older than 6 months'

    def handle(self, **options):
        # Filter users with outdated consent using model manager method
        users_to_check = User.objects.filter(has_latest_consent_granted_and_older_than_six_months=True)

        num_users_checked = users_to_check.count()
        num_reports_deleted = 0

        for user in users_to_check:
            # Delete credit report for this user (handle case where no report exists)
            num_deleted = CreditReport.objects.filter(user=user).delete()
            if num_deleted:
                num_reports_deleted += num_deleted
                logger.info(f"Deleted credit report for user {user.username}")
            else:
                logger.info(f"No credit report found for user {user.username}. Skipping deletion.")

        logger.info(f"Checked {num_users_checked} users. Deleted {num_reports_deleted} outdated credit reports.")

        self.stdout.write(self.style.SUCCESS('Successfully processed outdated credit reports.'))
