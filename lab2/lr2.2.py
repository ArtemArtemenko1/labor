#Організація циклу за допомогою оператора while
#Дано ціле число, що складається з різних цифр. Визначити, яка з цифр заданого числа більше, тобто знайти найбільшу цифру числа.
import re
def check_input(user_input):
    pattern = r"\d"
    user_input=input()
    while not re.match(pattern,user_input):
        user_input = input("Введене значення некоректне!")
    return float(user_input)
def maxDigit():

    num = check_input("num")
    print("число:", num)

    strNum = str(num)

    maxDigit = -1

    for i in range(len(strNum)):
        if strNum[i] == '.':
            continue
        elif maxDigit < int(strNum[i]):
            maxDigit = int(strNum[i])

    print("найбільше число:", maxDigit)
maxDigit()


