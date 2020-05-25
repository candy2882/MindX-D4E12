from turtle import *
speed(-1)
color('blue')
a = 20
left(30)
for i in range(4):
    forward(a)
    left(90)
for j in range(a, 114, 2):
    for k in range(4):
        forward(j)
        left(90)
    left(10)
mainloop()