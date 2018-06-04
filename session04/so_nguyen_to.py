n = int(input("Enter a number: "))

# is_prime = True

# for i in range(2,n):
#     if n % i == 0:
#         is_prime = False
#         break

# if is_prime:
#     print("{0} is a prime number".format(n))
# else:
#     print("{0} is not a prime number".format(n))

count = 0

for i in range(1,n):
    if n % i == 0:
        count += 1

if count == 1:
    print("{0} is a prime number".format(n))
else:
    print("{0} is not a prime number".format(n))
    
