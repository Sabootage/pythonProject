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



# """"x = open('E:/SM/TinderSim_InkChapters/ADRENALINE/CS/ADRENALINE_CH01_CS.ink', 'r', encoding='utf-8')
# c = x.read() #устанавливаем переменную чтения этого файла
# # print(c) #выводим содержимое файла в консоль
# y = (f'В файле {c} найден искомый символ')
# q = input('Введите искомый символ: ')
# if q in c:
#     # print(y),
#     input('Нажмите Enter для поиска индекса искомого элемента: ')
#     if q in c:
#         index = c.index(q)
#         print(f'Индекс искомого элемента: {index}') # вывод индекса искомого элемента (index)
# else:
#     print('Совпадений не найдено')"""


# получим объект файла
# file1 = open("E:/SM/TinderSim_InkChapters/ADRENALINE/CS/ADRENALINE_CH01_CS.ink", "r", encoding="utf-8")
# a = '$price_1'
# while True:
#     # считываем строку
#     line = file1.readline()
#     # прерываем цикл, если строка пустая
#     if not line:
#         break
#     # выводим строку
#     print(line.strip())
# if a in file1:
#     line = file1.count(a)
# print('Количество price_1:', line)
# # else:
# #     print('Совпадений не найдено')
#
# # # закрываем файл
# # file1.close
