rivers = {
    'nile': 'egypt',
    'fraser': 'canada',
    'amazon': ' ecuador, colombia, venezuela ,bolivia ,brazil',#Nearly 60% of the rainforest is in Brazil, while the rest is shared among eight other countries
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())