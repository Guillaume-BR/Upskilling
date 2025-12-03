try:
   int("salut")
except ValueError as ve:
   print(ve)
   print("yo")

def parite() -> str:
    while True:
        try:
            nombre = int(input("donne moi un nombre entier"))
            break
        except ValueError as e:
            print(e)
            print("je veux un entier, merde !")
    if nombre % 2 == 0:
        print("pair")
    else:
        print("impair")

parite()