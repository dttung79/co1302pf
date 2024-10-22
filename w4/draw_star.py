import turtle as t

size = int(input('Enter the size of the star: '))

for _ in range(5):
    t.forward(size)
    t.right(144)

t.exitonclick()