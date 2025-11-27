from string_utils import *
import json

file_to_read = "drilling_machine3.json"

with open(file_to_read,"r") as file:
    machine3 = json.load(file)

print(machine3)

convert_miles_km(machine3)

update_date(machine3)

print(machine3)

ajout_info(machine3)

print(machine3)

food = ["banana", "apple", "orange", "kiwi"]

print("banana" in food)
print("grape" in food)

print("key" in {"key": "value"})
print("value" in {"key": "value"})

ma_condition = "whatever"
print(ma_condition == "whatever")

if ma_condition == "whatever":
    print("la condition est vraie, le code est exécuté")


#user_variable = input("type in your age: ")

#if int(user_variable) % 2 == 0:
#    print(f"Votre âge est pair et vous avez {user_variable} ans")
#else:
#    print(f"Votre âge est impair et vous avez {user_variable} ans")
#
#if int(user_variable) < 27:
#    print("49€ / an:  30% garantis sur tous les trains TGV INOUI et INTERCITÉS en 2nd et 1er classe")
#elif int(user_variable) < 64:
#    print("70€ / an:  30% garantis sur tous les trains TGV INOUI et INTERCITÉS en 2nd et 1er classe")
#else: 
#    print("gratuit")
#
#carte = input("Avez-vous une carte de réduction (oui/non) ? ").strip().lower() == "oui"
#
#membre = input("Êtes-vous membre du programme de fidélité (oui/non) ? ").strip().lower() == "oui"
#
#if (carte and int(user_variable) > 18) or membre:
#    print("c'est bon tu rentres")
#else: 
#    print("tu ne rentres pas")
#
print(len(machine3))

for element in range(1,16,2):
    print(element)

print(isinstance(machine3, bool))

grades_class_a = [11, 10, 8, 12, 9, 10]
grades_class_b = [20, 20, 20, 0, 0, 0]

mean_a = sum(grades_class_a)/len(grades_class_a)
mean_b = sum(grades_class_b)/len(grades_class_b)

print(mean_a,mean_b)

print(min(grades_class_a), max(grades_class_a))

print(min(grades_class_b), max(grades_class_b))

names = ["Ross", "Monica", "Rachel", "Chandler"]
family_name = ["Geller", "Geller", "Green", "Bing"]

zipped = zip(names,family_name)
print(list(zipped))

          