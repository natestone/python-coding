#
# Copyright Nate Stone 2023
# 
# BSD License
#

import sys
#print(sys.argv[1])
#print(sys.argv[2])

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

