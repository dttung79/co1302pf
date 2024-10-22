import turtle as t

n = int(input('Enter the number of mountains: '))
size = int(input('Enter the size of the mountains: '))
increase = 10
for _ in range(n):
    t.left(60)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.left(60)
    size += increase

t.exitonclick()