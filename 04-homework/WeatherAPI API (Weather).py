#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*


import requests


# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* 
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*


city = 'Sunnyvale'
url =  f'http://api.weatherapi.com/v1/current.json?key=f5b146a0ca05450aa7711748200311&q={city}'

response = requests.get(url, allow_redirects=True)

data = response.json()


# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*


wind_speed = data['current']["wind_mph"]
print(f'The current wind speed in {city} is {wind_speed} miles per hour.')

current_temp = data['current']['temp_f']
feels_like = data['current']['feelslike_f']
difference = current_temp - feels_like

if difference > 0:
    print(f'It feels {difference} degrees colder in {city}.')
elif difference < 0:
    print(f'It feels {difference} degrees warmer in {city}.')
else:
    print(f'The weather in {city} feels like the current temperature, {current_temp} degrees.')


# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible on next Thursday?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

moon_url = "http://api.weatherapi.com/v1/forecast.json?key=f5b146a0ca05450aa7711748200311&q=Sunnyvale&days=10"
moon_response = requests.get(moon_url, allow_redirects=True)
moon_data = moon_response.json()
# I requested 10 days on Thursday, Nov. 5, but because we're on a free plan, WeatherAPI only shows forecasts through Saturday.
# Since I can't view next Thursday's forecast info, here if the info for Saturday, Nov. 7:

forecast_day = moon_data['forecast']['forecastday']

for day in forecast_day:
    if day['date'] == '2020-11-07':
        the_date = day['date']
        illumination = day['astro']['moon_illumination']
        phase = day['astro']['moon_phase']

print(f'On {the_date} in {city}, the moon\'s illumination will be {illumination}% and its phase will be {phase}.')


# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

my_url =  f'http://api.weatherapi.com/v1/forecast.json?key=f5b146a0ca05450aa7711748200311&q={city}'
my_response = requests.get(my_url, allow_redirects=True)
my_data = my_response.json()

high_temp = my_data['forecast']['forecastday'][0]['day']['maxtemp_f']
low_temp = my_data['forecast']['forecastday'][0]['day']['mintemp_f']
        
temp_difference = round(high_temp - low_temp)
print(f'The difference between today\'s high and low temperature in {city} is about {temp_difference} degrees Fahrenheit.')


# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# I would rename every instance of the url, response, and data variables with unique names.
# For example, moon_url, moon_response, and moon_data.


# ## 5) Go through the daily forecasts, printing out the next week's worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# forecast_url is the same link as my_url, but I added the next few days of forecasts.
forecast_url = 'http://api.weatherapi.com/v1/forecast.json?key=f5b146a0ca05450aa7711748200311&q={city}&days=7'
forecast_response = requests.get(forecast_url, allow_redirects=True) 
forecast_data = forecast_response.json()

for forecast in forecast_data['forecast']['forecastday']:
    forecast_date = forecast['date']
    high_temperature = forecast['day']['maxtemp_f']
    if high_temperature >= 80:
        print(f'On {forecast_date} in {city}, the high temperature will be {high_temperature} degrees. That\'s hot!')
    elif high_temperature >= 60:
        print(f'On {forecast_date} in {city}, the high temperature will be {high_temperature} degrees. That\'s warm!')
    else:
        print(f'On {forecast_date} in {city}, the high temperature will be {high_temperature} degrees. That\'s cold!')
    print("-----")


# # 6) What will be the hottest day in the next week? What is the high temperature on that day?
hottest_temp = 0

for forecast in forecast_data['forecast']['forecastday']:
    high_temperature = forecast['day']['maxtemp_f']
    if high_temperature > hottest_temp:
        hottest_temp = high_temperature
        hottest_day = forecast['date']
        
print(f'The hottest day in {city} the next few days will be {hottest_day}, when the temperature hits {hottest_temp} degrees.')


# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

miami_city = 'Miami'
miami_url =  f'http://api.weatherapi.com/v1/forecast.json?key=f5b146a0ca05450aa7711748200311&q={miami_city}&days=2'
miami_response = requests.get(miami_url, allow_redirects=True)
miami_data = miami_response.json()

from datetime import datetime
time_now = str(datetime.now().time())
now = int(time_now[0:2]) + 1

forecaster = miami_data['forecast']['forecastday'][0]['hour']
forecaster_two = miami_data['forecast']['forecastday'][1]['hour']
count = now
current_timestamp = miami_data['forecast']['forecastday'][0]['hour'][count]['time']


# Run all the code above for this problem before running the two loops below, because, otherwise, this code sometimes won't return 24 hourly forecasts 
# Sometimes I got shorter results in Jupyter when I just ran the box with the two loops below
for forecast in forecaster:
    if forecast['time'] == current_timestamp:
        forecast_time = forecast['time']
        hourly_temp = forecast['temp_f']
        cloud_cover = forecast['cloud']
        if cloud_cover > 50:
            print(f'At {forecast_time} in {miami_city}, it will be {hourly_temp} degrees and cloudy.')
        else:
            print(f'At {forecast_time} in {miami_city}, it will be {hourly_temp} degrees.')
        if count < 23:
            count = count + 1
            current_timestamp = miami_data['forecast']['forecastday'][0]['hour'][count]['time']

count = 0
for forecast in forecaster_two:
    if count < now:
        forecast_time = forecast['time']
        hourly_temp = forecast['temp_f']
        cloud_cover = forecast['cloud']
        if cloud_cover > 50:
            print(f'At {forecast_time} in {miami_city}, it will be {hourly_temp} degrees and cloudy.')
        else:
            print(f'At {forecast_time} in {miami_city}, it will be {hourly_temp} degrees.')
    count = count + 1


# # 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

temp_counter = 0
reg_counter = 0

for forecast in forecaster:
    if forecast['time'] == current_timestamp:
        hourly_temp = forecast['temp_f']
        if hourly_temp > 85:
            temp_counter = temp_counter + 1
        if count < 23:
            count = count + 1
            current_timestamp = miami_data['forecast']['forecastday'][0]['hour'][count]['time']
    reg_counter = reg_counter + 1

count = 0
for forecast in forecaster_two:
    if count < now:
        hourly_temp = forecast['temp_f']
        if hourly_temp > 85:
            temp_counter = temp_counter + 1
    count = count + 1
    reg_counter = reg_counter + 1

hot_temp = round(temp_counter/reg_counter)
print(f'For the next 24 hours in Miami, it will be above 85 degrees about {hot_temp}% of the time.')


# ## 9) What was the temperature in Central Park on Christmas Day, 2015? How about 2012? 2007? How far back does the API allow you to go?
# 
# - *Tip: You'll need to use latitude/longitude. You can ask Google, it knows*
# - *Tip: Remember when latitude/longitude might use negative numbers*

# Hi! I can't get any historical temperature data because of our free plan. Here's the message I got:
# {"error":{"code":1008,"message":"API key is limited to get history data. Please check our pricing page and upgrade to higher plan."}}

# If we had a paid plan, here's the link I would have used:
# http://api.weatherapi.com/v1/history.json?key=f5b146a0ca05450aa7711748200311&dt=2020-10-10&q=40.7812,-73.9665

# In other words, the free API does not let us go far back at all!
# According to the documentation, the API will only let us go as far back as Jan. 1, 2015.