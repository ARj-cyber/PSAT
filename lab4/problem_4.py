#!/usr/bin/env python3


# Problem 4
# Read two integers, print "YES" if they are both odd and print "NO" otherwise. 

num1,num2 = input("Enter the number : ").split()

if (int(num1)%2 == 0)and (int(num2) %2 ==0) :
    print("NO")
else:
    print("YES")