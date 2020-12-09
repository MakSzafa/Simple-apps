import random
i = 1
print('Witaj w grze "Kamien, Papier, Nożyce"\n')
while i > 0:
    zagranie = input("Wybierz zaganie (k - kamien / p - papier / n - nozyce)\n")
    zagranie2 = random.choice(["k", "p", "n"])
    print("Wybrales: ", zagranie)
    print("Komputer wybral: ", zagranie2)
    if zagranie == "k" and zagranie2 == "n":
        print("Gratulacje, wygrales !!! :-)")
    elif zagranie == "k" and zagranie2 == "p":
        print("Tym razem przegrales ;(")
    elif zagranie == "k" and zagranie2 == "k":
        print("Remis !")
    elif zagranie == "p" and zagranie2 == "k":
        print("Gratulacje, wygrales !!! :-)")
    elif zagranie == "p" and zagranie2 == "n":
        print("Tym razem przegrales ;(")
    elif zagranie == "p" and zagranie2 == "p":
        print("Remis !")
    elif zagranie == "n" and zagranie2 == "p":
        print("Gratulacje, wygrales !!! :-)")
    elif zagranie == "n" and zagranie2 == "k":
        print("Tym razem przegrales ;(")
    elif zagranie == "n" and zagranie2 == "n":
        print("Remis !")
    wyjscie = input("Czy chcesz zagrac ponownie (T/N)?\n")
    if wyjscie == "n":
        break
