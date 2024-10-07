# Write a program to calculate the area and perimeter of a rectangle.
# Ask user to enter width and height of the rectangle.

width = int(input('Enter rectangle width: '))
height = int(input('Enter rectangle height: '))

area = width * height
perimeter = 2 * (width + height)

print(f'Rectangle ({width}, {height})')
print(f'Area: {area}')
print(f'Perimeter: {perimeter}')