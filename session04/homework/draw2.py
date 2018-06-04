from turtle import *

speed(-1)
shape("classic")
color("blue")

right(135)
dai = 150
for i in range(360):
    for j in range(4):
        forward(dai)
        right(90)
    right(15)
    dai = dai - 4
    if dai < 4:
        break
    
mainloop()