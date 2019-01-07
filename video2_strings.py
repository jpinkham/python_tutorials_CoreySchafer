#!/usr/bin/env python

# Video located at https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=3&t=0s

import sys


message = "Hello world"
greeting = "Hello"
person_name = "you"


# #slices
# print(">", message[0:5], "<") #starting from index 0, stop at index 5
# print(message[5:])  #when end of slice isn't mentioned, it's assumed you mean end of string
# print(">", message[:6], "<")	#when start of slice isn't mentioned, it's assumed you mean start of string

# # count the number of specified string/char in the string object (or array/tuple?)
# print("there are >",message.count('l'), "< instances of the letter 'l'")

# # find index of where specified text is found in the string
# print(message.find("orl"))

# string replace in-line
#message = message.replace('world', 'universe')
# print(message)

# meh idea
#message = greeting + ', ' + person_name

# auto adds spaces between vars if you use "," instead of "+"

# using placeholders that will be interpolated, with string formatting
#message = '{}, {}. Welcome!'.format(greeting, person_name)

# !python 3.6+ ONLY!
#"f strings"  simple and straightforward formatting AND you can write code within placeholders!
#message = f'{greeting}, {person_name.upper()}. Welcome!'

# show all attribs and methods available for the specified var
# print(dir(message))

# show all attribs and methods (WITH USAGE INFO!) available for the specified DATA TYPE
print(help(str))
