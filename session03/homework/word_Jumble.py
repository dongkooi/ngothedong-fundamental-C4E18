from random import choice
word = ["Songoku", "Luffy", "Yasuo"]
onlyword = choice(word)
chars = list(onlyword)
nw = []

for i in range(len(chars)):
    w = choice(chars)
    nw.append(w)
    chars.remove(w)
print(*nw, sep=" ")

while True:
    enter = input("Your answer: ")
    if enter == onlyword:
        print("Bingo^^")
        break
    else:
        print("Not correct! Try again!")
        break
