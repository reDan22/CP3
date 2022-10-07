print("Введите имя студента(Например: Иван):")
Student_name = input()
print("Введите фамилию студента(Например: Иванов):")
Student_second_name = input()
# Я не знаю как сделать проверку типа string
try:
    print("Введите год рождения студента(Например: 1998):")
    Student_birthday = int(input())
except:
    print("Указывайте именно число в качестве года рождения")
    quit()

print(Student_name + "_" + Student_second_name + "_" + str(Student_birthday))

Student_name, Student_second_name = Student_second_name, Student_name

Student_birthday = str(int(Student_birthday) + 60) 

print(Student_name + "_" + Student_second_name + "_" + str(Student_birthday))