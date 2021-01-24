"""I wake up
if I'm hungry
    I eat breakfast

I leave my house
if it's cloudy
    I bring an umbrella
otherwise
    I bring sunglasses

Im at a restaurant
If I want meat
    I order a steak
otherwise if I want pasta
    I order spaghetti and meatballs
otherwise
    I order a salad"""

is_male = True
is_tall = True

#EXAMPLE 1
if is_male and is_tall:
    print("You are a male and tall")

else:
    print("You are not a male")

#EXAMPLE 2
if is_male or is_tall:
    print("You are tall or a male ")

else:
    print("You are not a male nor tall")

#EXMAPLE 3
is_male = True
is_tall = True

#EXAMPLE 1
if is_male and is_tall:
    print("You are a male and tall")

else:
    print("You are not a male")

#EXAMPLE 2
if is_male or is_tall:
    print("You are tall or a male ")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall
    print("You are not a male but are tall")
else:
    print("You are not a male nor tall")