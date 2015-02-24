#David Buff
#Spiral Generator

import turtle

def spiral(num, angle, gap):
	for i in range(num * (360 // angle)):	#Each spiral is going to need all of its sides drawn, a side is 360 / angle ie. 360 / 90 is 4, a square.
		turtle.fd(gap + (i * gap))			#The spiral starts out with length gap and increases to the number of spirals draws, i.
		turtle.left(angle) 					#Turns the turtle to the given angle

num = int(input('How many spirals? '))		#All the inputs with the exception of color needs to be converted into numbers.
gap = float(input('The gap between each spiral? '))	#A float so that you can get smooth curves with small angles
angle = int(input('Angle of spirals? '))	#Angle is kind of like the resolution of the curve.
color = input('Color? ')					#Must be a valid turtle color.

turtle.color(color) 	#Set the color.
spiral(num, angle, gap)	#Run the function

turtle.Screen().exitonclick() #Wait for a click to close.