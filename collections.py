
names = []


def is_containing_numbers(string_to_validate: str):
    """for c in string_to_validate:
        if c.isdigit():
            return True
        return False"""
    return any([c.isdigit() for c in string_to_validate])


def is_element_in_list(element, list_to_check):
    return any([element.casefold() for element in list_to_check])


while True:
    person_name = input("Please enter the person name: ")
    if person_name == "":
        print("The name is empty")
        break
    elif is_containing_numbers(person_name):
        print("This name is not valid, it contains numbers")
    else:
        names.append(person_name)
print(names)
if is_element_in_list("PERCIVAL", names):
    print(f"{names[0]} is here")
else:
    print(f"{names[0]} is not here")

# ------------------- LIST COMPREHENSIONS -------------------


names = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]
# Ajoute longueur de nom pour chaque nom dans noms si longueur > 10
names_length = [len(name) for name in names if len(name) < 10]
print(names_length)

# Ajoute nom pour chaque nom dans noms si "e" est contenu dans nom
names_containing_e = [name for name in names if "e" in name]
print(names_containing_e)

# Ajoute longueur du nom si longueur du nom < 10 sinon ajoute 0 pour chaque nom dans noms
names_length = [len(name) if len(name) < 10 else 0 for name in names]
print(names_length)

# Ajoute i pour i dans l'intervalle 0-4 si i est pair
a = [i for i in range(5) if i % 2 == 0]
print(a)

b = [(i, True if i % 2 == 0 else False) for i in range(11)]
print(b)

# ------------------- Any / All -------------------

# S'utilisent sur des collections
# Any renvoie True si AU MOINS UN element est True, sinon renvoie False
# All renvoie True si TOUS les elements sont True, sinon renvoie False

a = [True, True, False, True, False]
print(any(a))
print(all(a))

# Renvoie True si nom possede "z" sinon renvoie False pour chaque nom dans noms
is_names_with_a_z = any([True if "z" in name.casefold() else False for name in names])
if is_names_with_a_z:
    print("Found!")
else:
    print("Not found")