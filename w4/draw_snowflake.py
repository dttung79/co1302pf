import turtle as t

n = int(input('Enter the number of sides: '))
size = int(input('Enter the size of the snow: '))
angle = 360 / n

for _ in range(n):
    t.forward(size)
    t.backward(size)
    t.left(angle)

t.exitonclick()