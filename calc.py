first_number = int(input("plz input first number"))
symbol = input("plz input a symbol from this list(+,-,%,X)")
second_number = int(input("plz input second number"))
add = 0
subtract = 0
divide = 0
multiply = 0
if symbol == ("+"):
    add = first_number + second_number
    print(add)
if symbol == ("X"):
    multiply = first_number * second_number
    print(multiply)
if symbol == ("%"):
    divide = first_number / second_number
    print(divide)
if symbol == ("-"):
    subtract = first_number - second_number
    print(subtract)
