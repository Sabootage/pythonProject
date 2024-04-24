
"""
    Программа для поиска общих элементов в двух списках
    с использованием функции lambda и filter() (ВЫВЕДЕТ ТОЛЬКО ТОЧНЫЕ СОВПАДЕНИЯ СТРОК, ЗАВИСИМОСТИ ОТ № в ink НЕТ)
"""
from colorama import init
init()
from colorama import Fore, Back, Style

# Два массива, имеющие общие элементы
file = input('Введите путь к файлу для проверки #1:').strip('"')
file = open(f'{file}', 'r', encoding='utf-8')
file = file.read() #готовая переменная для проверки
file = file.split('\n') #разбитие file на отдельные строки -> class list
file = [line.strip() for line in file] #разбитые строки проверить и удалить пробелы
print('Количество строк в файле =', len(file))
file2 = input('Введите путь к файлу для проверки #2:').strip('"')
file2 = open(f'{file2}', 'r', encoding='utf-8')
file2 = file2.read() #готовая переменная для проверки
file2 = file2.split('\n') #разбитие file на отдельные строки -> class list
file2 = [line.strip() for line in file2] #разбитые строки проверить и удалить пробелы
print('Количество строк в файле =', len(file2))

# лямбда с использованием filter() для поиска общих значений
def interSection(file, file2): # find identical elements
   out = list(filter(lambda it: it in file, file2))
   return out
# функция main
if __name__ == "__main__":
   out = interSection(file, file2)
   print("Отфильтрованный список:", out)
out_str = out[:] # копия списка
out_str = list(filter(None, out_str)) # удалить пустые строки
print("Отфильтрованный список без пустых строк:", out_str)
out_str = list(filter(lambda it: it.startswith('//') == False, out_str))  #удалить комменты
out_str = list(filter(lambda it: it.startswith('CMD') == False, out_str))  #удалить команды
out_str = list(filter(lambda it: it.startswith('-') == False, out_str))  #удалить разделители
out_str = list(filter(lambda it: it.startswith('=') == False, out_str))  #удалить разделители сессий
out_str = list(filter(lambda it: it.startswith('Player: {') == False, out_str))  #удалить эмоджи Player
out_str = list(filter(lambda it: it.startswith('NPC: {') == False, out_str))  #удалить эмоджи NPC
out_str = list(filter(lambda it: it.startswith('INCLUDE') == False, out_str))  #удалить GlobalVariables
print("Отфильтрованный список без синтаксиса inka:", out_str)
if len(out_str) == 0:
   print(Fore.GREEN + "Тест пройден успешно: общих текстовых элементов не обнаружено")
else:
   print(Fore.RED + 'Тестом обнаружены общие элементы: ' + Style.RESET_ALL)
   for i, item in enumerate(out_str, 1):
      # print(i, item)
      print(i, item, Fore.YELLOW + 'Cтрока:', [file.index(item) + 1], '' + Style.RESET_ALL)
      # print(Fore.YELLOW + 'Cтрока: ', [file2.index(item) + 1], '' + Style.RESET_ALL, i, item)



# цикл для вывода списка с нумерацией (пропуская пустые строки/комменты/разделители)
# for i, item in enumerate(out, 1):
#       if item == '':
#          continue
#       elif item == '//Free choice' or item == '//Free choice:':
#          continue
#       elif item == '//Paid choice' or item == '//Paid choice:':
#          continue
#       elif item == '-' or item == '--' or item == '---':
#          continue
#       else:
#          print(i, item)
