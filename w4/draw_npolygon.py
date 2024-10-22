import turtle as t

n = int(input('Enter the number of sides: '))
size = int(input('Enter the size of the polygon: '))

angle = 180 - (180 * (n - 2) / n)

for _ in range(n):
    t.forward(size)
    t.left(angle)

t.exitonclick()