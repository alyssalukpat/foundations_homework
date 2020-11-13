# Alyssa Lukpat
# Oct. 28
# Homework 3, Part 2

# 1 What is the URL to the documentation?
    # The documentation URL is https://www.weatherapi.com/docs/
# 2 Make a request for the current weather where you are born, or somewhere you've lived.
    # Here's the weather in Sunnyvale, Calif.:
    # {'location': {'name': 'Sunnyvale', 'region': 'California', 'country': 'United States of America', 
    # 'lat': 37.37, 'lon': -122.04, 'tz_id': 'America/Los_Angeles', 'localtime_epoch': 1604370079, 
    # 'localtime': '2020-11-02 18:21'}, 'current': {'last_updated_epoch': 1604328211, 
    # 'last_updated': '2020-11-02 06:43', 'temp_c': 29.2, 'temp_f': 84.6, 'is_day': 1, 
    # 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 
    # 'wind_mph': 3.8, 'wind_kph': 6.1, 'wind_degree': 325, 'wind_dir': 'NW', 'pressure_mb': 1016.0, 'pressure_in': 30.5, 
    # 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 18, 'cloud': 3, 'feelslike_c': 27.2, 'feelslike_f': 81.0, 
    # 'vis_km': 10.0, 'vis_miles': 6.0, 'uv': 7.0, 'gust_mph': 4.5, 'gust_kph': 7.2}}
# 3 Print out the country this location is in.
    # Sunnyvale is in this country: United States of America.
# 4 Print out the difference between the current temperature and how warm it feels. Use "It feels ___ degrees colder" or "It feels ___ degrees warmer," not negative numbers.
    # It feels 3.60 degrees colder in Sunnyvale.
# 5 What's the current temperature at Heathrow International Airport? Use the airport's IATA code to search.
    # The current temperature at Heathrow Airport is 47.3 degrees Fahrenheit.
# 6 What URL would I use to request a 5-day forecast at Heathrow?
    # http://api.weatherapi.com/v1/forecast.json?key=f5b146a0ca05450aa7711748200311&q=LHR&days=3
    # (This is for a three-day forecast, not five, because we're on a free plan.)
# 7 Print the date of each of the 5 days you're getting a forecast for.
    # 2020-11-03, 2020-11-04, 2020-11-05
# 8 Print the maximum temperature of each of the days.
    # The maximum temperature on 2020-11-03 is 49.6 degrees Fahrenheit.
    # The maximum temperature on 2020-11-04 is 55.6 degrees Fahrenheit.
    # The maximum temperature on 2020-11-05 is 51.6 degrees Fahrenheit.
# 9 Print the day with the highest maximum temperature.
    # 2020-11-04 will have the highest maximum temperature: 55.6 degrees.

import requests

# question two
my_city = 'Sunnyvale'
my_key = 'f5b146a0ca05450aa7711748200311'
my_url = f'http://api.weatherapi.com/v1/current.json?key={my_key}&q={my_city}'
my_response = requests.get(my_url, allow_redirects=True)
my_data = my_response.json()

print(my_data)

# question three
my_data_location = my_data['location']['country']
print(f'{my_city} is in this country: {my_data_location}.')

# question four
current_temp = my_data['current']['temp_f']
feels_like_temp = my_data['current']['feelslike_f']

temp_diff = abs(current_temp - feels_like_temp)
if current_temp > feels_like_temp:
    print(f'It feels {temp_diff:.2f} degrees colder in Sunnyvale.')
else:
    print(f'It feels {temp_diff:.2f} degrees warmer in Sunnyvale.')

# question five - current temp at Heathrow
heathrow_iata = 'LHR'
heathrow_url = f'http://api.weatherapi.com/v1/current.json?key={my_key}&q={heathrow_iata}'
heathrow_response = requests.get(heathrow_url, allow_redirects=True)
heathrow_data = heathrow_response.json()

heathrow_current_temp = heathrow_data['current']['temp_f']
print(f'The current temperature at Heathrow Airport is {heathrow_current_temp} degrees Fahrenheit.')

# question seven - print the date of each day you're getting a forecast for
heathrow_forecast_url = f'http://api.weatherapi.com/v1/forecast.json?key={my_key}&q={heathrow_iata}&days=3'
heathrow_forecast_response = requests.get(heathrow_forecast_url, allow_redirects=True)
heathrow_forecast_data = heathrow_forecast_response.json()

forecast_day = heathrow_forecast_data['forecast']['forecastday']

for day in forecast_day:
    print("-----")
    print(day['date'])
print("-----")

# question eight
for the_day in forecast_day:
    date_I_want = the_day['date']
    max_temp = the_day['day']['maxtemp_f']
    print(f'The maximum temperature on {date_I_want} is {max_temp} degrees Fahrenheit.')

# question nine
highest_max = 0

for a_day in forecast_day:
    get_max = a_day['day']['maxtemp_f']
    if get_max > highest_max:
        highest_max = get_max
        max_day = a_day['date']
print(f'{max_day} will have the highest maximum temperature: {highest_max} degrees.')