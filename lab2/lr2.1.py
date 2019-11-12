#Організація циклу за допомогою оператора while
import re
def check_input(user_input):
    pattern = r"^-?\d+(.\d+)?$"
    user_input=input()
    while not re.match(pattern,user_input):
        user_input = input("Введене значення некоректне!")
    return float(user_input)
def main():
     n = check_input("Введіть число n: ")
     sum = 0
     x = check_input("Введіть число:x ")
     i = 1
     while i <= n:
         sum += i * x
         i += 1
     print("sum = ", sum)



print(main())
