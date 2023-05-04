#
# Copyright Nate Stone 2023
# 
# BSD License
#

import sys
import math

#print(sys.argv[1])
#print(sys.argv[2])


# Check if the user input the correct number of inputs
if (len(sys.argv) < 3) or (len(sys.argv) > 3):
    print "usage: python basic_structures.py [-h|-g] [name]"
    quit()

opt = sys.argv[1]
person = sys.argv[2]


# Greeting Function
def greeting(greetingType):
     i = 0
     while i < 12:
        i = i + 1
        print(greetingType + ", " + person + "! (" + str(i) + ")")


# Main Code
if opt == '-h':
    greeting('Hello')
elif opt == '-g':
    greeting('Goodbye')


fruits = ["apple", "banana", "cherry"]

#
#  [
#    0 => "apple",
#    1 => "banana",
#    2 => "cherry"
#  ]
#

# python
for index, fruit in enumerate(fruits):
    print((index + 1), fruit)


# Now for some math

