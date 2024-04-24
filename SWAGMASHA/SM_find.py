from SWAGMASHA import SM_open_file #импорт модуля SM_open_file






# print('Привет, я помогу тебе в тестировании:)')
# file = input('Пожалуйста, введи путь к файлу, который ты хочешь проверить (пример: E:/SM/TinderSim_InkChapters/ADRENALINE/CS/ADRENALINE_CH01_CS.ink): ').strip('"')
# file2 = open(f'{file}', 'r', encoding='utf-8')
# file3 = file2.read()
# #print(file3) (что бы убедиться, что файл подгружен)
# find = input('Теперь введи текст для поиска: ') #переменная find - объект для поиска №1
# find2 = file3.count(find)
# print('Количество найденных объектов:', find2)
# find_new = input('Если хотите сравнить найденные объекты с объектами в этом же файле - введите второй объект для сравения. Если хотите сравнить с объектами из другого файла - напишите "Next": ')
# if find_new == 'Next':
#     file_new = input('Будет выполнен поиск по объектам из другого файла, пожалуйста, введите путь к файлу: ').split('"')[1]
#     file_new2 = open(f'{file_new}', 'r', encoding='utf-8')
#     file_new3 = file_new2.read()
#     find_new = file_new3.count(find)
#     print('Количество объектов в файле №2:', find_new)
#     if find_new == find2:
#         print('Здорово! Количество объектов в файлах не отличается :)')
#     else:
#         print('Хм..., количество сравниваемых объектов в файлах отличается, думаю стоит проверить файлы вручную')
# else:
#     find_new2 = file3.count(find)
#     print('Количество сравниваемых объектов в файле:', find_new2)
#     if find_new2 == find2:
#         print('Здорово! Количество объектов не отличается :)')
#     else:
#         print('Хм..., количество сравниваемых объектов в файле отличается, думаю стоит проверить файл вручную')
# input('Нажмите Enter для выхода\n')