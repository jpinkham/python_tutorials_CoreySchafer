#!/usr/bin/env python
import sys

# let's be certain which version/executable of python we are running the script under
print("Python interpreter: ", sys.executable, "\n")
# print(sys.version)

# Following along with https://www.youtube.com/watch?v=DZwmZ8Usvnk
# Topic: Conditionals and Booleans

# if False:
#    print('Conditional was True')

language = 'Javascript'

if language == 'Python':
    print("Lang is python")
elif language == 'Java':
    print("Lang is Java")
else:
    print("Lang is unknown")


# any switch/case?   Nope just keep adding 'elif'


# Booleans:  and, or, not, is

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('bad creds')

if not logged_in:
    print('Please log in')
else:
    print('Welcome user')


# Test if two objects are exactly the same, in memory(not just containing same data)

a = [1, 2, 3]
b = [1, 2, 3]

print("a == b:", a == b)  # true because contents of each are equivalent
print("a is b:", a is b)  # false because they aren't pointing to exact same object instance
print("a ID:", id(a), "b ID:", id(b))

# set b as pointer to a
b = a
print("a is b:", a is b)  # true because they ARE pointing to exact same object instance
print("a ID:", id(a), "b ID:", id(b))  # IDs are now exactly the same


# Values that
# Evaluates to False:
#    False
#    None
#    Zero, of any numeric type
#    Any empty sequence ( '', [], () )
#    Any empty mapping ( {} )

#condition = {}
#condition = ''
condition = 2


if condition:
    print(condition, "evaluates to True")
else:
    print(condition, "evaluates to False")
