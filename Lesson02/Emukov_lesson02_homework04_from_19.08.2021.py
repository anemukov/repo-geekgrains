#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

words = input("Введите несколько слов через пробел ").split()
for ind, el in enumerate(words, 1):
    print(ind, el[0:10])
