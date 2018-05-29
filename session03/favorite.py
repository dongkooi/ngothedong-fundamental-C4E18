like = ["ăn", "ngủ", "chơi"]

print("your favorite: ")
for i in range(3):
    print(i+1, ".", like[i], sep='')
print("*"*20)
n = int(input("Position you want to update? "))
like[n - 1] = input("your favorite? ") 

# for i in range(len(like)):
#     print(i+1, ". ", like[i])

# string for matting

for i in range(len(like)):
    print("{0}.{1}".format(i + 1, like[i]))
