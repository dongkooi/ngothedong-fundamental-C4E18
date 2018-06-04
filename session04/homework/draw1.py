from turtle import *

speed(-1)
shape("classic")
color("blue")

for i in range(20):
    for j in range(4):
        forward(100)
        left(90)
    right(360/20)    

mainloop()