#!/usr/bin/env python3


# Problem 7
# Read three different integers, print YES if they are given in ascending order, print NO otherwise. 

num1,num2,num3 = input("Enter the numbers : ").split()
if (int(num1)<int(num2) and int(num2)<int(num3)) :
    print("YES")
else :
    print("NO")