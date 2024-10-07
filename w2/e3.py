# Calculate area and perimeter of a triangle
a = int(input('Enter triangle side a: '))
b = int(input('Enter triangle side b: '))
c = int(input('Enter triangle side c: '))

perimeter = a + b + c
p = perimeter / 2
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(f'Triangle ({a}, {b}, {c})')
print(f'Area: {area:.2f}')
print(f'Perimeter: {perimeter}')