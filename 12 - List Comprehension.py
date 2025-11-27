import os
import json

squares = []

for number in range(5):
    squares.append(number*number)

print(squares)

squares2 = [number * number for number in range(5)]
print(squares2)

salaires = [2000 , 4000 , 5000]
print([salaire*1.1 for salaire in salaires])

print([float(salaire) for salaire in salaires])

def double_salaire(my_list:list) -> list:
    return [m*2 for m in my_list]

new_salary = double_salaire(salaires)
print(new_salary)

#Avec des conditions
pairs = [n for n in range(10) if n % 2 == 0]
print(pairs)

cols = ["customer_file","date_blabla","date_bhe","hrg_date","end"]
filtered_cols = [col for col in cols if "date" in col]
print(filtered_cols)

wages = [30000, 45000, 50000, 24000, 32000]
augmentation = [salaire*1.2 if salaire > 35000 else salaire for salaire in wages]
print(augmentation)

def liste_parite(liste:list) -> list:
    return [True if n % 2 == 0 else False for n in liste]

test=liste_parite([56,34,24,77])
print(test)

my_dict = {
    "key1": "int",
    "key2": "float",
    "key3": "object",
    "key4": "int",
    "key5": "object",
}

keys_of_interest = [n for n in my_dict if my_dict[n] =="int"]
print(keys_of_interest)

#on ouvre les fichier que si il commence par drilling
liste_fichier = [machine for machine in os.listdir("data/raw") if machine[:8] == "drilling"]

for fichier in liste_fichier:
    with open(f"data/raw/{fichier}",'r') as f:
        machine = json.load(f)
    try:
        print(machine["machine_id"])
    except KeyError:
        print("Clé manquante")