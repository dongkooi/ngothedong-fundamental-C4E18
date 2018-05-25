# for i in range(4):
#     print('*' * 5)

# print("hello", end = ' ')
# print("world")

# for i in range(10):
#     for j in range(i):
#         print("*" , end = " ")
#     print()


for i in range(10):
    for j in range(10):
        if j <= 10 - i - 1:
            print(" ", end= '')
        else:
            print("*", end= '')
    print()