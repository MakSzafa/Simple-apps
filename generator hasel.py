import random
print("Witaj w generatorze hasel by Max Szafa\n")
charsUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
charsLow = "abcdefghijklmnopqrstuvwxyz"
charsNumber = "0123456789"
charsSpecial = "!@#$%&*()[]{}"
i = 5
while i > 0:
    password = ''
    ilosc = int(input("Podaj z ilu znakow ma skladac sie twoje haslo:\n"))
    for i in range (ilosc):
        znak = random.randint(1,4)
        if znak == 1:
            password += random.choice(charsUpper)
        elif znak == 2:
            password += random.choice(charsLow)
        elif znak == 3:
            password += random.choice(charsNumber)
        elif znak == 4:
            password += random.choice(charsSpecial)
    print("Wygenerowane haslo to: ", password)
    ponow = input("Czy chcesz wygenerowac nowe haslo? (T/N)\n")
    if ponow == "n":
        break
