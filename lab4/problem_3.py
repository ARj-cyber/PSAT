#!/usr/bin/env python3

# Problem 3

'''
Read an integer,
print "YES" if its last digit is 7 and print "NO" otherwise.
'''

num = input("Enter the number : ")
if num[-1] == '7' :
	print('Yes')
else :
	print('No')
