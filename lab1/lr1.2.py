#Увести з клавіатури три дійсних числа. Піднести до квадрата ті з них, значення яких невід'ємні, і в четверту ступінь - від`ємні .
import re
def check_input(user_input):
    pattern = r"\d"
    user_input = input()
    while not re.match(pattern,user_input):
        user_input = input("Введене значення некоректне!")
    return float(user_input)


def stepen() :

    a =check_input( "a")
    b = check_input("b")
    c = check_input("c")
    if a > 0:
        print("a=", a ** 2)
    else:
        print("a=", a ** 4)

    if a > 0:
        print("b=", b ** 2)
    else:
        print("b=", b ** 4)
    if c > 0:
        print("c=", c ** 2)
    else:
        print("c=", c ** 4)


print(stepen())

