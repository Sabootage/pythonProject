import re
file = input('Введите путь к файлу для проверки:').strip('"')
file = open(f'{file}', 'r', encoding='utf-8')
file = file.read() #готовая переменная для проверки

"""
    print(file) #печать всего документа (как в inky)
    print(type(file)) #class str
"""

file = file.split('\n') #разбитие file на отдельные строки -> class list
file = [line.strip() for line in file] #разбитые строки проверить и удалить пробелы
print('Количество строк в файле =', len(file))

new_file = list(filter(lambda item: isinstance(item, str) and '-' in item, file))
print(new_file)

# new_file = list(filter(lambda item: isinstance(item, str) and '-' in item, file))
# print(new_file)
# new_file = str(new_file)
# print(re.findall(r'[-]', new_file))


# file2 = input('Пожалуйста, введи путь к файлу #2: ').strip('"')
# file2 = open(f'{file2}', 'r', encoding='utf-8')
# file2 = file2.read()
# file2 = file2.split('\n') #разбить file2 на отдельные строки
# file2 = [line.strip() for line in file2] #разбитые строки проверить и удалить пробелы
#
# print(file2) #вывести полностью файл #2
# print(type(file2)) #class list(проверка типа)
# print('Количество строк в файле #2 =', len(file2)) #вывести количестков строк в файле#2

# file1 = str(file1)
# file2 = str(file2)

# result = file1 in file2
# print(result)








# if 'INCLUDE' in file1: #проверка наличия значения 'CMD' в списке file1
#     print(file1.index('CMD'))
# else:
#     print('В списке нет значения "CMD"')



# fr = "" #переменная для хранения результата
#
# for 'CMD' in file1: #проходимаcя по нашему листу
#     if line == 'CMD' or line == '.ink': #если эти значения входят в список
#         continue #пропускаем итерацию
#     else: #иначе
#         fr += (line + '\n') #добавляем в результирующий лист
# print(fr) #выводим результирующий лист
# print(type(fr)) #class str
# # fr = list(fr.split('\n')) #разбиваем на отдельные строки
# print(type(fr)) #class list
#
# cmd = fr.find('CMD') #поиск значения 'CMD'
# #вывести строку с индексом cmd
# print(fr.index.str(cmd))



# file1 = set(file1)
# file2 = set(file2)
#
# # result = [x for x in file1 if x in file2]
# # print(result)
#
# result = file1.intersection(file2) #пересечение множеств
# print(result)

# #из result исключить строки, содержащие CMD в названии
# result = [x for x in result if 'CMD' not in x]
# # print(result)
# #из result исключить строки, содержащие слова c comment //
# result = [x for x in result if '//' not in x]
# # print(result)
# #из result исключить строки, содержащие слова с ->
# result = [x for x in result if '->' not in x]
# # print(result)
# #из result исключить строки, содержащие слова с ===
# result = [x for x in result if '===' not in x]
# # print(result)
# #найти result в file3 и file_new_3 и вывести индекс строки
# print(result)
#
# #если остаются пересечения множеств, выввести индекса строк из file_3 и file_new_3
# # file3 = list(file3)
# # file_new_3 = list(file_new_3)
# # print('Количество строк в файле #1 =', len(file3))
# # for i in result:
# #     if i in file_new_3:
# #         print('Индекс пересекающейся строки в файле #2 "', i, '" в file_new_3 =', file_new_3.index(i))
#

input('Нажмите Enter для выхода\n')