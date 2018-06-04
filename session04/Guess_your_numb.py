low = 0
hight = 100
mid = (low + hight) // 2
input("Enter")
print("""
All you have to do is to answer to my guess
'c' if my guess is 'C'orrect
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number""")
while True:
    ans = input("Is {0} your number?".format(mid)).lower()
    if ans == 'l':
        hight = mid
    elif ans == 's':
        low = mid
    else:
        print("I knew it!")
        break
    mid = (low + hight) // 2
    if (hight - low) == 1 or (hight - low) == 0:
        print("You lie!")
        break
    

