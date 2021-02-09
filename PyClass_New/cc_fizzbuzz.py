
n1 = int(input("Your first divisible number? "))
n2 = int(input("Your second divisible number? "))
n3 = range(1, 101)

for number in n3:
    if number % n1 == 0 and number % n2 == 0:
        print("FizzBuzz")
    elif number % n1 == 0:
        print("Fizz")
    elif number % n2 == 0:
        print("Buzz")
    else:
        print(number)

