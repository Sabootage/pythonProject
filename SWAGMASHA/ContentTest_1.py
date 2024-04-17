from art import tprint

tprint("SWAGMASHA")

from colorama import init
init()
from colorama import Fore, Back, Style

file = input(Fore.MAGENTA + 'Введите путь к файлу для проверки:' + Fore.RESET).strip('"')
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)
print(Fore.BLACK + Back.WHITE + "Тест платных выборов: " + Fore.RESET + Back.RESET)
file = open(f'{file}', 'r', encoding='utf-8')
file = file.read() #готовая переменная для проверки
#print(file) #этот print вызывает печать всего документа (как в inky)
file = file.split('\n') #разбить file на отдельные строки
file = [line.strip() for line in file] #разбтые строки проверить и удалить пробелы
#print(file) #этот print печатает уже разбитый документ
#вывести количестков строк в файле
print('Количество строк в файле =', len(file))
#найти и псчитать количество строк, содержащих "//Paid"
count = 0
for line in file:
    if '//Paid' in line:
        count += 1
#если //Paid будет = 0, найти и посчитать количество строк, содержащих "Premium"
print('Количество строк, содержащих "//Paid" =', count)
if count == 0:
    for line in file:
        if '//Premium' in line:
            count += 1
    print('Количество строк, содержащих "Premium" =', count)
#найти и посчитать количество строк, содержащих "$price_"
count2 = 0
for line in file:
    if '$price_' in line:
        count2 += 1
print('Количество строк, содержащих "$price_" =', count2)
#проверить равентсво Paid/Premium и $price_
if count == count2:
    print(Fore.GREEN + 'Тест пройден успешно: есть все платные выборы')
else:
    print(Fore.RED + 'Возможно, пропущен платный выбор, пожалуйста, проверьте документ вручную')
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)
#найти и напечатать строки, содержашие "$price_1" с номером строки
print(Fore.BLACK + Back.WHITE + "Тест $price1: " + Fore.RESET + Back.RESET)
for line in file:
    if '$price_1' in line:
        #вывести номер строки, содержащей "$price_1"
        print(Fore.CYAN + 'Номер строки, содержащей "$price_1" =', file.index(line) + 1) #для удобства, начинаем счиать с 1
        print(Style.RESET_ALL + line)
        #сравнить, что в строке '$price_1' содержатся '_price_1'
        if '_price_1' in line:
            print(Fore.GREEN + 'Тест пройден успешно')
        elif '_price_1' not in line:
            if '_price_3' in line:
                print(Fore.RED + 'Тест провален: неверный тег')
            elif '_price_2' in line:
                print(Fore.RED + 'Тест провален: неверный тег')
            elif '_price_1' not in line:
                print(Fore.YELLOW + 'Тег_1 отсутствует', Fore.GREEN + 'DONE')
            else:
                print(Fore.RED + 'Тест провален: проверьте тег')
        else:
            print(Fore.RED + 'Тест провален: нужно вмешательство')
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)
#найти и напечатать строки, содержашие "$price_2" с номером строки
print(Fore.BLACK + Back.WHITE + "Тест $price2: " + Fore.RESET + Back.RESET)
for line2 in file:
    if '$price_2' in line2:
        #вывести номер строки, содержащей "$price_2"
        print(Fore.CYAN + 'Номер строки, содержащей "$price_2" =', file.index(line2) + 1) #для удобства, начинаем счиать с 1
        print(Style.RESET_ALL + line2)
        #сравнить, что в строке '$price_2' содержатся '_price_2'
        if '_price_2' in line2:
            print(Fore.GREEN + 'Тест пройден успешно')
        elif '_price_2' not in line2:
            if '_price_3' in line2:
                print(Fore.RED + 'Тест провален: неверный тег')
            elif '_price_1' in line2:
                print(Fore.RED + 'Тест провален: неверный тег')
            elif '_price_2' not in line2:
                print(Fore.YELLOW + 'Тег_2 отсутствует', Fore.GREEN + 'DONE')
            else:
                print(Fore.RED + 'Тест провален: проверьте тег')
        else:
            print(Fore.RED +'Тест провален, нужно вмешательство')
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)
#найти и напечатать строки, содержашие "$price_3" с номером строки
print(Fore.BLACK + Back.WHITE + "Тест $price3: " + Fore.RESET + Back.RESET)
for line3 in file:
    if '$price_3' in line3:
        #вывести номер строки, содержащей "$price_3"
        print(Fore.CYAN + 'Номер строки, содержащей "$price_3" =', file.index(line3) + 1) #для удобства, начинаем счиать с 1
        print(Style.RESET_ALL + line3)
        #сравнить, что в строке '$price_3' содержатся '_price_3'
        if '_price_3' in line3:
            print(Fore.GREEN + 'Тест пройден успешно')
        elif '_price_3' not in line3:
            if '_price_2' in line3:
                print(Fore.RED + 'Тест провален: неверный тег')
            elif '_price_1' in line3:
                print(Fore.RED + 'Тест провален: неверный тег')
            elif '_price_3' not in line3:
                print(Fore.YELLOW + 'Тег_3 отсутствует', Fore.GREEN + 'DONE')
            else:
                print(Fore.RED + 'Тест провален: проверьте тег')
        else:
            print(Fore.RED + 'Тест провален: нужно вмешательство')
# else:
#     print(Fore.RED + '$price_3 не найден') #закоменчено, т.к. не ясно поведение с одновременным выводом if и else о том, что price не найден
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)
# Test на проверку #playerEmoji
print(Fore.BLACK + Back.WHITE + "Тест #playerEmoji: " + Fore.RESET + Back.RESET)
for line in file:
    if '#playerEmoji' in line: #если строка содержит #playerEmoji
        #в этой же строке должен быть текст 'NPC:'
        if 'NPC:' or 'CMD #image' in line: #если строка содержит NPC: или CMD #iamge
            print(Fore.GREEN + 'Тест #playerEmoji пройден успешно', Fore.RESET + 'Номер строки =', file.index(line) + 1) #для удобства, начинаем счиать с 1
        elif 'NPC:' not in line:
            print(Fore.RED + 'Тест #playerEmoji провален, проверьте строку: ', file.index(line) + 1) #для удобства, начинаем счиать с 1
        else:
            print(Fore.RED + 'Тест провален: проверьте соответствие #playerEmoji и NPC в строке: ', file.index(line) + 1) #для удобства, начинаем счиать с 1
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)
# Test на проверку #charEmoji
print(Fore.BLACK + Back.WHITE + "Тест #charEmoji: " + Fore.RESET + Back.RESET)
for line in file:
    if '#charEmoji' in line: #если строка содержит #charEmoji
        #в этой же строке должен быть текст 'Player:'
        if 'Player:' in line:
            print(Fore.GREEN + 'Тест #charEmoji пройден успешно', Fore.RESET + 'Номер строки =', file.index(line) + 1) #для удобства, начинаем счиать с 1
        elif 'Player:' not in line: #если нет 'Player:'
            if ('[ID ') in line:
                print(Fore.GREEN + 'Тест #charEmoji+ID пройден успешно', Fore.RESET + 'Номер строки =', file.index(line) + 1) #для удобства, начинаем счиать с 1
            else:
                print(Fore.RED + 'Тест #charEmoji+ID провален, проверьте строку: ', file.index(line) + 1) #для удобства, начинаем счиать с 1
        else:
            print(Fore.RED + 'Тест провален: проверьте соответствие #charEmoji и Player в строке: ', file.index(line) + 1) #для удобства, начинаем счиать с 1
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)
# Test проверки progressPoints
print(Fore.BLACK + Back.WHITE + "Тест #progressPoints: " + Fore.RESET + Back.RESET)
for line in file:
    if '#endCutscene' in line:
        #if '#progressPoints' in file3[file3.index(line) + 1]:
        if '#progressPoints' in line:
            print(Fore.GREEN + 'Тест progressPoints пройден успешно')
        else:
            print(Fore.RED + 'Тест progressPoints провален', Fore.RESET + 'Номер строки =', file.index(line) + 1) #для удобства, начинаем счиать с 1
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)
#Test проверить, что НЕТ строк 'Player: Player' и 'NPC: NPC'
print(Fore.BLACK + Back.WHITE + "Тесты отсутсвия в репликах Player:/NPC:" + Fore.RESET + Back.RESET)
for line in file:
    if 'Player: Player' in line:
        print(Fore.RED + 'Тест Player провален', Fore.RESET + 'Номер строки =', file.index(line) + 1) #для удобства, начинаем счиать с 1
for line in file:
    if 'NPC: NPC' in line:
        print(Fore.RED + 'Тест NPC провален', Fore.RESET + 'Номер строки =', file.index(line) + 1) #для удобства, начинаем счиать с 1
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)
#Test_1 (проверка Online статуса)
print(Fore.BLACK + Back.WHITE + "Тесты Статусов: " + Fore.RESET + Back.RESET)
ch = int(input(Fore.MAGENTA + 'Пожалуйста, введите количество чаптеров в файле: ' + Fore.RESET))
print(Style.RESET_ALL) #очистить цвет
# посчитать количество 'CMD #statusOnline' в файле
countOnline = file.count('CMD #statusOnline')
print('Количество "CMD #statusOnline" в файле =', countOnline)
if countOnline == ch:
    print(Fore.GREEN + 'Тест Online пройден успешно')
else:
    print(Fore.RED + 'Тест Online провален, вероятно, стоит проверить документ вручную')
#Test_2 (проверка Inactive статуса)
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)
#посчитать количество 'CMD #statusInactive' в файле
countInactive = file.count('CMD #statusInactive=minutes:240')
print('Количество "CMD #statusInactive" в файле =', countInactive)
if countInactive == ch -1: #если количество "CMD #statusInactive" равно введенному количеству чапетров, уменьшеному на 1
    print(Fore.GREEN + 'Тест Inactive пройден успешно')
else:
    print(Fore.RED + 'Тест Inactive провален, вероятно, стоит проверить документ вручную')
#Test_3 (проверка Offline статуса)
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)
if 'CMD #statusOffline' in file:
    #посчитать количество 'CMD #statusOffline' в файле
    countOffline = file.count('CMD #statusOffline')
    print('Количество CMD #statusOffline =', countOffline)
    if countOffline == 1:
        print(Fore.GREEN + 'Тест Offline пройден успешно')
    else:
        print(Fore.RED + 'Тест Offline провален')
else:
    print('CMD #statusOffline не найден')
input(Fore.MAGENTA + 'Нажмите Enter для выхода\n')

