print(type(42))

my_tuple = tuple([1,2])

print(my_tuple[0])

#fonction open
fichier = open('ultima_verba.txt','r')
contenu = fichier.read()
print(contenu)
fichier.close()

fichier = open('test.txt','a') #w pour write (mais écrase), r pour read, a pour append
fichier.write(" ce soir")
fichier.close()

fichier = open('ultima_verba.txt','a')
#fichier.write("\nVictor Hugo, Jersey, 2 décembre 1852")
fichier.close()

#age = input("Insérez votre age: ")
#print(f"Vous avez {age} ans")

def hello_there():
    print("hello_there")

hello_there()

def print_bonjour(x):
    print(f"Bonjour {x}")

print_bonjour("Benoit")

def jesus(pain: int,nombre: int) -> int:
    return pain*nombre

print(jesus("trois",3))

def divede(x: int|float, y: int|float) -> int | float:
    return x/y

print(divede(4,3))

drilling_machine_two = {
  "machine_id": "DM-2",
  "name": "Land Rover 200",
  "location": {
    "latitude": 37.7749,
    "longitude": -107.9090,
    "region": "San Juan Basin",
    "country": "USA"
  },
  "status": "Under Maintenance",
  "specifications": {
    "type": "Onshore",
    "depth_capacity_miles": 7,
    "drilling_speed_miles_per_day": 0.3,
    "crew_size": 25,
    "power_source": "Electric"
  },
  "last_maintenance_date": "2024-07-15",
  "next_maintenance_due": "2025-01-15"
}

def fonction_harmonize_machines(dico : dict) -> dict:
    #miles -> km
    dico["specifications"]["depth_capacity_meters"] = dico["specifications"]["depth_capacity_miles"] * 1609
    dico["specifications"]["drilling_speed_meters_per_day"] = dico["specifications"]["drilling_speed_miles_per_day"] * 1609
    del(dico["specifications"]["depth_capacity_miles"])
    del(dico["specifications"]["drilling_speed_miles_per_day"])

    #ajout_info
    dico["contact_information"] = {
        "operator_company" : None,
        "contact_person" : None,
        "phone" : None,
        "email" : None,
    }

    #maintenace date
    dico["last_maintenance_date"] = "/".join(dico["last_maintenance_date"].split("-")[::-1])
    dico["next_maintenance_due"] = "/".join(dico["next_maintenance_due"].split("-")[::-1])

    #machine_id
    letter, number = dico["machine_id"].split("-")
    dico["machine_id"] = f"{letter} - number.zfill(3)"

    return dico

drilling_machine_two = fonction_harmonize_machines(drilling_machine_two)
print(drilling_machine_two)


my_string = """
Ceci est une chaine de caractère
qui tient sur plusieurs lignes
Essayez de faire ça avec une seule " au début
et une seule autre " à la fin pour voir !
"""

