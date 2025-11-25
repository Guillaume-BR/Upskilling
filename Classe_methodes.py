warehouse_one = {
    "Location": "Paris",
    "surface_area": 1040,
    "manager": "Tom Felton",
    "n_employees": 12,
    "storage": {"item1": 24, "item2": 42, "item3": 56},
 }

def quantite_moyenne(dico:dict) -> dict:
    valeurs = dico["storage"].values()
    total = sum(valeurs)
    return total / dico["n_employees"]

print(quantite_moyenne(warehouse_one))

#warehouse_two = {
#    "surface_area" : 2000,
#    "manager" : "Emma",
#    "storage" : {"item1" : 12, "item2":25,},
#}
#
#print(quantite_moyenne(warehouse_two))

class Warehouse:
    def __init__(self,location,manager):
        print("ce code s'exécute lorsqu'on crée une instance de cette classe")
        self.location = location
        self.manager = manager
    pass

warehouse_one = Warehouse("Paris","Tom")
print(warehouse_one.location)
print(warehouse_one.manager)

class DrillingMachine:
    def __init__(self,
                 machine_id:str,
                 name:str,
                 location:str,
                 status:str,
                 specifications:dict,
                 last_maintenance_date:str,
                 next_maintenance_due:str,
                 contact_information:dict
                 ) -> None:
        self.machine_id = machine_id
        self.name = name
        self.location = location
        self.status = status
        self.specifications = specifications
        self.last_maintenance_date = last_maintenance_date
        self.next_maintenance_due = next_maintenance_due
        self.contact_information = contact_information
    pass

from typing import Dict


class Warehouse:

    def __init__(self, location: str, manager: str, storage: Dict[str, int]) -> None:
        self.location = location
        self.manager = manager
        self.storage = storage

    def compute_total_items(self) -> int:
        return sum(self.storage.values())
    
    def moyenne_article(self) -> float:
        return self.compute_total_items() / len(self.storage.values())


items = {"item1": 24, "item2": 42, "item3": 56}
warehouse_one = Warehouse("Paris", "Tom Felton", items)

total_items = warehouse_one.compute_total_items()

moy_items = warehouse_one.moyenne_article()

print(warehouse_one.storage)

print(total_items)
print(moy_items)