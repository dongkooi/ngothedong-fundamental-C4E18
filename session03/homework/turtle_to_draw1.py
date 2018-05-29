from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
speed(-1)
shape("turtle")

for index, item in enumerate(colors):
    color(item)
    for i in range(index + 3):
        forward(100)
        left(360/(index + 3 ))


mainloop()