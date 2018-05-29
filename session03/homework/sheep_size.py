sheep = [5, 7, 300, 90, 24, 50, 75]
print("Hello my name is Đông and these are my ship sizes")
print(sheep)
print()

print("Now my biggest sheep has size ",max(sheep)," let's shear it")
print()

sheep[sheep.index(max(sheep))] = 8
print("After shearing, here is my flock")
print(sheep)
print()


for i in range(4):
    money = 0
    print("MONTH", i + 1)
    for j in range(len(sheep)):
        sheep[j] = sheep[j] + 50
        money += sheep[j]  
    print("Onne month has passed, now here is my flock")
    print(sheep)
    print("Now my biggest sheep has size ",max(sheep)," let's shear it")
    sheep[sheep.index(max(sheep))] = 8
    print("After shearing, here is my flock")
    print(sheep)
    print("My flock has size in total: ",money)
    print("i would get ",money,"* 2$ = ",money*2," $")
    



