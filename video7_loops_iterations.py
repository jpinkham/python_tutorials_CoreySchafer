#!/usr/bin/env python
import sys

# let's be certain which version/executable of python we are running the script under
print("Python interpreter: ", sys.executable, "\n")
# print(sys.version)

# Following along with https://www.youtube.com/watch?v=6iF8Xb7Z3wQ
# Topic: Loops & Iterations

days = ['mon', 'tue', 'wed']

# break = exits innermost-loop early once a conditional is met
# continue = continue looping  (== perl 'next')

for day in days:
    print('Current day >', day, '<')
    if day == 'tue':
        print('Found', day)
        break


for day in days:
    if day == 'tue':
        continue
    print('Current day >', day, '<')


for day in days:
    for letter in 'abcd':
        print(day, letter)


# range()
for i in range(6):  # (will do 0,1, 2, 3, 4, 5)
    print(i)

print('\n')

for i in range(2, 6):  # (will do 2, 3, 4, 5)
    # PERL EQUIV    for(my $i = 2; $i < 6; $i++)
    print(i)

print('\n')

# EQUIV code using while loop
x = 2
while x < 6:
    print(x)
    x = x + 1
#        x + +  #Is there no ++ shortcut in python? Sublime keeps spacing this out everytime I save
#		python DOES support x += 1

print('\n')

x = 0
while True:  # indefinitely continue
    #    if x == 4:
 #       break		#without this conditional, you have to do Ctrl+C to stop infinite loop
    print(x)
    x += 1
