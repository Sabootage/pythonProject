# Проверка соответствия текста в файле
search = 'INCLUDE' #устанавливаем переменную для поиска текста
f = open('E:/SM/TinderSim_InkChapters/ADRENALINE/CS/ADRENALINE_CH01_CS.ink', 'r', encoding='utf-8')
#устанавливаем переменную для открытия файл по пути с кодировкой
a = f.read() #устанавливаем переменную чтения файла
print(a) #выводим содержимое файла
b = a.find(search) #устанавливаем переменную для поиска
print(b)




