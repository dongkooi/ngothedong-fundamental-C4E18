from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
shape("turtle")

dai = 20 * len(colors)
for i in range(len(colors)):
    fillcolor(colors[len(colors) - i - 1])
    begin_fill()
    for j in range(2):
        forward(dai)
        left(90)
        forward(40)
        left(90)
    end_fill()
    dai -= 20


mainloop()