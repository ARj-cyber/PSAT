#!/usr/bin/env python3


# Problem 9
# Read 3 integers, print the smaller value. 


a,b,c= input("Enter Three numbers seperated by space : ").split()
if (int(a)<int(b)<int(c)):
    print(a)
elif (int(a)>int(b)>int(c)):
    print(c)
else :
    print(b)