#!/usr/bin/env python3


# Problem 10
'''
Read three integers, determine how many of them are equal.
The program must print one of these numbers: 
   a. 3 (if all are the same),  
   b. 2 (if two of them are equal and the third is different) 
   c. 0 (if all numbers are different).
'''

num1,num2,num3 = input ("Enter the integers : ") .split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
if num1 == num2 and num2 == num3 and num3 == num1 :
    print("3")
elif num1 == num2 or num2 == num3 or num3 == num1 :
    print("2")
else :
    print ("0")