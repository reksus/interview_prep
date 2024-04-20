class Message:
  """Simple message class to hold data"""
  def __init__(self, sender, content):
    self.sender = sender
    self.content = content

class Hub:
  """Central Hub that receives messages from spokes and routes them"""
  def __init__(self):
    self.spokes = []

  def register_spoke(self, spoke):
    """Register a spoke with the Hub"""
    self.spokes.append(spoke)
    spoke.set_hub(self)

  def distribute_message(self, message):
    """Distribute a message from a spoke to all other spokes"""
    for spoke in self.spokes:
      if spoke != message.sender:
        spoke.receive_message(message)

class Spoke:
  """Spoke that sends and receives messages to/from the Hub"""
  def __init__(self, name):
    self.name = name
    self.hub = None

  def set_hub(self, hub):
    """Set the Hub for this spoke"""
    self.hub = hub

  def send_message(self, content):
    """Send a message to the Hub"""
    message = Message(self.name, content)
    self.hub.distribute_message(message)

  def receive_message(self, message):
    """Receive a message from the Hub and print it"""
    print(f"Spoke {self.name} received message from {message.sender}: {message.content}")

# Create a Hub and Spokes
hub = Hub()
spoke1 = Spoke("Spoke 1")
spoke2 = Spoke("Spoke 2")

# Register Spokes with the Hub
hub.register_spoke(spoke1)
hub.register_spoke(spoke2)

# Send messages from Spokes
spoke1.send_message("This is a message from Spoke 1")
spoke2.send_message("This is a message from Spoke 2")
