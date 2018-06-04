import getpass

user = "qweqwe"
password = "123123"
u = input("User: ")
count = 0
while True:
    if u == user:
        p = getpass.getpass('Pass:')
        if p == password:
            print("Welcom, c4e")
            break
        else:
            print("Wrong password, please try again")
    elif u != user:
        print("You are not super user")
        u = input("User: ")
    count +=1
    if count == 3:
        print("faild")
        break