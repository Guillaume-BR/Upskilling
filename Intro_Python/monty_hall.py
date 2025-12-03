from typing import List

rideau_voiture = 2
rideau_ouvert = ""

def demander_le_rideau(options: List) -> int:
    while True:
        try:
            rideau_ouvert = int(input(f"Quel rideau ouvrir: {options} ?"))
            if rideau_ouvert not in options:
                raise ValueError(f"L'option doit être dans {options}")
            break
        except ValueError as e:
            print(e)
            print("That's not a valid option!")
    return rideau_ouvert


rideau_ouvert = demander_le_rideau([1, 2, 3])
if rideau_ouvert == 1:
    print("Je vous montre le rideau 3: c'est une chèvre !")
    print("Voulez-vous changer de rideau ?")
    rideau_ouvert = demander_le_rideau([1, 2])
else:
    print("Je vous montre le rideau 1: c'est une chèvre !")
    print(" Voulez-vous changer de rideau ?")
    rideau_ouvert = demander_le_rideau([2, 3])

if rideau_ouvert == 2:
    print("Félicitations, vous avez gagné la voiture !!")
else:
    print("Désolé, vous avez gagné une chèvre")