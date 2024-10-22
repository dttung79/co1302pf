# draw a square

from turtle import * # import everything from the turtle module
# define a variable to store the size of the square
size = int(input('Enter the size of the square: '))

for _ in range(4):
    forward(size)
    left(90) # turn left by 90 degrees

exitonclick() # close the window when clicked on it
