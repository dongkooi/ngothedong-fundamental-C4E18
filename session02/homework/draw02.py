from turtle import *

speed(-1)
color("blue")
for n in range(3,7,2):
    for i in range(n):
        forward(100)
        left(360/n)

    for i in range(n):    
        color("blue")
        forward(100)
        left(360/n)

color("red")
for n in range(4,7,2):
    for i in range(n):
        forward(100)
        left(360/n)  
    for i in range(n):
        forward(100)
        left(360/n)    



mainloop()