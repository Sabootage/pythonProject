my_list = ['Alexander', 'Nikolai', 'Ksenia', 'Ekaterina']
a = str(input('Hello, What is your name? '))
b = str(input('Are you work in SWAGMASHA? '))
if a == my_list[0]:
    print('Hi, ', a, ' You are MOLODCHAGA!')
elif a == my_list[1]:
    print('Hi, ', a, ' You are MOLODCHAGA!')
elif a == my_list[2]:
    print('Hi, ', a, ' You are MOLODCHAGA!')
elif a == my_list[3]:
    print('Hi, ', a, ' You are MOLODCHAGA!')
else:
    print('You are not work in SWAGMASHA,', a)
if b == 'Yes' or b == 'yes' and a == my_list[0]:
    print('Relase on Friday!:)')
elif b == 'Yes' or b == 'yes' and a == my_list[1]:
    print('Relase on Friday!:)')
elif b == 'Yes' or b == 'yes' and a == my_list[2]:
    print('Relase on Friday!:)')
elif b == 'Yes' or b == 'yes' and a == my_list[3]:
    print('Relase on Friday!:)')
else:
    print('You are not work in SWAGMASHA', a)
input('Нажмите Enter для выхода\n')