#3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
#Пример файла:
#Иванов 23543.12
#Петров 13749.32

with open("503.txt", encoding="UTF-8") as staff_list:

    list_output = staff_list.readlines()

    z = 0
    sum_salaries = 0
    for x in list_output:
        y = x.split()

        if int(y[1]) < 20000:
            print(f"{y[0]} имеет оклад менее 20000 руб")
        z += 1
        sum_salaries += int(y[1])

    print(f"Общая зарплата = {sum_salaries}")
    print(f"Средняя зарплата = {sum_salaries/z}")
