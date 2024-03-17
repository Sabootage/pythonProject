# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
my_list = ['a', 'b', [1, 2, 3], 'd']
print(* my_list[2])

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
print(list_1[2] + list_1[3] + list_1[5] + list_1[6])
#    - распечатайте все строки, где есть буква 'a'
list_2 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
new_list2 = []
for x in list_2:
    if x == 'ananas' or x == 'pizza':
        new_list2.append(x)
print(new_list2)
# Вариант_2
list_3 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
new_list = []
for x in list_3:
    if isinstance(x, str) and 'a' in x:
        new_list.append(x)
print(new_list)
# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
list_4 = ['cat', 'dog', 'horse', 'cow']
new_tuple = tuple(list_4)
print(type(list_4))
print(type(new_tuple))

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
family1 = tuple(input('Enter family_1: ').split(','))
family2 = tuple(input('Enter family_2: ').split(','))
if len(family1) > len(family2):
    print('family1')
elif len(family1) < len(family2):
    print('family2')
else:
    print('Equal')

# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
film = {
    'title': 'my_film',
    'director': 'best_director',
    'year': '2012',
    'budget': '1000$',
    'main_actor': 'Tom Hardy',
    'slogan': 'best_slogan'
}
print(type(film))
print(film.keys())
print(film.values())
print(film.items())

# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum(my_dictionary.values()))
# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
my_list6 = [1, 2, 3, 4, 5, 3, 2, 1]
print(set(my_list6))
# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1.intersection(set2))