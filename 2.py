print("Введите значение первого катета прямоугольного треугольника:")
try:
    katet1 = float(input())
    print("Введите значение второго катета прямоугольного треугольника:")
    katet2 = float(input())
    gipotenuza = ((katet1**2)+(katet2**2))**(1/2)
    ploshad = (katet1 * katet2)/2
    print("Площадь треугольнка равна:" + str(ploshad))
    perimetr = katet1 + katet2 + gipotenuza
    print("Периметр равен:" + str(perimetr))

except ValueError:
    print("В качестве значения введите ЧИСЛО")
    quit()
