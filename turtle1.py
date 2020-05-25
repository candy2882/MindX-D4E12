from turtle import *
speed(-1)
color('blue')
a = 200
for i in range(20):
    for j in range(2):
        forward(a/2)
        left(90)
    forward(a)
    left(90)
    for j in range(2):
       forward(a/2)
       left(90)
    left(50)
mainloop()