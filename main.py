import json
from string_utils import *

file_to_read = "drilling_machine4.json"
file_to_write = f"updated_{file_to_read}"


with open(file_to_read,'r') as file:
    machine = json.load(file)

machine = update_date(machine)

if "machine_id" in machine.keys():
    machine = format_machine_id(machine)
else:
    machine["machine_id"] = machine["machine_ID"]
    del machine["machine_ID"]
    machine = format_machine_id(machine)

if "contact_information" not in machine.keys():
    machine = ajout_info(machine)


def miles_in_spec(specification:str) -> bool:
    return "miles" in specification

pres = list(filter(miles_in_spec,machine["specifications"].keys()))

if len(pres) != 0:
    machine = convert_miles_km(machine)

print(machine)

with open(file_to_write,'w') as file:
    json.dump(machine,file)

