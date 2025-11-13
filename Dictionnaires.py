ross = { "name" : "Geller",
         "girlfriend" : "Rachel",
         0 : 42,
}
print(ross)

cle = "name"
print(ross.get("name"))
print(ross.get("names"))
      

ross["sister"] = "Monica"
print(ross)

ross["girlfriend"] = "Emily"
print(ross)

# Another example:
warehouse_stocks = {"banana":200, "lettuce":20, "tomatoes": 50}
print(warehouse_stocks.get("tomatoes"))


benjamin_infos = {
		"age": 35,
		"years_in_company": 4,
		"salary": 250000,
}

print(benjamin_infos)

# nested dictionnaries:
dict_of_dict = {"benjamin": benjamin_infos, 
                "Emma": {"age":33, "years_in_company":20, "salary": 1000000}}
dict_of_dict["Emma"]
dict_of_dict["Emma"]["age"]


# update dictionnary:
my_dict = {}
my_dict["test"] = ["list", "of", "strings"]
my_dict

# keys, values
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())  # gives back a tuple

my_dict = {"key": [1, 2, 3]}

print(my_dict["key"][1])

drilling_machine = {
    "machine_id": "DM-001",
    "name": "Deep Driller 3000",
    "location": {
        "latitude": 29.7355,
        "longitude": -95.3635,
        "region": "Gulf of Mexico",
        "country": "USA",
    },
}

location = drilling_machine["location"]
country = location["country"]

print(country)

print(drilling_machine["location"]["country"])

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

#changement machine_id
id_letter, id_number = drilling_machine_two["machine_id"].split("-")
drilling_machine_two["machine_id"] = f"{id_letter}-{id_number.zfill(3)}"
print(drilling_machine_two["machine_id"])

#miles->km
drilling_machine_two["specifications"]["depth_capacity_meters"] = drilling_machine_two["specifications"]["depth_capacity_miles"]*1609
del(drilling_machine_two["specifications"]["depth_capacity_miles"])

drilling_machine_two["specifications"]["drilling_speed_meters_per_day"]=drilling_machine_two["specifications"]["drilling_speed_miles_per_day"]*1609
del(drilling_machine_two["specifications"]["drilling_speed_miles_per_day"])

#ajout des infos
drilling_machine_two["contact_information"] = {
    "operator_company": "Oceanic Drilling Inc.",
    "contact_person": "John Smith",
    "phone": "+1-555-123-4567",
    "email": "john.smith@oceanicdrilling.com"
  }

#date

yyyy,mm,dd = drilling_machine_two["last_maintenance_date"].split("-")
drilling_machine_two["last_maintenance_date"] = f"{yyyy}/{mm}/{dd}"

yyyy,mm,dd = drilling_machine_two["next_maintenance_due"].split("-")
drilling_machine_two["next_maintenance_due"] = f"{yyyy}/{mm}/{dd}"

print(drilling_machine_two)