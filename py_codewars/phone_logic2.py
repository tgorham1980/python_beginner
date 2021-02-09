"""char_numbers = [('abc',2), ('def',3), ('ghi',4), ('jkl',5), ('mno',6), ('pqrs',7), ('tuv',8), ('wxyz',9)]
char_num_map = {c:v for k,v in char_numbers for c in k}
phone = "1800flowers"
result = "".join(str(char_num_map.get(v,v)) for v in phone.lower())
print(result)"""

#My own solution!!!

list1 = ["blue", "foo", "green"]


def translate2(list1):
    translation2 = ""
    for letter in list1:
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
    return translation2


def translate(phone_number):
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


phone_number = input("Enter a phone number? ")
#converts any input to capital
phone_trans = (translate(phone_number.upper()))
#converts output to an integer
print(int(phone_trans))


phone_trans2 = (translate2(list1))
print(phone_trans2)

