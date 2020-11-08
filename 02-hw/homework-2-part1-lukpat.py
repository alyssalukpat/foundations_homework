# Alyssa Lukpat
# Oct. 28
# Homework 2, Part 1

# Lists

my_list = [22, 90, 0, -10, 3, 22, 48]
print(f'There are {len(my_list)} elements in this list.')
print(f'The fourth element of this list is {my_list[3]}.')
print(f'The sum of the second and fourth elements in this list is {int(my_list[1] + my_list[3])}.')

my_list_sorted = sorted(my_list, reverse=True)
print(f'The second largest value in this list is {my_list_sorted[1]}.')

FIRST_MY_LIST = next(reversed(my_list))
print(f'The last element in the original unsorted list is {FIRST_MY_LIST}.')

HALF_SUM_MY_LIST = sum(my_list)/2
print(f'The sum of the elements in this list is {HALF_SUM_MY_LIST}.')

MEAN_MY_LIST = round(sum(my_list) / len(my_list))
median_calculation = round(len(my_list)/2)
MEDIAN_MY_LIST = my_list[median_calculation - 1]

if MEAN_MY_LIST > MEDIAN_MY_LIST:
    print(f'The mean of this list, {MEAN_MY_LIST}, is higher than the median, {MEDIAN_MY_LIST}.')
elif MEDIAN_MY_LIST > MEAN_MY_LIST:
    print(f'The media of this list, {MEDIAN_MY_LIST}, is higher than the mean, {MEAN_MY_LIST}.')
else:
    print(f'The mean and median of this list are the same value: {MEAN_MY_LIST}.')



# Dictionaries

movie = {
    'title': 'Frozen',
    'year': 2013,
    'director': 'Jennifer Lee'
}

movie['budget'] = 150000000
movie['revenue'] = 1280000000
difference = movie['revenue'] - movie['budget']
print(f'The difference between the movie revenue and budget was ${difference}.')

if movie['budget'] > movie['revenue']:
    print(f'That was a bad investment.')
elif movie['revenue'] > (movie['budget'] * 5):
    print(f'That was a great investment.')
else:
    print(f'That was an okay investment.')


NYC_pop = {
    'Manhattan': 1.6,
    'Brooklyn': 2.6,
    'Bronx': 1.4,
    'Queens': 2.3,
    'Staten Island': 0.47
}

BROOKLYN_POP = NYC_pop['Brooklyn']
print(f'The population of Brooklyn is {BROOKLYN_POP} million.')

COMBINED_POP = NYC_pop['Manhattan'] + NYC_pop['Brooklyn'] + NYC_pop['Bronx'] + NYC_pop['Queens'] + NYC_pop['Staten Island']
print(f'The combined population of all five boroughs is {COMBINED_POP} million.')

MANHATTAN_PERCENTAGE = round((NYC_pop['Manhattan'] / COMBINED_POP) * 100, 2)
print(f'The percentage of New Yorkers living in Manhattan is about {MANHATTAN_PERCENTAGE}%.')
