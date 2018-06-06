def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1)+F(n-2)
    
month = int(input("Enter months: "))

rabbit = 1
for i in range(month):
    rabbit = rabbit + F(i)
    print("Month {0} : {1} pair(s) of rabbit".format(i + 1, rabbit))