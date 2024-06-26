# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
     # периметр квадрата, площадь квадрата и диагональ квадрата.

def square(x):
    return x*4, x**2, x*2
print(tuple(square(5)))

# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
def f(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
f(name='John', last_name='Smith', age=35, position='web developer')

# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
my_list = [20, -3, 15, 2, -1, -21]
new_list = list(filter(lambda x: x > 0, my_list))
print(new_list)

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке (my_list)
from functools import reduce
result_list = reduce(lambda x, y: x * y, new_list)
print(result_list)

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
import time
def count_execution_time(func):
    def wrapper(*args):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        exec_time = end - start
        print(f'{func.__name__} execution time is: {exec_time}')
        return result
    return wrapper
@count_execution_time
def greeting(name):
    return f'Hello {name}!'
greeting('Alex')

# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.

#из файла Lesson_1.py импортировать функцию calc
from Lesson_1 import calc
def func (calc):
    return calc


