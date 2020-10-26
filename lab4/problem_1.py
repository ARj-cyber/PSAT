#!/usr/bin/env python3


# Problem 1

'''
In this problem, we want to print the message, "You should 
wear a jacket today!" if it's cold or windy, or the message 
"You don't need a jacket today!" if it's not.
'''

how_is_day =  input("How is the day today : ").lower()

if ( how_is_day ==( 'cold' or 'windy') ) :
	print('You should wear a jacket today!')
else :
	print("You don't need a jacket today")
