import math
try:
    print("Введите значение радиуса круга")
    Radius = float(input())
    ploshad = math.pi * Radius * Radius
    print(ploshad)
except ValueError:
    print("Введите в качестве значения радиуса круга число")
    quit()