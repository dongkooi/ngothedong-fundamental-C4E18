import getpass

user = "qweqwe"
password = "123123"
u = input("User: ")
p = getpass.getpass('Pass:')
if u == user:
    if p == password:
        print("Welcom, c4e")
    else:
        print("Wrong password, please try again")
        # while (p == password):
        #     p = getpass.getpass('Pass:')
        #     if p == password:
        #         print("Welcom, c4e")
        #     else:
        #         print("Wrong password, please try again")
        #     break
if u != user:
    print("No such user, go away")
    