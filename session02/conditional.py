import datetime
now = datetime.datetime.now()
time = now.year
year = int(input("Ban sinh nam bao nhieu?"))
age = time - year
# print("tuoi cua ban la", age )
if age < 10:
    print("Baby")
elif age <= 18:
    print("Teenager")
else:
    print("Not Baby")

print("Bye")
