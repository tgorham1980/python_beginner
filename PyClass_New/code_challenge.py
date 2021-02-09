"""
Left Side
 w - 4
 p - 3
 b - 2
 s - 1
Right Side
m - 4
 q - 3
 d - 2
 z - 1
 """

start = input("Let the fight begin! Enter your string: ")
print(start + " accepted, the battle will be commencing soon!")

#translate input string into scored numbers only, nonscoring letters ignored
def translate2(letters):
    translation = ""
    for letter in letters:
        if letter == "w":
            translation = translation + "4"
        elif letter == "p":
            translation = translation + "3"
        elif letter in "b":
            translation = translation + "2"
        elif letter in "s":
            translation = translation + "1"
        else:
            translation = translation
    return translation


string_trans = (translate2(start.lower()))
sumz = int(string_trans)
print(sumz)

#sum of each scored number previously translated
def scorez(sumz):
    result = 0
    for i in range(len(str(sumz))):
        result = result + int(str(sumz)[i:i + 1])
        result2 = str(result)
        print(result2)


scorez(sumz)
  








