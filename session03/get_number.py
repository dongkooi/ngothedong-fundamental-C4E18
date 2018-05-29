from random import randint
mood = randint(0, 100)
count = 0
loop = True
while loop:
    if count < 7:
        n = int(input("Enter your number? "))
        if n < mood:
            print("Too small :(")
        elif n > mood:
            print("A little too large :(")
        else:
            print("Bingo ^^")
            loop = False
    else:
        print("You lose!")
        loop = False
    count +=1 