#!/usr/bin/env python3


# Problem 05: Fractional part
# Given an integer, print its fractional part.



import math
no = input ("Enter the number ")
answ = float (no)
a = math.modf(answ)

print (">>> ",a[0])
