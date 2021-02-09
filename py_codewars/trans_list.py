list1 = ["BLUE", "FOO", "GREEN"]
list2 = list(list1[0])
list3 = list(list1[1])
list4 = list(list1[2])
phone_number = input("Enter a phone number? ")
#phone_trans = (translate(phone_number.upper()))
#list5 = list2 + list3 + list4

def translate1(phone_number):
    translation = ""
    for letter in phone_number:
        if letter in "ABC":
            translation = translation + "2"
        elif letter in "DEF":
            translation = translation + "3"
        elif letter in "GHI":
            translation = translation + "4"
        elif letter in "JKL":
            translation = translation + "5"
        elif letter in "MNO":
            translation = translation + "6"
        elif letter in "PQRS":
            translation = translation + "7"
        elif letter in "TUV":
            translation = translation + "8"
        elif letter in "WXYZ":
            translation = translation + "9"
        else:
            translation = translation + letter
    return translation


def translate2(list2):
    translation2 = ""
    for letter in list2:
        if letter in "ABC":
            translation2 = translation2 + "2"
        elif letter in "DEF":
            translation2 = translation2 + "3"
        elif letter in "GHI":
            translation2 = translation2 + "4"
        elif letter in "JKL":
            translation2 = translation2 + "5"
        elif letter in "MNO":
            translation2 = translation2 + "6"
        elif letter in "PQRS":
            translation2 = translation2 + "7"
        elif letter in "TUV":
            translation2 = translation2 + "8"
        elif letter in "WXYZ":
            translation2 = translation2 + "9"
        else:
            translation2 = translation2 + letter
            print("Nothing to translate!")
    return translation2

print(list3)
print(translate2(list2))
print(translate2(list3))
print(translate2(list4))
phone_trans = (translate1(phone_number.upper()))
print(phone_trans)

