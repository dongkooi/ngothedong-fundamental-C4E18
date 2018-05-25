# from turtle import *

# n = 100

# speed(-1)
# shape("turtle")
# color("black")

# for i in range(0, n, 2):
#     forward(i)
#     left(90)
    

# mainloop()


from turtle import *

n = 100

speed(-1)
shape("turtle")
color("black")

length = 5

for i in range(n):
    forward(length)
    left(90)
    
    length += 5 #length = lenght + 5

mainloop()