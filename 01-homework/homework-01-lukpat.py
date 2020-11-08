## Alyssa Lukpat
## Oct. 26
## Homework 1

## variables and prompt
year = int(input("What year were you born? "))
age = 2020 - year

if year > 2020:
    year = input("You can\'t be born in the future! What year were you actually born?")

## print age
print(f'1. You\'re approximately {age} years old.')

## print lifetime heart beats
## assuming a person's heart beats about 60 times per minute ...
human_heart_rate = age * 60 * 60 * 24 * 365
if human_heart_rate >= 1000000000:
    print(f'2. Your heart has beaten about {round(human_heart_rate/1000000000, 1)} billion times since you were born.')
else:
    print(f'2. Your heart has beaten about {round(human_heart_rate/1000000)} million times since you were born.')
                 
## print whale heart beats
## assuming a blue whale's heart beats about 8 times per minute ...
whale_heart_rate = age * 8 * 60 * 24 * 365
if whale_heart_rate >= 1000000000:
    print(f'3. Since {year}, a blue whale\'s heart has beaten about {round(whale_heart_rate/1000000000, 1)} billion times.')
else:
    print(f'3. Since {year}, a blue whale\'s heart has beaten about {round(whale_heart_rate/1000000)} million times.')

## print rabbit heart beats
## assuming a rabbit's heart beats about 140 times per minute ...
rabbit_heart_rate = age * 140 * 60 * 24 * 365
if rabbit_heart_rate >= 1000000000:
    print(f'4 and 5. Since {year}, a rabbit\'s heart has beaten about {round(rabbit_heart_rate/1000000000, 1)} billion times.')
else:
    print(f'4 and 5. Since {year}, a rabbit\'s heart has had about {round(rabbit_heart_rate/1000000)} million times.')


## print Venus years
## assuming one Venus year = 0.6152 Earth years
Venus_age = 0.6152 * age
print(f'6. In Venus years, you\'re about {round(Venus_age)} years old.')

## print Neptune years
## assuming one Venus year = 165 Earth years
Neptune_age = 165 * age
print(f'7. In Neptune years, you\'re about {round(Neptune_age)} years old.')

## print their age compared to mine
older_age_difference = age - 22
younger_age_difference = 22 - age 
if age == 22:
    print(f'8 and 9. We\'re the same age!')
elif age > 22:
    if older_age_difference == 1:
        print(f'8 and 9. You\'re older than me by {older_age_difference} year.')
    else:
        print(f'8 and 9. You\'re older than me by {older_age_difference} years.')
else:
    if younger_age_difference == 1:
        print(f'8 and 9. You\'re younger than me by {younger_age_difference} year.')
    else:
        print(f'8 and 9. You\'re older than me by {younger_age_difference} years.')


## even or odd year?
if year % 2 == 0:
    print(f'10. You were born in an even year.')
else:
    print(f'10. You were born in an odd year.')

## Democratic president tally
## Hi, I have a question! Is there a more efficient way to do this question and the next one? Like with a list somehow?
president_tally = 0
if year >= 1960:
    ## if 1960 <= year <= 1963: more efficient with only one year!
    if year <= 1963:
        president_tally = 5
    elif year <= 1969:
        president_tally = 4
    elif 1970 <= year <= 1981:
        president_tally = 3
    elif 1982 <= year <= 2001:
        president_tally = 2
    elif 2002 <= year <= 2020:
        president_tally = 1

if president_tally > 1:
    print(f'11. Since you were born, there have been {president_tally} Democratic presidents.')
elif president_tally == 1:
    print(f'11. Since you were born, there has been 1 Democratic president.')

## sitting president at birth
president_name = ""
if year >= 1960:   
    if year == 1960:
        president_name = "Dwight D. Eisenhower"
    elif 1961 <= year <= 1963:
        president_name = "John F. Kennedy"
    elif 1964 <= year <= 1968:
        president_name = "Lyndon B. Johnson"
    elif 1969 <= year <= 1974:
        president_name = "Richard Nixon"
    elif 1975 <= year <= 1976:
        president_name = "Gerald Ford"   
    elif 1977 <= year <= 1980:
        president_name = "Jimmy Carter"
    elif 1981 <= year <= 1988:
        president_name = "Ronald Reagan"
    elif 1989 <= year <= 1992:
        president_name = "George H. W. Bush"
    elif 1993 <= year <= 2000:
        president_name = "Bill Clinton"
    elif 2001 <= year <= 2008:
        president_name = "George W. Bush"
    elif 2009 <= year <= 2016:
        president_name = "Barack Obama"
    elif 2017 <= year <= 2020:
        president_name = "Donald Trump"
    print(f'12. When you were born, President {president_name} was in office.')