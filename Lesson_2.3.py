# сравнение значений (логические операторы)
# x = 5
# print(x == 5)
# print(x < 5)
# print(x > 5)
# print(x != 5)
# print(x >= 5)
# print(x <= 5)
# print(x > 3 and x > 8)
# print(x > 3 or x > 8)
# print(not x > 3)

# сравнение условий
# x = 6
# if x == 5: # если
#     print('Five')
# elif x == 6: # иначе если
#     print('Six')
# else: # иначе
#     print('Not five')

# сравнение длинны строки
# x = 'Hello'
# y = 'World'
# if len(x) > len(y):
#     print(x)
# else:
#     print(y)

# поиск и сравнение символа в строке с выводом индекса
# x = 'Hello World, How are you, I am fine, and you?'
# y = (f'В строке {x} найден искомый символ')
# q = input ('Введите искомый символ: ')
# if q in x:
#     print(y), input('Нажмите Enter для поиска индекса искомого элемента: ')
#     if q in x:
#         index = x.index(q)
#         print(f'Индекс искомого элемента: {index}') # вывод индекса искомого элемента (index)
# else:
#     print('Совпадений не найдено')

# ЦИКЛЫ
# i = 0
# while i < 5:
#     i = i + 1
#     if i == 3:
#         # break # выход из цикла
#         continue # переход к следующей итерации цикла
#     print(i)

# отсчет с 5 до 1
# i = 5
# while i > 0:
#     print(i, 'Hello')
#     i = i - 1
# print('Go!')

# вывод с 0 до 9
# for i in range(10):
#     print(i)

# вывод с 1 до 10
# for i in range(1, 11, 1): #1-ое значение: старт, 2-ое: граница, 3-е: шаг
#     print(i)

# вывод каждой буквы с индексом
# i = 'Hello'
# for x in i:
#     print(f'{i.index(x)} - {x}')

# вывод нумерации (списком)
# i = 'Hello'
# for x, i in enumerate(i):
#     print(f'{x} - {i}')

# проверка условий
# a = ''
# if a:
#     print('Not empty')
# else:
#     print('Empty')

# ФУНКЦИИ
# def sum_it (x, y):
#     result = x + y
#     return result #возвращает результат
# print(sum_it(5, 8))
# print(sum_it(25,12))

# Импорт функции из другого файла
# from Lesson_1 import sum_it
# print(sum_it(58,79))

# сравнение значений (логические операторы)
# print('Hello!' != 'Hello')
# сравнение условий
# if 1 < 2:
#     print('True')
# else:
#     print('False')

# сравнение условий
# is_admin = True
# if is_admin:
#     print('Hi, Admin')
# elif is_admin == False:
#     print('Hi, Guest')
# else:
#     print('Hi, User')

# ЦИКЛЫ (цикл for)
# for c in 'Hello': # {c} здесь просто имя переменной
#     print(c)

# проверка пароля
# password = 'qwerty1234@*'
# is_valid = True
# for c in password:
#     if c in '@_*':
#         is_valid = True
# if is_valid:
#     print('Good password')
# else:
#     print('Bad password')

# ЦИКЛЫ (цикл while)
n = 10

# while n > 0:
#     print('Hello')
#     n -= 1

while True:
    print(n)
    n -= 1
    if n == 0:
        break













