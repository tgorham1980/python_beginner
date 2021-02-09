def fire_fight(s):
    check = "Fire"
    if check in s:
        fire = s.replace("Fire", "~~")
        return fire
    if check not in s:
        return s
    elif check == "":
        return s
    elif check == None:
        return s
    else:
        pass

print(fire_fight("Water Deck Deck Boat Deck Propeller Water Water"))