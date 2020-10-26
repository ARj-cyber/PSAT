#!/usr/bin/env python3


# Problem 8
# Read an integer, print "YES" if it is a three-digit number and print "NO" otherwise. 


num = input("Enter an integer : ")
if int(num)>99 and int(num)<=999 :
    print("Yes") 
else :
    print("No")