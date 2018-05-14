#!/usr/bin/env python
import sys
# add my custom lib dir to python path so importing my libs will work
# sys.path.append('/Users/jpinkham/dev/python_tutorials_CoreySchafer/mymodules')
# better not to hardcode here and instead add this to PYTHONPATH env var in ~/.bash_profile

# Following along with https://www.youtube.com/watch?v=CqvZ3vGoGs0
# Topic: Importing modules and exporing the std lib

#import jp_module
# import jp_module as jpm  #custom name, usually done to shorten original name
# from jp_module import find_index  #import function from custom mod into local namespace
from jp_module import find_index, test  # import module function and variable
# from jp_module import *  #DONT DO THIS because now you have no idea what is imported

looney_list = ['Taz', 'Bugs Bunny', 'Yosemite Sam', 'Pepe Le Pew']

#index = jp_module.find_index(looney_list, 'Bugs Bunny')
# index = jpm.find_index(looney_list, 'Bugs Bunny')   #use short custom name
index = find_index(looney_list, 'Bugs Bunny')  # use imported function

print(index)
print(test)


import random

random_looney = random.choice(looney_list)
print('Random Looney Tunes character:', random_looney)
