#6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#Пример готовой структуры:
#[
    #(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    #(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    #(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#]
#Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
#Пример:
#{
#“название”: [“компьютер”, “принтер”, “сканер”],
#“цена”: [20000, 6000, 2000],
#“количество”: [5, 2, 7],
#“ед”: [“шт.”]
#}

#item = input("Пожалуйста введите название товара ")
#price = input("Пожалуйста введите цену товара ")
#quantity = input("Пожалуйста введите кол-во товара ")
#unit = input("Пожалуйста введите единицу измерения количества товара ")

#dic1 = {"название": item, "цена": price, "кол-во": quantity, "eд": unit}
#cort1 = (1, dic1)
#print(cort1)

tuple_list = []
i = 1
while True:
    tuple_list.append(
        (input('Введите номер товара: '), dict({
            'название': str(input('Введите название: ')),
            'цена': float(input('Введите цену: ')),
            'количество': int(input('Введите количество: ')),
            'eд': str(input('Введите единицы измерения: ')),
        }))
    )

    if input('Добавить еще один товар? (да/нет): ') == 'нет':
        break

    i += 1

print(f'список кортежей:{tuple_list}')

output_dict = dict({})
for product in tuple_list:
    for key, value in product[-1].items():
        if key in output_dict:
            if value not in output_dict.get(key):
                output_dict.get(key).append(value)
        else:
            output_dict.update({key: [value]})


print(f'словарь: {output_dict}')

