#
# Copyright Nate Stone 2023
# 
# BSD License
#
#
# Usage: python3.10 basic_structures.py [-h|-g] [name]
#
#
# https://github.com/Makeblock-official/PythonForMegaPi
# https://support.makeblock.com/hc/en-us/articles/1500012868722-Program-mBot-Mega-with-Raspberry-Pi-in-Python
# https://gist.github.com/xeecos/5fa6cb5876a8c9449562d8026942fff1/revisions
# https://gist.github.com/xeecos/0a326e03f44633fed726867b0e71a3fe
# https://gist.github.com/xeecos/ceeb8fd83cc15b4e83b713bb75a982fd
#

import sys
import math
import numpy as np
import cyberpi
#from makeblock import MegaPi,SerialPort

#print(sys.argv[1])
#print(sys.argv[2])


# Check if the user input the correct number of inputs
if (len(sys.argv) != 3):
    print("usage: python3.10 basic_structures.py [-h|-g] [name]")
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
print("Math Time")
theNumber = 8.2394290
print(math.ceil(theNumber))
print(math.pi)

# Standard deviation example
a = np.array([1, 2, 3, 4])
print(np.std(a))
