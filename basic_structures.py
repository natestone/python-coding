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

if opt == '-h':
     i = 0
     while i < 12:
        i = i + 1
        print("Hello, " + person + "! (" + str(i) + ")")
elif opt == '-g':
     i = 0
     while i < 12:
        i = i + 1
        print("Goodbye, " + person + "! (" + str(i) + ")")


