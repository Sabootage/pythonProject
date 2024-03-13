# Замена текста в файле
a = 'NPC'#устанавливаем переменную для поиска текста
b = open('E:/SM/TinderSim_InkChapters/ADRENALINE/CS/ADRENALINE_CH01_CS.ink', 'r', encoding='utf-8')
#устанавливаем переменную для открытия файл по пути с кодировкой
c = b.read() #устанавливаем переменную чтения файла
print(c) #выводим содержимое файла
new_text = c.replace('NPC', 'Player') #устанавливаем переменную для замены текста
print(new_text)

