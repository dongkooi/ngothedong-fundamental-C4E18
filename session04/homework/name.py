name = input("Your full name: ").lower()
while ("  " in name):
    name = name.replace("  ", " ")
fullname = name.title()

print("Update: ", fullname)