#!/usr/bin/env python3


# Problem 04: Last two digits
# Given an integer number, print its last two digits.

print('Enter the number')
numbe = input('> ')
numbe = numbe+'0' # Concating with 0 for a correct proccesing of output
lst_dgt = numbe[-3:-1]  # this ignores -3rd & -1st positioned characters
print(lst_dgt)
