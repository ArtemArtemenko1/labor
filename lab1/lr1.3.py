#Обчислення конкретної функції, в залежності від введеного значення х

import re
def check_input(user_input):
    pattern = r"^-?\d+(.\d+)?$"
    user_input=input()
    while not re.match(pattern,user_input):
        user_input = input("Введене значення некоректне!")
    return float(user_input)

def  main():
    x = check_input("x")
    that_list = list(range(-9999, 3))


    if x in that_list:
        print("значение функции при х<=3=", x ** 2 - 3 * x + 9)
    if x not in that_list:
        print("значение функции при х>3=", 1 / x ** 3 - 6)


main()

