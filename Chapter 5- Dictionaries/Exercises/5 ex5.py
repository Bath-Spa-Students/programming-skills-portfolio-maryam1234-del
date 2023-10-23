# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'frog',
    'name': 'marci',
    'owner': 'sakina',
    'weight': 50,
    'eats': 'flies',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'lara',
    'owner': 'andy',
    'weight': 4,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'jacky',
    'owner': 'jhonny',
    'weight': 40,
    'eats': 'shoes',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))