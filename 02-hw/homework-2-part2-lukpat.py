# Alyssa Lukpat
# Oct. 28
# Homework 2, Part 2

# Lists

countries = ["Botswana", "Panama", "Egypt", 'Albania', "Taiwan", "Canada", "France"]

tally = 0
for country in countries:
    print(country)
    tally = tally + 1

countries.sort()

print(f'The first item in the list is {countries[0]}.')

reverse_countries = sorted(countries, reverse=True)
print(f'The second-to-last element in the list is {reverse_countries[1]}.')

countries.remove('France')

tally_new = 0
for place in countries:
    print(place.upper())
    tally_new = tally_new + 1



# Dictionaries

tree = {
    'name': 'Takeshi Kaneshiro Tree',
    'species': 'Bischofia javanica',
    'age': 95,
    'location_name': 'Taitung',
    'latitude': 22.7613,
    'longitude': 121.1438
}

TREE_NAME = tree['name']
TREE_AGE = tree['age']
TREE_LOCATION = tree['location_name']
print(f'The {TREE_NAME} is a {TREE_AGE}-year-old tree that is in {TREE_LOCATION}.')

NYC_LATITUDE = 40.7128
NYC_LONGITUDE = -74.0059
TREE_LATITUDE = 22.7613
TREE_LONGITUDE = 121.1438

if TREE_LATITUDE < NYC_LATITUDE:
    print(f'The {TREE_NAME} in {TREE_LOCATION} is south of NYC.')
elif TREE_LATITUDE > NYC_LATITUDE:
    print(f'The {TREE_NAME} in {TREE_LOCATION} is north of NYC.')
else:
    print(f'The {TREE_NAME} in {TREE_LOCATION} is at the same latitude as NYC.')

USER_AGE = int(input("How old are you? "))
AGE_DIFFERENCE = TREE_AGE - USER_AGE
if USER_AGE > TREE_AGE:
    print(f'You are {abs(AGE_DIFFERENCE)} years older than the {TREE_NAME}.')
elif TREE_AGE > USER_AGE:
    print(f'The {TREE_NAME} was {AGE_DIFFERENCE} years old when you were born.')
else:
    print(f'You are the same age as the {TREE_NAME}!')



# Lists of dictionaries

places = [
    {'name': 'Moscow',
    'longitude': 55.7558,
    'latitude': 37.6173
    },
    {'name': 'Tehran',
    'longitude': 35.6892,
    'latitude': 51.3890
    },
    {'name': 'Falkland Islands',
    'longitude': -51.7963,
    'latitude': -59.5236
    },
    {'name': 'Seoul',
    'longitude': 37.5665,
    'latitude': 126.9780
    },
    {'name': 'Santiago',
    'longitude': -33.4489,
    'latitude': -70.6693
    }
]

for place in places:
    PLACE_NAME = place['name']
    print(PLACE_NAME)
    if place['latitude'] > 0:
        print(f'{PLACE_NAME} is above the equator.')
    else:
        print(f'{PLACE_NAME} is below the equator.')
    if PLACE_NAME  == 'Falkland Islands':
        print(f'The Falkland Islands are a biogeographical part of the mild Antarctic zone.')

for pla in places:
    NAME = pla['name']
    if pla['latitude'] > TREE_LATITUDE:
        print(f'{NAME} is north of the {TREE_NAME}.')
    elif TREE_LATITUDE > pla['latitude']:
        print(f'The {TREE_NAME} is north of {NAME}.')

