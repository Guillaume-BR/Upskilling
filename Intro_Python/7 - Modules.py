my_string = """ 
Ceci est une chaine de caractère
qui tient sur plusieurs lignes
Essayez de faire ça avec une seule au début
et une seule autre à la fin pour voir !
"""

print(my_string)

import requests
import json


response = requests.get("https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=capricorn&day=today")
data = response.json()  # Convert the response to JSON

with open("horoscope_data.json", "w") as file:
    json.dump(data, file)

#  après ça, faites un cat horoscope_data.json dans votre terminal :) 


# Pour ouvrir votre json dans Python, vous pourrez ensuite faire:
with open("horoscope_data.json", "r") as file:
    json.load(file)

from calculations.arithmetic import addition
print(addition(5,7))

from string_utils import zfill_machine_id
id_machine2 = zfill_machine_id("DM-2")
print(id_machine2)

from string_utils import *

file_to_read = "machine.json"
file_to_write = f"updated_{file_to_read}"

with open(file_to_read,"r") as file:
    machine2 = json.load(file)


machine2 = convert_miles_km(machine2)
machine2 = ajout_info(machine2)
machine2 = update_date(machine2)
machine2 = format_machine_id(machine2)

with open(file_to_write,"w") as file:
    json.dump(machine2,file)