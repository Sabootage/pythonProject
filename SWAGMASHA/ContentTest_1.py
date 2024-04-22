from art import tprint

tprint("SWAGMASHA")

from colorama import init
init()
from colorama import Fore, Back, Style

file = input(Fore.MAGENTA + 'Введите путь к файлу для проверки:' + Fore.RESET).strip('"') #переменная для пути к файлу с делитом "" (для удобства ctrl+C)
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)
print(Fore.BLACK + Back.WHITE + "Тест платных выборов: " + Fore.RESET + Back.RESET) #цвет и имя теста для визуального спейса
file = open(f'{file}', 'r', encoding='utf-8') #открытие файла в кодировке utf-8
file = file.read() #чтение файла
#print(file) #этот print вызывает печать всего документа (как в inky)
file = file.split('\n') #разбить file на отдельные строки (для дальнейших тестов по строкам)
file = [line.strip() for line in file] #разбитые строки проверить и удалить пробелы
#print(file) #этот print вызывает печать уже разбитого по строкам документа
print('Количество строк в файле =', len(file)) #вывести количество строк в файле

'''ТЕСТ ПЛАТНЫХ ВЫБОРОВ'''
count_paid = 0 #счётчк для //Paid (нужно для принта если //Paid будут в файле)
for line in file: #запускаем цикл по строкам в файле
    if '//Paid' in line: #если в строке есть //Paid
        count_paid += 1 #прибавляем к счётчку 1-цу
    else: #если нет
        continue #продолжаем цикл
if count_paid > 0: #если счётчик больше 0 (т.е. если в файле есть //Paid) принтуем количество
    print('Количество строк, содержащих ' + Fore.GREEN + '"//Paid" =', [count_paid], '' + Fore.RESET)

#аналогичный цикл для //Premium
count_premium = 0
for line in file:
    if '//Premium' in line:
        count_premium += 1
    else:
        continue
if count_premium > 0:
    print('Количество строк, содержащих ' + Fore.GREEN + '"//Premium" =', [count_premium], '' + Fore.RESET)

#аналогичный цикл для прочих //комментариев
count_other_price = 0 #подсчет прочих (возможных неймингов) платных выборов
for line in file:
    if '//sub-interactive' in line:
        count_other_price += 1
        # print('В файле также найдены платные выборы ' + Fore.YELLOW + '"//sub-interactive" ' + Fore.RESET + 'строка №', [file.index(line) + 1])
    elif '//Sub-interactive' in line:
        count_other_price += 1
        # print('В файле также найдены платные выборы ' + Fore.YELLOW + '"//Sub-interactive" ' + Fore.RESET + 'строка №', [file.index(line) + 1])
    elif '//PREM' in line:
        count_other_price += 1
    else:
        continue

if count_other_price > 0: #если в файле есть //[S]sub-interactive/PREM, выводим их количество и общую сумму с //Paid и //Premium
    print('Количество строк, содержащих ' + Fore.GREEN + '"//[S]sub-interactive//PREM" =', [count_other_price], '' + Fore.RESET)
    print('Всего в файле', '' + Fore.GREEN + '', [count_paid + count_premium + count_other_price], '' + Fore.RESET, '//Paid/Premium/PREM/Sub-interactive')

#найти и посчитать количество строк, содержащих "$price_"
count_price = 0
for line in file:
    if '$price_' in line:
        count_price += 1
print('Количество строк, содержащих ' + Fore.GREEN + '"$price_" =', [count_price], '' + Fore.RESET)

#проверить равентсво Paid/Premium/Sub-interactive/PREM и $price_
if count_paid + count_premium + count_other_price == count_price:
    print(Fore.GREEN + 'Тест пройден успешно: есть все платные выборы')
elif count_paid + count_premium + count_other_price < count_price:
    print(Fore.YELLOW + 'Тест пройден, вероятно пропущены комментарии ' + Fore.RESET + '[$price > //Paid/Premium/PREM/Sub-interactive]')
else:
    print(Fore.RED + 'Возможно, пропущен платный выбор, пожалуйста, проверьте документ вручную')
print(Style.RESET_ALL) #очистить цвет

'''ТЕСТЫ $price_1_2_3'''
print(Fore.BLACK + Back.WHITE + "Тест $price1: " + Fore.RESET + Back.RESET)
count_price = 0 #счётчк на случай ошибки
#цикл для поиска "$price_1" с номером строки
for line in file:
    if '$price_1' in line:
        #вывести номер строки, содержащей "$price_1"
        # print(Fore.CYAN + 'Номер строки, содержащей "$price_1" =', file.index(line) + 1) #для удобства, начинаем считать с 1
        # print(Style.RESET_ALL + line)
        #сравнить, что в строке '$price_1' содержатся '_price_1'
        if '_price_1' in line:
            continue
            #print(Fore.GREEN + 'Тест пройден успешно')
        elif '_price_1' not in line:
            if '_price_3' in line:
                count_price += 1
                print(Fore.RED + 'Тест провален, проверьте строку:', [file.index(line) + 1])
                print(Style.RESET_ALL + line)
            elif '_price_2' in line:
                count_price += 1
                print(Fore.RED + 'Тест провален, проверьте строку:', [file.index(line) + 1])
                print(Style.RESET_ALL + line)
            elif '_price_1' not in line:
                continue
                #print(Fore.YELLOW + 'Тег_1 отсутствует', Fore.GREEN + 'DONE')
            else:
                count_price += 1
                print(Fore.RED + 'Тест провален: проверьте тег')
        # else:
        #     print(Fore.RED + 'Тест провален: нужно вмешательство')
if count_price == 0:
    print(Fore.GREEN + 'Тесты $price1 пройдены успешно')
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)

#найти и напечатать строки, содержашие "$price_2" с номером строки
print(Fore.BLACK + Back.WHITE + "Тест $price2: " + Fore.RESET + Back.RESET)
count_price_2 = 0  #счётчик для $price_2 (реализуем проверку если $price_2 не используется в файле)
count_price = 0  #счётчик на случай ошибки
for line2 in file:
    if '$price_2' in line2:
        count_price_2 += 1
        #вывести номер строки, содержащей "$price_2"
        # print(Fore.CYAN + 'Номер строки, содержащей "$price_2" =', file.index(line2) + 1) #для удобства, начинаем считать с 1
        # print(Style.RESET_ALL + line2)
        #сравнить, что в строке '$price_2' содержатся '_price_2'
        if '_price_2' in line2:
            continue
            #print(Fore.GREEN + 'Тест пройден успешно')
        elif '_price_2' not in line2:
            if '_price_3' in line2:
                count_price += 1
                print(Fore.RED + 'Тест провален, проверьте строку:', [file.index(line2) + 1])
                print(Style.RESET_ALL + line2)
            elif '_price_1' in line2:
                count_price += 1
                print(Fore.RED + 'Тест провален, проверьте строку:', [file.index(line2) + 1])
                print(Style.RESET_ALL + line2)
            elif '_price_2' not in line2:
                continue
                #print(Fore.YELLOW + 'Тег_2 отсутствует', Fore.GREEN + 'DONE')
            else:
                count_price += 1
                print(Fore.RED + 'Тест провален: проверьте тег')
        # else:
        #     print(Fore.RED +'Тест провален, нужно вмешательство')
if count_price_2 == 0:
    print(Fore.YELLOW + '$price_2 в файле не используется')
if count_price_2 > 0 and count_price == 0: #если $price_2 реализован в файле и счётчик ошибок пустой
    print(Fore.GREEN + 'Тесты $price2 пройдены успешно')
print(Style.RESET_ALL) #очистить цвет

#найти и напечатать строки, содержашие "$price_3" с номером строки
print(Fore.BLACK + Back.WHITE + "Тест $price3: " + Fore.RESET + Back.RESET)
count_price_3 = 0  #счётчик если $price_3 не используется в файле
count_price = 0  #счётчик на случай ошибки
for line3 in file:
    if '$price_3' in line3:
        count_price_3 += 1
        #вывести номер строки, содержащей "$price_3"
        # print(Fore.CYAN + 'Номер строки, содержащей "$price_3" =', file.index(line3) + 1) #для удобства, начинаем считать с 1
        # print(Style.RESET_ALL + line3)
        #сравнить, что в строке '$price_3' содержатся '_price_3'
        if '_price_3' in line3:
            continue
            #print(Fore.GREEN + 'Тест пройден успешно')
        elif '_price_3' not in line3:
            if '_price_2' in line3:
                count_price += 1
                print(Fore.RED + 'Тест провален, проверьте строку:', [file.index(line3) + 1])
                print(Style.RESET_ALL + line3)
            elif '_price_1' in line3:
                count_price += 1
                print(Fore.RED + 'Тест провален, проверьте строку:', [file.index(line3) + 1])
                print(Style.RESET_ALL + line3)
            elif '_price_3' not in line3:
                continue
                #print(Fore.YELLOW + 'Тег_3 отсутствует', Fore.GREEN + 'DONE')
            else:
                count_price += 1
                print(Fore.RED + 'Тест провален: проверьте тег')
        # else:
        #     print(Fore.RED + 'Тест провален: нужно вмешательство')
if count_price_3 == 0:
    print(Fore.YELLOW + '$price_3 в файле не используется')
if count_price_3 > 0 and count_price == 0:
    print(Fore.GREEN + 'Тесты $price3 пройдены успешно')
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)

'''ДОП. ТЕСТ для проверки удаления тега'''
#доп. тест на delete $price
print(Fore.BLACK + Back.WHITE + "Доп. тест (delete $price): " + Fore.RESET + Back.RESET)
count_dell = 0  #счётчик для elif
for line_del in file:
    if '_price_' in line_del:
        if '$price_' in line_del:
            continue #для конечного пользователя
            # print(Fore.GREEN + 'Тест удаления $price пройден успешно')
        elif '$price_' not in line_del:
            count_dell += 1
            print(Fore.RED + 'Тест удаления тегов провален: проверьте строку', [file.index(line_del) + 1])
            print(Fore.RESET + line_del)
if count_dell == 0:
    print(Fore.GREEN + 'Тест удаления $price пройден успешно')
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)

'''ТЕСТ для проверки #playerEmoji'''
# Test на проверку #playerEmoji
print(Fore.BLACK + Back.WHITE + "Тест #playerEmoji: " + Fore.RESET + Back.RESET)
count_playeremoji = 0
for line in file:
    if '#playerEmoji' in line: #если строка содержит #playerEmoji
        #в этой же строке должен быть текст 'NPC:'
        if 'NPC:' in line: #если строка содержит NPC: или CMD #iamge
            continue
            # print(Fore.GREEN + 'Тест #playerEmoji пройден успешно', Fore.RESET + 'Номер строки =', file.index(line) + 1) #для удобства, начинаем считать с 1
        elif 'CMD #image' in line: #если строка содержит CMD #iamge
            continue
            # print(Fore.GREEN + 'Тест #playerEmoji пройден успешно', Fore.RESET + 'Номер строки =', file.index(line) + 1) #для удобства, начинаем считать с 1
        elif 'NPC:' not in line:
            count_playeremoji += 1
            print(Fore.RED + 'Тест #playerEmoji провален, проверьте строку: ', [file.index(line) + 1]) #для удобства, начинаем счиать с 1
            print(Fore.RESET + line)
        else:
            print(Fore.RED + 'Тест провален: проверьте соответствие #playerEmoji и NPC в строке: ', [file.index(line) + 1]) #для удобства, начинаем считать с 1
if count_playeremoji == 0:
    print(Fore.GREEN + 'Тест #playerEmoji пройден успешно')
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)

'''ТЕСТ для проверки #charEmoji'''
# Test на проверку #charEmoji
print(Fore.BLACK + Back.WHITE + "Тест #charEmoji: " + Fore.RESET + Back.RESET)
count_charemoji = 0
for line in file:
    if '#charEmoji' in line: #если строка содержит #charEmoji
        #в этой же строке должен быть текст 'Player:'
        if 'Player:' in line:
            continue
            #print(Fore.GREEN + 'Тест #charEmoji пройден успешно', Fore.RESET + 'Номер строки =', file.index(line) + 1) #для удобства, начинаем считать с 1
        elif 'Player:' not in line: #если нет 'Player:'
            if '[ID ' in line:
                continue
                #print(Fore.GREEN + 'Тест #charEmoji+ID пройден успешно', Fore.RESET + 'Номер строки =', file.index(line) + 1) #для удобства, начинаем считать с 1
            else:
                count_charemoji += 1
                print(Fore.RED + 'Тест #charEmoji провален, проверьте строку: ', [file.index(line) + 1]) #для удобства, начинаем счиать с 1
                print(Fore.RESET + line)
        else:
            print(Fore.RED + 'Тест провален: проверьте соответствие #charEmoji и Player в строке: ', [file.index(line) + 1]) #для удобства, начинаем считать с 1
if count_charemoji == 0:
    print(Fore.GREEN + 'Тест #charEmoji пройден успешно')
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)

'''ТЕСТ для проверки #progressPoints'''
# Test проверки #progressPoints
print(Fore.BLACK + Back.WHITE + "Тест #progressPoints: " + Fore.RESET + Back.RESET)
count_cutscene = 0 #счётчик для #endCutscene
for line in file:
    if '#endCutscene' in line:
        count_cutscene += 1
        #if '#progressPoints' in file3[file3.index(line) + 1]:
        if '#progressPoints' in line:
            print(Fore.GREEN + 'Тест progressPoints пройден успешно')
        else:
            print(Fore.RED + '#ProgressPoints отсутсвует', Fore.RESET + 'Номер строки =', file.index(line) + 1) #для удобства, начинаем считать с 1
if count_cutscene == 0:
    print(Fore.YELLOW + 'Cutscene в файле не используется')
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)

'''ТЕСТ для проверки реплик Player: Player и NPC: NPC'''
#Test проверить, что НЕТ строк 'Player: Player' и 'NPC: NPC'
print(Fore.BLACK + Back.WHITE + "Тесты реплик Player:/NPC:" + Fore.RESET + Back.RESET)
count_Player = 0 #счётчик для Player: Player
for line in file:
    if 'Player: Player' in line:
        count_Player += 1
        print(Fore.RED + 'Тест Player провален, проверьте строку: ', [file.index(line) + 1], Fore.RESET) #для удобства, начинаем считать с 1
        print(Fore.RESET + line)
count_NPC = 0  # счётчик для NPC: NPC
for line in file:
    if 'NPC: NPC' in line:
        count_NPC += 1
        print(Fore.RED + 'Тест NPC провален, проверьте строку: ', [file.index(line) + 1], Fore.RESET) #для удобства, начинаем считать с 1
        print(Fore.RESET + line)
if count_Player == 0 and count_NPC == 0:
    print(Fore.GREEN + 'Тесты репита для Player и NPC пройдены успешно')
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)

'''ТЕСТ для проверки статусов'''
print(Fore.BLACK + Back.WHITE + "Тесты Статусов: " + Fore.RESET + Back.RESET)
# посчитать количество 'CMD #statusOnline' в файле
countOnline = file.count('CMD #statusOnline')
# посчитать количество 'CMD #statusInactive' в файле
countInactive = file.count('CMD #statusInactive=minutes:240') #нужно точное совпадение (без '=minutes:240' не проходит)
# посчитать количество 'CMD #statusOffline' в файле
countOffline = file.count('CMD #statusOffline')

if countInactive + countOffline == countOnline:
    print(Fore.GREEN + 'Тесты статусов пройдены успешно')
else:
    print(Fore.RED + 'Тесты статусов провалены:', Fore.RESET,
          '\nStatusOnline =', [countOnline],
          '\nStatusInactive =', [countInactive],
          '\nStatusOffline =', [countOffline])
print(Style.RESET_ALL) #очистить цвет

'''ТЕСТ для проверки статусов (нужно количество чаптеров в файле)'''
# #Test_1 (проверка Online статуса)
# print(Fore.BLACK + Back.WHITE + "Тесты Статусов: " + Fore.RESET + Back.RESET)
# ch = int(input(Fore.MAGENTA + 'Пожалуйста, введите количество чаптеров в файле: ' + Fore.RESET))
# print(Style.RESET_ALL) #очистить цвет
# # посчитать количество 'CMD #statusOnline' в файле
# countOnline = file.count('CMD #statusOnline')
# print('Количество "CMD #statusOnline" в файле =', countOnline)
# if countOnline == ch:
#     print(Fore.GREEN + 'Тест Online пройден успешно')
# else:
#     print(Fore.RED + 'Тест Online провален, вероятно, стоит проверить документ вручную')
#
# #Test_2 (проверка Inactive статуса)
# print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)
# #посчитать количество 'CMD #statusInactive' в файле
# countInactive = file.count('CMD #statusInactive=minutes:240')
# print('Количество "CMD #statusInactive" в файле =', countInactive)
# if countInactive == ch -1: #если количество "CMD #statusInactive" равно введенному количеству чапетров, уменьшеному на 1
#     print(Fore.GREEN + 'Тест Inactive пройден успешно')
# else:
#     print(Fore.RED + 'Тест Inactive провален, вероятно, стоит проверить документ вручную')
#
# #Test_3 (проверка Offline статуса)
# print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)
# if 'CMD #statusOffline' in file:
#     #посчитать количество 'CMD #statusOffline' в файле
#     countOffline = file.count('CMD #statusOffline')
#     print('Количество CMD #statusOffline =', countOffline)
#     if countOffline == 1:
#         print(Fore.GREEN + 'Тест Offline пройден успешно')
#     else:
#         print(Fore.RED + 'Тест Offline провален')
# else:
#     print('CMD #statusOffline не найден')

input(Fore.MAGENTA + 'Нажмите Enter для выхода\n')

