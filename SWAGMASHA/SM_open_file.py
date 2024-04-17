from art import tprint

tprint("SWAGMASHA")

from colorama import init
init()
from colorama import Fore, Back, Style

file = input(Fore.MAGENTA + 'Введите путь к файлу для проверки:' + Fore.RESET).strip('"')
print(Style.RESET_ALL) #очистить цвет (для визуального спейса тестов друг от друга)
file = open(f'{file}', 'r', encoding='utf-8')
file = file.read() #готовая переменная для проверки
#print(file) #этот print вызывает печать всего документа (как в inky)
file = file.split('\n') #разбить file на отдельные строки
file = [line.strip() for line in file] #разбитые строки проверить и удалить пробелы
#print(file) #этот print печатает уже разбитый документ (в одной строчке)
#вывести количество строк в файле
print('Количество строк в файле =', len(file))
#input(Fore.MAGENTA + 'Нажмите Enter для выхода\n') #окончание кода для консоли