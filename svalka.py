# s = ['foo', 'baz', 'bar']
# for i, word in enumerate(s, 1):
#     print(f'{i} {word}')
#
# count = s.count('foo')
# print('Количество foo:', count)


# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# for i, m in enumerate(months, 1):  # начитать нумерацию с 1
#    print(f'{i}: {m}')

# names = ['Bob', 'Alice', 'Guido']
# print(list(enumerate(names, 1)))


# разбиение на index (результат остается на одной строке через end, различаем введенное значение через [1]
# number = (input("Введите 4-eх значное число: "))
# print ('Тысячи: ', end="")
# print (f'{number}'[0])
# print ('Сотни: ', end="")
# print (f'{number}'[1])
# print ('Десятки: ', end="")
# print (f'{number}'[2])
# print ('Единицы: ', end="")
# print (f'{number}'[3])


# a = 'hello'
# print(a)
# # upper - ставит верхний регистр
# b = 'hello'.upper()
# print(b)
# # lower - ставит нижний регистр
# c = "HELLO".lower()
# print(c)
# # title - ставит 1-ую букву (каждой буквы в строк) заглавной (.capitalize() - только 1-го слова в строке)
# d = 'hEllo world'.title()
# print(d)
# # .swapcase() - меняет регистр
# # .find ("l') - ищет и возвращает индекс того, что введено в '     "
# # .find ( __sub: 'H', __start:2, __end:4) - указывает что искать и в каком диапазоне индексов - возвращет номер индекса
# # .startswith('hel') или .end - возвращают true/fals в зависимости от искомого значения в начале или конце строки
# # .ljust( __width: 10, __fillchar: '*") - вставляет введеное значение в левую часть строки
# # .rjust() - вставляет введеное значение в правую часть строки
# # .center( __width:10, __fillchar: '*') - вставляет введеное значение в центр строки
#
# # обрезание пробелов
# e = '     hello   '.strip()
# print(e)
#
# # обрезание введенной информации (.lstrip и .rstrip - удаление слева и справа)
# f = 'hello'.strip('o')
# print(f)
#
# # разбиение на список
# g = 'Hello World Nikolai'
# h = g.split()
# print(h)
# # приведение к строке
# j = '  '.join(h)
# print(j)

number = input('How old are you?')
print('Your age is:' + number)
print(f'Your age is: {number}')
print('Your age is: {}'.format(str(number)))
