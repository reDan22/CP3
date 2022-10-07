import math

kolvo_exponatov = 2800000
kolvo_exponatov_per_day = 8 * 60 / 5
count = 0
try:
    print("Выберите тип вычислений: Напишите '1' (без кавычек), если хотите вычислить количество экспонатов просмотренных за определённое кол-во лет, и напишите '2'  (без кавычек), если хотите узнать сколько лет потребуется для просмотра определённого кол-ва экспонатов.")
    vibor = input()
    if vibor == "1":
        print("Введите количество лет")
        kolvo_let = float(input())
        kolvo_prosmotrenno = kolvo_let * 365 * kolvo_exponatov_per_day
        #Проверка на високосные года
        visokosnie = math.floor(kolvo_let / 4)
        kolvo_prosmotrenno += kolvo_exponatov_per_day * visokosnie
        
        # Мы не можем посмотреть экспонатов больше, чем их существует
        print("За это количество лет можно посмотреть " + str(int(min(kolvo_exponatov, kolvo_prosmotrenno))) + " экспонатов")
    elif vibor == "2":
        print("Введите количество экспонатов:")
        kolvo_exponatov = int(input())
        #Считаем общее время
        time_potracheno_minut = kolvo_exponatov * 5
        #Считаем сколько лет
        kolvo_let = math.floor(time_potracheno_minut / 60 / 24 / 365)
        #Считаем остаток в минутах с учётом високосных лет
        ostatok = (time_potracheno_minut - kolvo_let * 60 * 24 * 365) - (math.floor(kolvo_let / 4)) * 60 * 24
        #Считаем сколько месяцев
        kolvo_months = math.floor(ostatok / 60 / 24 / 30)
        #Считаем остаток в минутах
        ostatok = ostatok - kolvo_months * 60 * 24 * 30
        #Считаем сколько дней
        kolvo_days = math.floor(ostatok / 60 / 24)
        #Считаем остаток в минутах
        ostatok = ostatok - kolvo_days * 60 * 24
        #Считаем сколько часов
        kolvo_hours = math.floor(ostatok / 60)
        #Считаем остаток в минутах
        ostatok = ostatok - kolvo_hours * 60
        print("На это кол-во экспонатов уйдёт " + str(kolvo_let) + " лет, " + str(kolvo_months) + " месяцев, " + str(kolvo_days) + " дней, " + str(kolvo_hours) + " часов и " + str(ostatok) + " минут!")

    else:
        print("Введите '1' или '2'")


    

except ValueError:
    print("Введите в качестве значения число")
    quit()
