#!/usr/bin/env python
import sys

# let's be certain which version/executable of python we are running the script under
print("Python interpreter: ", sys.executable, "\n")
# print(sys.version)

# Following along with https://www.youtube.com/watch?v=9Os0o3wzS_I&index=7&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
# Topic: Functions


# def hello_function():
#	pass		# I assume this is useful for doing function skeletons; does nothing and exits function


# Test function that performs an action
# def hello_function():
#    print('Hello world')


# hello_function()

# Test function that returns a value
# def hello_function():
#    return 'Hello world!'


# print(hello_function())
# print(hello_function().upper())
# because a string object is returned, you can call the string method upper()


# function that return values AND require callers to supply input params
# def hello_function(greeting):
#    return '{}'.format(greeting)  # guess: this is how you do a recursive call
# my guess was wrong, I was thrown by tutorial including the word 'Function' in the return line, but that's just how he did his example
# there's nothing recursive about this, it's simply returning [what I now understand to be] a string with substituted vars

# print(hello_function())
# because we just defined the function as requiring an input param, this exits script with 'TypeError' "missing 1 required positional argument: 'greeting' "

# print(hello_function('Hola!'))  # correct way to call


# by providing a default value for the input parameter, it is no longer required to be supplied by the caller
# def hello_function(greeting = "Hello"):
#    return '{}'.format(greeting)

# print(hello_function())

# def hello_function(greeting, name):
#    return '{}'.format(greeting)

# print(hello_function())
# supply nothing when calling the function and TypeError is returned
# TypeError: hello_function() missing 2 required positional arguments: 'greeting' and 'name'

# print(hello_function('Whazzup','JP'))	#correct way to call

# one required input param and one optional input param, with default value
# return value now includes two placeholders and two vars supplied to format()
# def hello_function(greeting, name='you'):
#   return '{} {}'.format(greeting, name)


# print(hello_function('Whazzup'))  # this usage is fine since 'name' has a default value
# print(hello_function('Whazzup','JP'))

# add slightly more formatting to output
# def hello_function(greeting, name):
#    return '{} there, {}'.format(greeting, name)  # perl: $greeting . ' there, ' . $name

#print(hello_function('Aloha', 'lady'))


# def flexible_function(*args, **kwargs):
# *args == unknown/variable number of positional arguments; uses any data type supplied or tuple by default?
# **kwargs == unknown/variable number of keyword arguments; store in dictionary by default (always)?
# these are conventions for naming, but not required
#    print('args: ', args)
#    print('kwargs: ', kwargs)


#print(flexible_function('blargh', 'yadda'))
#print(flexible_function('Tall', haircolor='blonde', age=42))

# ?output includes 'None', after printing args and kwargs, where is it coming from?


person_characteristics = ['Loud', 'Kind', 'Introverted']
person_attributes = {'age': 42, 'name': 'Jane Doe', 'height': "5'"}


def flexible_function_autounpack(*characteristics, **attributes):
    # by prefixing input params with '*' or '**', python will unpack objects into their individual elements
    print('Characteristics: ', characteristics)
    print('Attributes: ', attributes)

#print(flexible_function_autounpack(person_characteristics, person_attributes))
# Nope.  Output:
#  Characteristics:  (['Loud', 'Kind', 'Introverted'], {'age': 42, 'name': 'Jane Doe', 'height': "5'"})
#  Attributes:  {}
#  None  ? where is this coming from?!?


print(flexible_function_autounpack(*person_characteristics, **person_attributes))
# aha!  The passed params must be prefixed with '*' or '**' as well, not just in the function definition
# in order to be unpacked into individual elements/members
print('\n\n')


def function_with_docstring(string_to_print):
    """Prints the supplied string"""
    # is there an equivalent to 'perldoc' that extracts this data dynamically at the command line?
    print(string_to_print)


function_with_docstring("I'm just a bill, yes I'm only a bill, and I'm sittin here on Capitol Hill")
