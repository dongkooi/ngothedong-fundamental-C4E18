tudien = {
    "ck": "Chồng",
    "vk": "vợ",
    "p": "bạn"
}

while True:
    print("*"*20)
    for k in tudien:
        print(k, end="\t ")

    print()
    user = input("Your code? ")
    if user in tudien:
        print("Translation: ", tudien[user])
    else:
        anw = input("Not found, do you want to contribute this word? (Y/N)? If you want to exit, plese write:'exit'! ").lower()
        if anw == "y":
            new = input("Enter your tranlation: ")
            tudien[user] = anw
            print("Updated")
        elif anw == "n":
            print("Exit")
        elif anw == "exit":
            break    

        
            
