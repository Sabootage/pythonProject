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
def count_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result
    return wrapper


# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.


