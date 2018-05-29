# food1 = "Salad Nga"
# food2 = "Chocolate"
# food3 = "Sò"
# food4 = "Mỳ Tôm"
# food5 = "Phở"

#  list (array)
# CRUD
#   C: create
#      R: read
#        U: update
#       D: delete

    #create
menu = ["Salad Nga", "Chocolate", "Sò", "Mỳ tôm", "Phở"]

    #read
    #seperator: sep=""
# print(*menu, sep=", ")

    #append() - thêm
    #len - đếm số phần tử trong list
# menu.append("Bánh mướt")
# print(*menu, sep=", ")
# print(len(menu), sep=", ")

# first_item = menu[0]
# print(first_item)
# for i in range(len(menu)):
#     print("{0}. {1}".format(i + 1, menu[i]))

# print("*"*20)

for index, item in enumerate(menu):
    print("{0}. {1}".format(index + 1, item))

# print("*"*20)

# for item in menu:
#     print(item)



        #update 
menu[2] = "Cua"

print(*menu, sep=', ')