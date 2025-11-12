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

