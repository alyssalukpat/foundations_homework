#
# "It doesn't work"
#
# 1. The error message
# 2. The code around where the error is happening
# 3. Expected output
# 4. Actual output
# 5. What you've tried already

# Error
print("Hello world, so full of errors")

# Error
num = 4.55
print(round(num) * int(5) + 3)

# Error
name = "Roberta"
degrees = 14
print("Hello, my name is", name, "and it is", degrees, "degrees out today")

# Error
name = "Smushface"
print("I have a cat named", name)

# Error
age = 4
if age < 18:
    print("You aren't old enough to vote") 

# Error
print("One two three four")
print("Five six seven eight")
print("Nine ten eleven twelve")

# Error
pies = 9
print("You have eaten " + str(pies) + " pies today")

# Error
current_year = 2013
travel = "future"
cars = True
animal_type = "lions"
if current_year > 2017:
    print("It's the", travel, "!")

# Error
# I'm assuming this person meant to do 4 + 4, not concatenate 4 and 4
print(int(4 + 4))

# Error
year = 2017
if year >= 1776:
    print("The United States exists")
elif year >= 1607:
    print("The American colonies existed")
else:
    print("America was just a dream")