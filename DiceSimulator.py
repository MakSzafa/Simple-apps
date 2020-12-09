import random

z = 1
print("This is dice simulator by Max\n")
while z == 1:
    number = random.randint(1, 6)
    z = 0

    if number == 1:
        print("|----------|")
        print("|          |")
        print("|     0    |")
        print("|          |")
        print("|----------|")
    elif number == 2:
        print("|----------|")
        print("|     0    |")
        print("|          |")
        print("|     0    |")
        print("|----------|")
    elif number == 3:
        print("|----------|")
        print("|     0    |")
        print("|     0    |")
        print("|     0    |")
        print("|----------|")
    elif number == 4:
        print("|----------|")
        print("|  0    0  |")
        print("|          |")
        print("|  0    0  |")
        print("|----------|")
    elif number == 5:
        print("|----------|")
        print("|  0    0  |")
        print("|     0    |")
        print("|  0    0  |")
        print("|----------|")
    elif number == 6:
        print("|----------|")
        print("|  0    0  |")
        print("|  0    0  |")
        print("|  0    0  |")
        print("|----------|")

    q = input("Do you want to dice again? (Y/N)\n")
    if q == "y":
        z = 1
    else:
        exit()

