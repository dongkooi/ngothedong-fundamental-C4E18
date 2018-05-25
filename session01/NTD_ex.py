from turtle import *

n = int(input("nhap so canh cua hinh"))

speed(-1)
shape("turtle")
color("green")
fillcolor("yellow")

begin_fill()
for i in range(n):
    forward(100)
    left(360/n)
    # forward(100)
    # left(360/n)
    # forward(100)
    # left(360/n)
    # forward(100)
    # left(360/n)
    # right(1)

end_fill()

mainloop()