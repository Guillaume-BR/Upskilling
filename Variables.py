dayly_rate = 500
worked_day = 20
revenue = dayly_rate * worked_day
print(revenue)

ma_boite = 800
my_string = f'ma boite contient {ma_boite}'
print(my_string)

date = "2024/12/25"
day = date[-2:]
month = date[-5:-3]
year = date[0:4]

print(f"mois : {month}, jour : {day}, annee : {year}")

jour_mois_annee = date.split("/")
print(f"annee: {jour_mois_annee[0]}")

#révision
machine_id = "DM-2"
serial_nb = machine_id[-1:].zfill(3)
machine_id = machine_id.replace("2",serial_nb)
print(machine_id)

print("42"[1])


print("tom marvolo riddle"[:3]) 

print("django".capitalize())

print("Da Vinci Code"[-4:].lower())

