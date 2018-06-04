for i in range(0,10):
    if i % 2 ==0:
        for j in range(0,10,2):
            print("1", end= ' ')
            print("0", end= ' ')
        print()
    else:
        for j in range(0,10,2):
            print("0", end= ' ')
            print("1", end= ' ')
        print()