import json
from difflib import get_close_matches

print("This is dictionary by Max\n")
z = 1
data = json.load(open("data.json"))

while z == 1:

    search = input("What are you looking for?\n")
    search = search.lower()
    z = 0

    if search in data:
        for item in data[search]:
            print(item)
    elif search.title() in data:
        for item in data[search.title()]:
            print(item)
    elif search.upper() in data:
        for item in data[search.upper()]:
            print(item)
    elif len(get_close_matches(search, data.keys())) > 0:
        print("Did you mean %s instead?" %get_close_matches(search, data.keys())[0])
        decide = input("press y for YES or n for NO\n")
        if decide == "y":
            for item in data[get_close_matches(search, data.keys())[0]]:
                print(item)
        elif decide == "n":
            print("The word you entered doesn't exist in this dictionary.")
        else:
            print("You entered wrong input.")
    else:
        print("The word you entered doesn't exist in this dictionary.")

    q = input("\nPress 'y' if you want to use dictionary again\n")
    if q == "y":
        z = 1
    else:
        exit()