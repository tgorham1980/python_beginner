def alphabet_position(text):
    letters = "abcdefghijklmnopqrstuvwxyz"
    trans = []
    for i in text:
        if i.isalpha() and i.islower() and i in letters:
            i = letters.index(i) + 1
            trans.append(i)
        elif i.isalpha() and i.isupper():
            i = letters.upper().index(i) + 1
            trans.append(i)
        else:
            pass
    trans = str(trans)[1:-1] #slicing method
    trans2 = trans.rstrip()
    trans3 = trans2.replace(',', '')
    #print("'" + trans3 + "'")
    trans4 = (str(trans3))
    return trans4

print(alphabet_position("The sunset sets at twelve o' clock."))

