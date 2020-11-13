#!/usr/bin/env python
# coding: utf-8

# # Last FM API (Music)
# 
# Spotify's API is dead to us, so we're using Last.fm's - it's still music, just not as nice of an API.
# 
# 1. Create an account at https://www.last.fm/api/
# 2. Create an "application" to get a key: https://www.last.fm/api/account/create
#     - It isn't a real application, it's just your project
#     - Name/description doesn't matter, ignore callback key and callback url
# 3. And save the API key that shows up on the next screen
# 
# You can find documentation at https://www.last.fm/api/
# 
# The domain for the API is `http://ws.audioscrobbler.com`, so all of your endpoints will be connected to that. To test your API key, check the following URL in your browser: `http://ws.audioscrobbler.com/2.0/?method=artist.search&artist=cher&api_key=XXXXXXXXXXXXXXXXXXXX&format=json` (change the `XXXXXX` to be your API key, of course!).
# 
# > Last.fm used to be called **AudioScrobbler**, which is why its URLs don't have "last.fm" in them.
# > While we're asking about URLs, notice that the API endpoints have a lot of `?` and `&` in them - these are key/value pairs, kind of like dictionaries, but for URLs instead of Python.

# # FIRST: SETUP

# ## 1) Import the libraries/packages you might need
# 
# We need a library to read in the data for us! We don't like `urllib2`, so it must be something cooler and better.

import requests


# ## 2) Save your API key
# 
# Write your API key here so you don't forget it - it's the "api key" one, not the "shared secret" one
# 
# # 65297f4af0c2fbc492dff031c75f7c52

# ## 3) The death of an API
# 
# I used to have some code here that allowed you to display images, but _the images don't work any more._ Let this be an important lesson: when you depend on external services, they can die at any time.

# # NOW: YOUR ASSIGNMENT

# ## 1) Search for and print a list of 50 musicians with `lil` in their name, along with the number of listeners they have
# 
# There are a lot of musicians with "Lil" in their name - it used to be all Lil Wayne and Lil Kim, but we live in a new world now!
# 
# - *Tip: Remember, the domain for the API is `http://ws.audioscrobbler.com`*
# - *Tip: Make sure you ask the API for 50 musicians! This involves adding another parameter to the URL - notice they all have a `&` before them. [Read the documentation](http://www.last.fm/api/show/artist.search) to find the parameter's name.* 
# - *Tip: When you are looking at any piece of data - is it a dictionary? Look at the keys! Is it a list? Look at the first element!*
# - *Tip: LOOK AT THE KEYS. and then the other keys and the other keys and the other keys. It's an ugly series of dictionaries!*

search_url = 'http://ws.audioscrobbler.com/2.0/?method=artist.search&artist=lil&api_key=65297f4af0c2fbc492dff031c75f7c52&format=json&limit=50'
search_response = requests.get(search_url, allow_redirects=True)
search_data = search_response.json()

key = '65297f4af0c2fbc492dff031c75f7c52'

artist_search = (search_data['results']['artistmatches']['artist'])

artist_list = []
for artist in artist_search:
    artist_name = artist['name']
    artist_listeners = artist['listeners']
    output = f'{artist_name} has {artist_listeners} listeners.'
    artist_list.append(output)

for sentence in artist_list:
    print(sentence)

# ## 2) How many listeners does your list have in total?
# 
# The answer should be roughly **15,000,000**. If it's lower, make sure you have 50 artists instead of 30 artists.
# 
# - *Tip: What's the data type of the `listeners` count? It's going to cause a problem!*
# - *Tip: If you were crazy you could use sum and a list comprehension. But you really don't have to!*

listener_count = 0

for listen in artist_search:
    artist_listeners = int(artist['listeners'])
    listener_count = listener_count + artist_listeners

print(f'There are {listener_count} total listeners.')


# ## 3) Show each artist's name and the URL to the extra-large image
# 
# The images don't work any more, but we'll print their URLs out anyway.

# Each artist **has a list of images of different sizes**. We're interested in the second-to-last one, where `size` is `extralarge`. Print their name and use `display_image` to display their extra-large image.
# 
# - *Tip: The URL should look like this: `https://lastfm-img2.akamaized.net/i/u/300x300/0fc7d7a1812dc79e9925d80382cde594.png`*
# - *Tip: You can always assume it's the second to the last, or assume it's `extralarge`, or whatever you want to do to find it.*
# - *Tip: Make sure the URL is correct before you try to display it.*

for artist in artist_search:
    artist_name = artist['name']
    print(artist_name)
    for photo in artist['image']:
        if photo['size'] == 'extralarge':
            print(photo['#text'])
    print("-----")


# ## 4) Find Lil Jon's `mbid` (or anyone else's!).
# 
# Oftentimes in an API, you can do a few things: you can **search** for items, and you can **see more information** about items. To find more information about the item, you need to use their **unique id**. In this dataset, it's called an `mbid` (MusicBrainz, I think - another company associated with last.fm!).
# 
# Go through the artists and print their **name and mbid**. Find Lil Jon's `mbid`. I *wanted* Lil Uzi Vert's, but for some reason it isn't there. Then I wanted us to look at Lily Allen's, but I just couldn't bring myself to do that. If you'd rather do someone else, go for it.

for mbid_finder in artist_search:
    artist_mbid = mbid_finder['mbid']
    name_artist = mbid_finder['name']
    if name_artist == 'Lil Jon':
        print(f'{name_artist}\'s mbid is {artist_mbid}.')


# ## 5) Find the artist's name and bio using their `mbid`.
# 
# It can either be Lil Jon or whoever you selected above.
# 
# If you look at the [last.fm documentation](http://www.last.fm/api/show/artist.getInfo), you can see how to use the artist's `mbid` to find more information about them. Print **every tag associated with your artist**.
# 
# - *Tip: It's a new request to the API*
# - *Tip: Use the `mbid`, and make sure you delete the `&name=Cher` from the sample endpoint*
# - *Tip: If you use `print` for the bio it looks a little nicer than it would otherwise*

mbid_url = 'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&mbid=a95384b1-6aec-468c-ae0d-8c6daf87c4c2&api_key=65297f4af0c2fbc492dff031c75f7c52&format=json'
mbid_response = requests.get(mbid_url, allow_redirects=True)
mbid_data = mbid_response.json()

artist_name = mbid_data['artist']['name']
artist_bio = mbid_data['artist']['bio']['content']

print(f'Here is {artist_name}\'s bio:\n{artist_bio}')


# ## 6) Print every tag of that artist

mbid_data_tag = mbid_data['artist']['tags']['tag']

for every_tag in mbid_data_tag:
    mbid_name = every_tag['name']
    mbid_link = every_tag['url']
    print(f'Name: {mbid_name}, link: {mbid_link}')


# # GETTING A LITTLE CRAZY
# 
# So you know your original list of musicians? I want to get tag data for ALL OF THEM. How are we going to do that?
# 
# ## 7) Find the mbids (again)
# 
# If we have a musician with an mbid of `AAA-AAA-AAA`, we get their info from a url like `http://ws.audioscrobbler.com/blahblah/?api_key=12345&mbid=AAA-AAA-AAA`.
# 
# |artist|url|
# |---|---|
# |`AAA-AAA-AAA`|`http://ws.audioscrobbler.com/blahblah/?api_key=12345&mbid=AAA-AAA-AAA`|
# |`BBB-BBB-BBB`|`http://ws.audioscrobbler.com/blahblah/?api_key=12345&mbid=BBB-BBB-BBB`|
# |`CCC-CCC-CCC`|`http://ws.audioscrobbler.com/blahblah/?api_key=12345&mbid=CCC-CCC-CCC`|
# 
# I guess we should start trying to get a list of all of the mbids.
# 
# **Loop through your artists, and print out the `mbid` for each artist**
# 
# - *Tip: You probably need to request your artist search result data again, because you probably saved over `data` with your other API request. Maybe call it `artist_data` this time?*
# - *Tip: If the artist does NOT have an `mbid`, don't print it.*

mbid_list = []
for artist in artist_search:
    artist_name = artist['name']
    artist_mbid = artist['mbid']
    if artist_mbid != '':
        mbid_list.append([artist_name, artist_mbid])

for person in mbid_list:
    name_artist = person[0]
    mbid_artist = person[1]
    print(f'{mbid_artist}')

# ## 8) Saving those mbids
# 
# For those `mbid` values, instead of printing them out, save them to a new list of just mbid values. Call this list `mbids`.
# 
# - *Tip: Use `.append` to add a single element onto a list*

mbids = []
for artist in artist_search:
    artist_name = artist['name']
    artist_mbid = artist['mbid']
    if artist_mbid != '':
        mbids.append(artist_mbid)
        
print(mbids)


# ## 9) Printing our API urls
# 
# To get tag data for each artist, you need to use those `mbid` values to access their artist page on the API. Loop through the mbids, displying the URL you'll need to access.
# 
# - *Tip: You don't want to use a comma when printing, because commas add spaces into your text and URLs can't have that*
# - *Tip: Make sure your URL has `artist.getinfo` in it - if not, you're using the wrong endpoint.*

new_mbid_list = []
for mbid in mbids:
    new_mbid_list.append(f'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&mbid={mbid}&api_key=65297f4af0c2fbc492dff031c75f7c52&format=json')
    print(f'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&mbid={mbid}&api_key=65297f4af0c2fbc492dff031c75f7c52&format=json')


# ## OKAY HERE IS A LITTLE INFORMATION: Using our API urls
# 
# This time instead of just *displaying* the URL, we're going to *request and process it*. **But first I'm going to teach you something.**
# 
# When you're dealing with an API, you don't want to make a million requests, have bad code, and then need to do those million requests again. It's usually best to test your code with a few of the results first.
# 
# So, if we have a list of numbers like this:

numbers = [4, 5, 6, 7]
numbers


# You can actually say to Python, **give me the first two**, and it will only give you the first two.

numbers[:2]


# The is **very convenient** with loopng with APIs, because instead of trying to use all FIFTY artists, you can just say "hey, please try this out with 2 of them" and you don't waste time.

# ## 10) Using the first three `mbids`, request the API urls and print the artist's name.
# 
# You built the URLs in the last question, now it's time to use them! Use `requests` etc to grab the URL and get out the artist's name.
# 
# - *Tip: The code is the same as last time you got an artist's name from their info page, it's just going to be inside of a loop*
# - *Tip: USE `PRINT` TO SEE WHAT YOU ARE LOOKING AT!!!!!*

count = 0
for mbid in new_mbid_list:
    if count < 3:
        check_mbid_url = new_mbid_list[count]
        check_mbid_response = requests.get(check_mbid_url, allow_redirects=True)
        check_mbid_data = check_mbid_response.json()
        print(check_mbid_data['artist']['name'])
    count = count + 1


# ## 11) Using the first three `mbids`, request the API urls and print the artist's name and their tags
# 
# - *Tip: The code is the same as last time you got an artist's name from their info page, it's just going to be inside of a loop*
# - *Tip: It's a for loop in a for loop!*

count = 0
for mbid in new_mbid_list:
    if count < 3:
        check_mbid_url = new_mbid_list[count]
        check_mbid_response = requests.get(check_mbid_url, allow_redirects=True)
        check_mbid_data = check_mbid_response.json()
        print(check_mbid_data['artist']['name'])
        for get_tag in check_mbid_data['artist']['tags']['tag']:
            mbid_name = get_tag['name']
            mbid_link = get_tag['url']
            print(f'Name: {mbid_name}, link: {mbid_link}')
    count = count + 1


# ## 12) Using the first ten mbids, print the artist's name and whether they're a rapper
# 
# Only print their name ONCE and only print whether they are hip hop or not ONCE.
# 
# - *Tip: Rap tags include hip hop, swag, crunk, rap, dirty south, and probably a bunch of other stuff! You can include as many categories as you'd like.*
# - *Tip: You can use `2 in [1, 2, 3]` to find out if `2` is in the list of `[1, 2, 3]`.*
# - *Tip: Every time you look at a new artist, you can say they are NOT a rapper. And once you find out one of their tags is hip hop or rap, then you can note that they're a rapper. Then once you're done looking at their tags, then you can say HEY this is a rapper, or HEY this is not a rapper.*

count = 0
for mbid in new_mbid_list:
    is_rap = False
    if count < 10:
        check_mbid_url = new_mbid_list[count]
        check_mbid_response = requests.get(check_mbid_url, allow_redirects=True)
        check_mbid_data = check_mbid_response.json()
        print(check_mbid_data['artist']['name'])
        for get_tag in check_mbid_data['artist']['tags']['tag']:
            mbid_name = get_tag['name']
            if 'rap' or 'hip hop' in mbid_name:
                is_rap = True
        if is_rap == True:
            print("Yes hip hop")
        else:
            print("No hip hop")
        print("-----")
    count = count + 1

# ## 13) What percent of "lil" results are rappers?

rapper_count = 0

for human in new_mbid_list:
    is_rap = False
    actual_mbid_url = human
    actual_mbid_response = requests.get(actual_mbid_url, allow_redirects=True)
    actual_mbid_data = actual_mbid_response.json()
    for tag_check in check_mbid_data['artist']['tags']['tag']:
        mbid_name = tag_check['name']
        if 'rap' or 'hip hop' in mbid_name:
            is_rap = True
    if is_rap == True:
        rapper_count = rapper_count + 1

total_lil = len(new_mbid_list)
percent_rap = (round(rapper_count/total_lil) * 100)

print(f'Of the \'lil\' results, {percent_rap}% are rappers.')


# ## 14) Seriously you are all-powerful now.
# wow

