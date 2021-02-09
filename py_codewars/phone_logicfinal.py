list1 = ["BLUE", "FOO", "LOW"]
list2 = list(list1[0])
list3 = list(list1[1])
list4 = list(list1[2])
phone_number = input("Enter a phone number? ")
#phone_trans = (translate(phone_number.upper()))
#list5 = list2 + list3 + list4

def translate2(phone_number):
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


print("Word 1 translated " + translate2(list2))
print("Word 2 translated " + translate2(list3))
print("Word 3 translated " + translate2(list4))
phone_trans = ("User provided number translated " + translate2(phone_number.upper()))
print(phone_trans)


if translate2(list2) in phone_trans:
    print("Checking first condition")
    print("Success," + translate2(list2) + " is found in phone number")
elif translate2(list3) in phone_trans:
    print("Not found in first condition, checking second condition")
    print("Success," + translate2(list3) + " is found in phone number")
elif translate2(list4) in phone_trans:
    print("Not found in second condition, checking last condition")
    print("Success," + translate2(list4) + " is found in phone number")
else:
    print("Word does not appear in phone number")

