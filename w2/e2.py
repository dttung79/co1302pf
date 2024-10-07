# Calculate area and perimeter of a circle

PI = 3.14 # constant
radius = int(input('Enter circle radius: '))

area = PI * radius ** 2
perimeter = 2 * PI * radius

print(f'Circle ({radius})')
print(f'Area: {area:.2f}')
print(f'Perimeter: {perimeter:.2f}')