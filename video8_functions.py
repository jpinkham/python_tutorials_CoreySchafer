#!/usr/bin/env python
import sys

# let's be certain which version/executable of python we are running the script under
print("Python interpreter: ", sys.executable, "\n")
# print(sys.version)

# Following along with https://www.youtube.com/watch?v=9Os0o3wzS_I
# Topic: Functions


# def hello_function():
#	pass		#useful for laying out functions; does nothing and exits function
# print('Hello world')
#   return 'Hello World'

# hello_function()


# DRY == Don't Repeat Yourself == USE FUNCTIONS


# test functions that return values AND require callers to supply input params
def hello_function(greeting):
    return '{} Function.'.format(greeting)  # guess: this is how you do a recursive call (blargh, hate that)


#print(hello_function())  #this exits script with 'TypeError' "missing 1 required positional argument: 'greeting' "


#def goodbye_function():   #original test with no required params
def goodbye_function(greeting):
  #  result = hello_function('Goodbye forever')
    # print(result)
#    print(result.upper())  # string is returned, so you can call string function upper()
    # wait, what?  this prints "GOODBYE FOREVER FUNCTION."
    return '{}'.format(greeting)  # guess: this is how you do a recursive call (blargh, hate that)


print(goodbye_function('Sayonara!'))
