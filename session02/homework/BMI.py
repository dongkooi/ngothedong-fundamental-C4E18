h = int(input("Your height(cm) = "))
weight = int(input("Your weight(km) = "))

height = h / 100
bmi = weight / height**2
if bmi < 16:
    print("Severely")
elif bmi <=30:
    if bmi <= 18.5:
        print("Underweight")
    elif bmi <= 25:
        print("Normal")
    else:
        print("Overweight")
else:
    print("Obese")
