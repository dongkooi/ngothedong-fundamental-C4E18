n = int(input("n = "))

if n%2 != 0:
    for i in range(0,n):
        for j in range(0,n-1,2):
            print("1", end= ' ')
            print("0", end= ' ')
        print("1")
else:
    for i in range(0,n):
        for j in range(0,n,2):
            print("1", end= ' ')
            print("0", end= ' ')
        print()