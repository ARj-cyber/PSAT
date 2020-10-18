#!/usr/bin/env python3


# Problem 07 : Shapes

import math

print ("Cylinder or Trapezoid ? ")
what = input ("[+]  ")
whata = what .lower()

# Calculate and display the volume and area of a cylinder
if whata == 'cylinder' :
	hei_cyl =input("Enter the height of Cylinder : ")
	rad_cyl =input("Enter the Radius of Cylinder : ")
	vol_cyl = ( math.pi * (int(rad_cyl) ** 2) * int( hei_cyl) )
	area_cyl = ( 2 * math.pi * int(rad_cyl) * int(hei_cyl) ) + ( 2 * math.pi * ( int(rad_cyl) ** 2 ) )
	print ( f"The Volume of Cylinder is : {(vol_cyl)} \n The Area of cylinder is : {area_cyl} ")

# Calculate the area of a trapezoid
elif whata == 'trapezoid' :
	a = input("Enter the length of side A : ")
	b = input("Enter the length of side B : ")
	h = input("Enter the length of Height : ")
	area_trap = ( ( int(a)+int(b) ) / 2 ) * int(h)
	print ( "The Area of " , what , " is ", area_trap )

else :
	print ( "x X --ERROR-- Xx" )
