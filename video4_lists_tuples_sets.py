#!/usr/bin/env python
import sys

# Following along with https://www.youtube.com/watch?v=W8KRzm-HUcc&t=0s&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=4


# LISTS
# Create with [ ]

#num_list = [1, 5, 2, 9, 4]
#print('Lowest num:', min(num_list))
#print('Highest num:', max(num_list))
#print('Sum of all nums', sum(num_list))


courses = ['CompSci', 'History', 'Calculus']
courses2 = ['French', 'Philosophy']
# print(len(courses))  # number of items in the list
# print(courses[-1])  # print last item
# print(courses[0:2])  # slice

# courses.append("Sociology")  # add new value to the end of the list
# courses.insert(0, courses2)	# insert courses2 into first element of courses (essentially a prepend)
# print(courses[0])		#shows that that insert method inserted a list object and not the list contents

# iterable
# courses.extend(courses2)  # this does what we wanted, which is add the courses2 elements to end of courses list

#print('pre-pop list:', courses)
# use list like a stack
# popped = courses.pop()  # pop from top of stack (which is newest item, ie a LIFO queue)
#print('we popped off:', popped)
# print('post-pop list:', courses)  # modified version of list, post-pop


# courses.reverse()  # modifies in-place
#print('reversed list:', courses)
# sorted_courses = sorted(courses)  # returns a sorted version of the list, without modifying original list

#print('Unsorted list:    ', courses)


# print('A-Z sorted list;', sorted_courses)  # ascending order by default
# print('Z-A tempsort list:', sorted(courses, reverse=True))  # ascending order by default, but can force reverse
# docs: sorted(iterable, *, key=None, reverse=False)


#print('index of course "Calculus":', courses.index('Calculus'))
#print('index of course "French":', courses.index('French'))

# for item in courses:		#I'll need to remember this needs colon, not curly
#    print(item)


#print('Enumerated list, with element index num')
# for index, course in enumerate(courses):
#    print(index, course)

# determine list membership; output is boolean True/False
#print('French' in courses)

# turn a list into a string and join with a char, seems same as perl
#course_string = ', '.join(courses)
#print('Comma separated list: ', course_string)

# make a list object from a string that is split on the specified char, same as perl
#list2 = course_string.split(', ')
#print('new list obj:', list2)

# so far so good, pretty straightforward and is very similar to what I know from perl

# TUPLES - immutable lists
# create with ( )

# not sure of the benefit yet, beyond preventing accidental modification
# supports all list methods that do not involve modification

#tuple_courses = ('CompSci', 'History', 'Calculus', 'Sociology', 'French', 'Philosophy')
#print('Tuple version of courses:',tuple_courses)
# attempt to modify, fails with TypeError
#tuple_courses[1] = 'Macro Economics'

# SETS - lists with unique elements and unordered
# perl equivalent:  hashes, but really only hash keys.  auto-elim dupes, direct access to a member, random order each time you access
# main benefit: more efficient to check list 'membership' since iteration isn't needed, including comparing two lists
# create with { }

#users = {'Pepe Le Pew', 'Yosemite Sam', 'Taz', 'Wile E. Coyote, Super Genius', 'Tweety'}
#users2 = {'Bugs Bunny', 'Taz', 'Tweety', 'Porky Pig'}
#print('Daffy in the list?', 'Daffy Duck' in users)
#print('Taz in the list2?', 'Taz' in users2)

# intersection to find shared items
#print('Shared items:', users.intersection(users2))
# members of one but not the other
#print('Diff:', users.difference(users2))

# combine unique members from both lists
#print('Union:', users.union(users2))


# creating empty list, tuple, set
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {}  # NOPE!  GOTCHA!  That's a 'dict', which I haven't learned yet, but I'm guessing it will be a complex data structure like perl hashes
print(type(empty_set)) # == class 'dict'
empty_set = set()  # correct way
print(type(empty_set)) # == class 'set'
