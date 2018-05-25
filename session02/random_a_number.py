from random import randint
mood = randint(0, 100)
if mood < 30:
    print("T.T")
elif mood < 60:
    print(".-.")
else:
    print("Let's Rock & Roll")