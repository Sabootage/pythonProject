# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре. Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
health = int(input('Здоровье: '))
if health <= 0:
    print('False')
else:
    print('True')

# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным. Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”
number = int(input('Введите число: '))
if number % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600). Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)
year = int(input('Enter year: '))
if year%4 == 0 and year%100 != 0 or year%400 == 0:
    print('Високосный')
else:
    print('Не високосный')
# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно. Текст и количество повторений нужно ввести с помощью input()
text = input('Enter text: ')
count = int(input('Enter count: '))
for i in range(count):
    print(text)
# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str), производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}
num1 = int(input('Введите 1-ое число: '))
num2 = int(input('Введите 2-ое число: '))
operator = str(input('Введите требуемое арифметическое действие: '))
if operator == '+':
     result = num1 + num2
     print(f'{num1} {operator} {num2} = {result}')
elif operator == '-':
     result = num1 - num2
     print(f'{num1} {operator} {num2} = {result}')
elif operator == '*':
     result = num1 * num2
     print(f'{num1} {operator} {num2} = {result}')
elif operator == '/':
     if num2 != 0:
         result = num1 / num2
         print(f'{num1} {operator} {num2} = {result}')
     else:
         print('Деление на ноль невозможно')
else:
     print('Введеное неверное значение')

# ВАРИАНТ №2
try:
     if operator == '+':
         print(num1 + num2)
     elif operator == '-':
         print(num1 - num2)
     elif operator == '*':
         print(num1 * num2)
     elif operator == '/':
         print(num1 / num2)
except ZeroDivisionError:
     print('Деление на ноль невозможно')



