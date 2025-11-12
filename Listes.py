its_easy_as = [i for i in range(1,4)]
print(its_easy_as)

title = [4,"mariages", "et", 1 , "enterrement"]

sda = ["sda1", "sda2", "sda3"]
movies = ["Titanic", "Django", sda] 
print(movies)

# vous avez une liste de courses:
groceries = ["tomatoes", "carrots", "bananas"]

print(groceries.reverse())
print(groceries)

# essayez le code suivant : 
my_list = [1, 2, 3]
print(len(my_list))

my_list = ["et", 1, "et", 2, "et", 3, "zé", "ro"]
print(len(my_list))

# qu'en déduisez vous sur la fonction len() ?
# le slicing et l'indexing fonctionnent comme avec les strings
# récupérez le premier item de votre liste
print(my_list[0])
# récupérez le 2e et le 3e items de votre liste
print(my_list[1:3])
# récupérez le dernier item de votre liste 
print(my_list[-1])
# récupérez toute la liste SAUF le premier item
print(my_list[1:])

# essayez le code suivant:
my_list = [1, 2, 3]
my_double_list = my_list + my_list
print(my_double_list)

# puis essayez le code suivant
try_new_list = my_list
print(try_new_list)

# puis essayez le code suivant:
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# Quel résultat obtenez-vous ? 
# Qu'en déduire sur le fonctionnement de l'opérateur + avec les listes ?
#on peut ajouter deux listes !!

my_list = [1, 2, 3]
my_list2 = [4, 5 ,6]
my_list.append(my_list2) #my_list2 reste sous la forme d'une liste dans my_list
print(my_list)

my_list = [1, 2, 3]
my_list2 = [4, 5 ,6]
my_list.extend(my_list2)
print(my_list)

# testez le code suivant:
my_list = [1, 2 ,3]
del(my_list[-1])
print(my_list)

my_list[-1] = "ZERO!!"
print(my_list)


my_list = [2,6,3,10]
my_list.sort()
print(my_list)

my_list = [2,6,3,10]
my_list = my_list.sort()
print(my_list)

# vous avez une liste de courses:
groceries = ["tomatoes", "carrots", "bananas"]

# finalement, vous souhaitez manger un burger à la place des carottes
# essayez de devenir comment remplacer "carrots" par "burger" 
# indice: utilisez l'indexing 
groceries[1] = "brugers"
print(groceries)