# Alyssa Lukpat
# Oct. 28
# Homework 3, Part 1

# 1 What is the URL to the documentation?
    # The documentation URL is https://pokeapi.co/docs/v2
# 2 What pokemon has the ID of 55?
    # golduck has the ID of 55.
# 3 How tall is that pokemon?
    # golduck's height is 17.
# 4 How many versions of Pokemon games have been released?
    # There are 20 versions of Pokemon.
# 5 Print out the name of every electric-type pokemon.
    # Here are the names:
    # ['pikachu', 'raichu', 'magnemite', 'magneton', 'voltorb', 'electrode', 'electabuzz', 
    # 'jolteon', 'zapdos', 'chinchou', 'lanturn', 'pichu', 'mareep', 'flaaffy', 'ampharos', 
    # 'elekid', 'raikou', 'electrike', 'manectric', 'plusle', 'minun', 'shinx', 'luxio', 
    # 'luxray', 'pachirisu', 'magnezone', 'electivire', 'rotom', 'blitzle', 'zebstrika', 
    # 'emolga', 'joltik', 'galvantula', 'tynamo', 'eelektrik', 'eelektross', 'stunfisk', 
    # 'thundurus-incarnate', 'zekrom', 'helioptile', 'heliolisk', 'dedenne', 'charjabug', 
    # 'vikavolt', 'togedemaru', 'tapu-koko', 'xurkitree', 'zeraora', 'yamper', 'boltund', 
    # 'toxel', 'toxtricity', 'pincurchin', 'morpeko', 'dracozolt', 'arctozolt', 'rotom-heat', 
    # 'rotom-wash', 'rotom-frost', 'rotom-fan', 'rotom-mow', 'thundurus-therian', 
    # 'ampharos-mega', 'manectric-mega', 'pikachu-rock-star', 'pikachu-belle', 'pikachu-pop-star', 
    # 'pikachu-phd', 'pikachu-libre', 'pikachu-cosplay', 'pikachu-original-cap', 'pikachu-hoenn-cap', 
    # 'pikachu-sinnoh-cap', 'pikachu-unova-cap', 'pikachu-kalos-cap', 'pikachu-alola-cap', 
    # 'raichu-alola', 'geodude-alola', 'graveler-alola', 'golem-alola', 'vikavolt-totem', 
    # 'oricorio-pom-pom', 'pikachu-partner-cap', 'togedemaru-totem']
# 6 What are electric-type Pokemon called in the Korean version of the game?
    # In the Korean version of the game, electric-type Pokemon are called 전기.
# 7 Who has a higher speed stat, Eevee or Pikachu?
    # Pikachu is faster than Eevee, with a speed of 90 compared to Eevee's 55.

# --------------------------------------------------------------

import requests

# question two
two_id = 55
two_url = f'https://pokeapi.co/api/v2/pokemon/{two_id}/'
two_response = requests.get(two_url, allow_redirects=True)
two_data = two_response.json()

two_name = (two_data['name'])
print(f'{two_name} has the ID of 55.')
    
# question three
two_height = (two_data['height'])
print(f'{two_name}\'s height is {two_height}.')

# question four
four_url = "https://pokeapi.co/api/v2/version/"
four_response = requests.get(four_url, allow_redirects=True)
four_data = four_response.json()

version_count = 0
for version in four_data['results']:
    version_count = version_count + 1

print(f'There are {version_count} versions of Pokemon.')

# question five
five_url = "https://pokeapi.co/api/v2/type/"
five_response = requests.get(five_url, allow_redirects=True)
five_data = five_response.json()

five_results = five_data['results']

for name in five_results:
    if name['name'] == 'electric':
        five_url_electric = name['url']

five_response_electric = requests.get(five_url_electric, allow_redirects=True)
five_data_electric = five_response_electric.json()

five_names = five_data_electric['pokemon']

five_names_list = []
for na in five_names:
    nested_name = na['pokemon']['name']
    five_names_list.append(nested_name)

print(five_names_list)

# question six - names of electric-type Pokemon in the Korean version 
nested_five_data_electric = five_data_electric['names']

for elec in nested_five_data_electric:
    if elec['language']['name'] == 'ko':
        elec_name_ko = elec['name']
        print(f'In the Korean version of the game, electric-type Pokemon are called {elec_name_ko}.')

# question seven - who has higher speed stat - eevee or pikachu?
seven_url = "https://pokeapi.co/api/v2/pokemon?limit=1000"
seven_response = requests.get(seven_url, allow_redirects=True)
seven_data = seven_response.json()

seven_results = seven_data['results']

for res in seven_results:
    if res['name'] == 'eevee':
        eevee_url = str(res['url'])
        eevee_response = requests.get(eevee_url, allow_redirects=True)
        eevee_data = eevee_response.json()
    if res['name'] == 'pikachu':
        pikachu_url = str(res['url'])
        pikachu_response = requests.get(pikachu_url, allow_redirects=True)
        pikachu_data = pikachu_response.json()

pikachu_stats = pikachu_data['stats']
eevee_stats = eevee_data['stats']

# print(pikachu_stats[0]['stat'])
# print(pikachu_stats[0]['stat']['name'])

pikachu_speed = 0
for sp in pikachu_stats:
    if sp['stat']['name'] == 'speed':
        pikachu_speed = sp['base_stat'] 
print(pikachu_speed)

eevee_speed = 0
for sp in eevee_stats:
    if sp['stat']['name'] == 'speed':
        eevee_speed = sp['base_stat'] 
print(eevee_speed)

if eevee_speed > pikachu_speed:
    print(f'Eevee is faster than Pikachu, with a speed of {eevee_speed} compared to Pikachu\'s {pikachu_speed}.')
else:
    print(f'Pikachu is faster than Eevee, with a speed of {pikachu_speed} compared to Eevee\'s {eevee_speed}.')