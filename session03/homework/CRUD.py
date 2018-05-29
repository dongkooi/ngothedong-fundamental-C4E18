shop = ["T-Shirt", " Sweater"]
while True:
    what = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if what == "R":
        print("Our items: ", end = '  ')
        print(*shop, sep=',')
        break
    elif what == "C":
        new = input("Enter new item: ")
        shop.append()
        print("Our items: ", end = "  ")
        print(*shop, sep=',')
        break
    elif what == "U":
        position = int(input("Update position? "))
        shop[position - 1] = input("New item? ")
        print("Our items: ", end = "  ") 
        print(*shop, sep=',')
        break
    elif what == "D":
        delete = int(input("Delete position? "))
        del shop[delete]
        print("Our items: ", end = "  ")
        print(*shop, sep=',')
        break
    else:
        print("Wrong! Enter again!")
        break
    



