import json
from string_utils import *

liste_machine = []
for i in range(1,6):
    liste_machine.append(f"drilling_machine{i}.json")

for fichier  in liste_machine:
    with open(f"data/raw/{fichier}",'r') as file:
        machine = json.load(file)
    
    machine = remove_useless_data(machine)
    machine = convert_miles_km(machine)
    machine = ajout_info(machine)
    machine = update_date(machine)
    machine = format_machine_id(machine)

    with open(f"data/processed/{fichier}",'w') as f:
        json.dump(machine,f,indent=4)
    

