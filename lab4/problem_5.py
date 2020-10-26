#!/usr/bin/env python3


# Problem 5
# Read two integers, print "YES" if at least one of them is odd and print "NO" otherwise.

num1,num2 = input("Enter the number : ").split()

if (int(num1)%2 != 0) or (int(num2) %2 !=0) :
    print("YES")
else:
    print("NO")