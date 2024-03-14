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


# ввод данных с клавиатуры + удаление пробелов + перевод в верхний регистр первой буквы
name = input('What is your name? ')
strip_name = name.strip().title() # удаление пробелов и перевод в верхний регистр
# title_name = strip_name.title() # только перевод в верхний регистр первой буквы
print(f'Hello, {strip_name}!')
result = strip_name # создаем итоговую переменную
for i, item in enumerate (result, 1):
    print(i, item)