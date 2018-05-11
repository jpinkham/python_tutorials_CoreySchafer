#!/usr/bin/env python
import sys

# let's be certain which version/executable of python we are running the script under
print("Python interpreter: ", sys.executable, "\n")
# print(sys.version)

# Following along with https://www.youtube.com/watch?v=daefaLgNkw0&index=4&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

# Dictionaries - key/value pairs (equiv to perl hash or JS assoc array)

# Example dict
student = {'name': 'john', 'age': 25, 'courses': ['Math', 'Philosophy']}
print("Direct key access: ", student['name'])

# preferred because returns 'None' if key not found:
print("Using get() method: ", student.get('name'))

# even better to specify a custom error when the key is not found
print("Using get() on non-existent key plus custom error text: ", student.get('nombre', 'Where did you go?'))


# Add a key
student["phone"] = "555-1212"
print("Using get() method: ", student.get('phone'))

# Modify an existing key
student["phone"] = "936-1212"
print("Using get() method: ", student.get('phone'))


# bulk update!  update() func. Input is a dictionary
student.update({'phone': '867-530nyeeeeyine', 'name': 'Jenny jenny', 'social': '123-45-9876'})
print("contents of 'student' dictionary object, after adding new key: ", student)

# delete keys
del student["social"]
print("contents of 'student' dictionary object, after deleting a key: ", student)

# let's see what happens when i try to delete a key that doesn't exist
###del student["nope"]
# it bails, after returns a somewhat vague (to me anyway, going on name alone): KeyError: 'nope'
# if KeyError can only ever mean that key doesn't exist, then it's not vague

# delete a dict item/key py popping from dict and return it / optionally store it elsewhere
student_name = student.pop('name')
print("Student name:", student_name)
print("contents of 'student' dictionary object, after deleting a key via pop(): ", student)


# number of keys in the dict
print("Num keys in student dict: ", len(student))

# list of keys...same as perl cmd - returns 'dict_keys' object
print("List of keys in student dict: ", student.keys(), "\n")

# list of values (but no keys to help give you any context) - returns 'dict_values' object
print("List of only values in student dict: ", student.values(), "\n")

# list of key/value pairs - returns 'dict_items' object
print("All items in student dict: ", student.items(), "\n")


# cycle through list using for
for stu_key, stu_value in student.items():
    print(stu_key, ":", stu_value)
