#Скласти програму переведення радіанної міри кута в градуси, хвилини і секунди.
import math

import re
def check_input(user_input):
    pattern =r"^-?\d+(.\d+)?$"
    user_input=input()
    while not re.match(pattern,user_input):
        user_input = input("Введене значення некоректне!")
    return float(user_input)
def rad():
    radians = check_input("q")
    totalSeconds = round(radians * 360 * 60 * 60 / (2 * (math.pi)))
    seconds = totalSeconds % 60
    minutes = (totalSeconds / 60) % 60
    degrees = totalSeconds / (60 * 60)
    print("seconds=", seconds)
    print("minutes=", minutes)
    print("degrees=", degrees)

rad()
