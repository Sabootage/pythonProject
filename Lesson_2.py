# вывод типа данных через переменную
a = 100
type_a = type(a)
print(a, type_a)
# вывод типа данных через функцию
b = 3.14
print(b, type(b))

# вывод данных в файл с созданием нового файла (.txt .doc .docx ...)
b = 3.14
print(b, type(b), file=open('test_my.doc', 'w'))

# сравнение значений (выводится True или False)
a = 100
b = 3.14
print(a is b)

# форматирование текста
name = 'Bob'
surname = 'Williams'
print(f'Hello, {name} {surname}!')
print('Hello, {} {}!'.format(name, surname))

# ввод данных с клавиатуры + удаление пробелов + перевод в верхний регистр первой буквы
name = input('What is your name? ')
strip_name = name.strip().title() # удаление пробелов и перевод в верхний регистр (2 метода сразу)
# title_name = strip_name.title() # только перевод в верхний регистр первой буквы
print(f'Hello, {strip_name}!')
result = strip_name # создаем итоговую переменную
for i, item in enumerate (result, 1):
    print(i, item)










