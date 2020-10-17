#!/usr/bin/env python3

# Problem 06: Ice-Cream
'''
If Ram buys two ice creams, each costing Rs 50 and
Shyam buys three ice creams, each costing Rs 40, 
write a Python program to determine the total price
 of ice creams bought by Ram and Shyam. 
'''

# Getting the names as input
name_a = input ('1 . Name here : ' )
name_b = input ('2 . Name here : ' )


# Getting and calculating more details from name_a
print ( 'How much ice cream does ' + name_a + ' bought? ' )
num_a = input ( '>>> : ' )
price_a = input ( "What was the price of Ice cream that " + name_a +' bought? \n >>> : ' )
tol_prce_a = ( int ( num_a) * int ( price_a ) )


# Getting and calculating more details from name_b
print ( 'How much ice cream does ' + name_b + ' bought? ' )
num_b = input ( '>>> : ' )
price_b = input ( "What was the price of Ice cream that " + name_b +' bought \n >>> : ' )
tol_prce_b = ( int ( num_b ) * int ( price_b ) )

# Calculating the deatails from the both and printing it
total_price = ( int(tol_prce_a ) + int ( tol_prce_b ) )
print ( f'Total price of the Ice creams both {name_a} and {name_b} bought is : {total_price}' )
