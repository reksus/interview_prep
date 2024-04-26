"""
find substring ---------------------------------
"""

a = "Exercise"
print(a.find("E"))  # 0
print(a.find("e"))  # 2
print(a.find("y"))  # -1
print(a.find("xe", 1))  # 1 (finding in a[1:])
print(a[1:2])  # x
print(a.find("xe", 1, 2))  # -1 (finding in a[1:2])


# both 'find' and 'index' gives the 1st occurence of substring
# but if not found 'find' return -1, while index throws ValueError
s = 'Car, Bike, Bus, Cycle'
x = s.find('Plane')
print(x)  # -1

print(s.index('Bike', 0))
try:
    x = s.index('Plane')
    print(x)  # 
except ValueError as e:
    print(f"{repr(e)}")


"""
subsequence -------------------------------
"""

s = "Captain America"
print(s[1:5:2])  # at

a = "Welcome to complete Python Course"
print(a.count("c"))  # 2
print(a.count("o"))  # 5
print(a.count("Python"))  # 1


"""
Checking char types ------------------------
"""
# casing

a = "hi Homies,good morning"
print(a.istitle()) # False
print(a.islower()) # False
print(a.isupper()) # False

# space

a = "\n\rab"
print(a.isspace())  # False
a = "\n\r"
print(a.isspace())  # True

# char class

c = "456"
d = "$*%!!**"
print(c.isalnum())  # True
print(d.isalnum())  # False

c = "456"
d = "Python"
print(c.isalpha())  # False
print(d.isalpha())  # True

c = u"\u00B10"
x = "10"
print(c.isdecimal())  # False
print(x.isdecimal())  # True

c = "4567"
d = "1.65"
# isdigit(): [0, 9]
# isnumeric(): if a string contains any numeric characters, including digits, fractions, and superscripts
print(c, d)
print(c.isdigit())  # True
print(d.isdigit())  # False
print(c.isnumeric())  # True
print(d.isnumeric())  # False
print('½⅓¼⅕⅙⅐⅛⅑⅒⅔¾⅖⅗⅘⅚⅜⅝⅞⅟↉'.isnumeric())  # True
print('一二三四五'.isdigit())  # False
print('一二三四五'.isnumeric())  # True

# other
b = "for"
print(a.isidentifier())  # True

"""
Manipulation -------------------------------
"""

# reverse a string
s = "Captain America"
print(s[::-1])  # aciremA niatpaC

# 1. Casing

a = "hi Homies,good morning"
print(a.swapcase())  # hI hOMIES
print(a.title())  # Hi Homies,Good Morning

print(a.lower())  # hi homies,good morning

print(a.upper())  # HI HOMIES,GOOD MORNING

print(a.capitalize())  # Hi homies,good morning

print(a.casefold())  # hi homies,good morning  
# similar to .lower(), but should be used for caseless comparison
# but display purpose use .lower()

# 2. Replace chars according to mapping table
txt = "Hello Sam!"
mytable = str.maketrans("SoO", "PyX")
print(mytable)  # {83: 80, 111: 121, 79: 88}
print(txt.translate(mytable))  # Helly Pam!

# 2. Splitting into list

a = "Welcome,,Friends,"
print(a.split(","))  # ['Welcome', '', 'Friends', '']

a = "Complete.Python-course-is-good"
print(a.partition("-"))  # ('Complete', '.', 'Python-course-is-good')  (return a 3-tuple)

a = "a\nb"
print(a.splitlines())  # ['a', 'b']
a = "a\rb"
print(a.splitlines())  # ['a', 'b']

# operation of starting and ending

print(a.startswith("A"))  # False
print(a.startswith("a"))  # True

a = "Watermelon"
print(a.endswith("s"))  # False
print(a.endswith("melon"))  # True

s = "***Python***"
print(s.strip('*'))
print(s)  # Python

print('MiscTests'.removesuffix('Tests'))  # 'Misc'
print('MiscTests'.removeprefix('Misc'))  # 'Tests'

"42".zfill(5)  # 00042
"-42".zfill(5)  # -0042

a = "Python" 
b = a.center(9, "*")  # Pads string with specified character
print(b)  # **Python*


"""
transmission
"""
a = "string"
b = a.encode()
print(b)  # b'string'
c = b.decode()
print(c)  # string
