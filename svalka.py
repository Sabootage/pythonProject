# импорт модуля SWAGMASHA для открытия файла
# from SWAGMASHA import SM_open_file
# print(SM_open_file)

def count_agtc(dna):
    a = dna.count('A')
    t = dna.count('T')
    g = dna.count('G')
    c = dna.count('C')
    return a, t, g, c
print(count_agtc("AGCTGACGTAC"))

def is_palindrome(text):
    text1 = text.lower()
    text2 = ''
    for char in text1:
        if char.isalpha():
            text2 += char
    return text2 == text2[::-1] #полученный text2 равен перевернутому text2

text = 'А роза упала на лапу Азора'
print(is_palindrome(text))

starts_with = lambda text, start: text.startswith(start)
def starts_with(text, start):
    return text.startswith(start)

starts_with = lambda text: text.startswith('W')
result = starts_with('World')
print(result)
def starts_with(text: str):
    return text.startswith('W')

func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False
print(func(19))

#сортировка по длине и алфавиту
data = ['1', '12', '123', '1234', '12345', '123456', '1234567', '12345678', '123456789', '1', '12', '123']
data2 = ['цйу', 'ыва', 'йцу', 'ячс', 'ывавып', 'ывапкп', 'гонг', 'мит', 'огл',]
sorted_dat = sorted(data, key=lambda x: len(x)) #по возрастанию
# sorted_dat = sorted(data, key=lambda x: -len(x)) #по убыванию
sorted_dat2 = sorted(data2, key=lambda x: (len(x), x)) #по длине, алфавиту
print(sorted_dat)
print(sorted_dat2)


def text_decor(func):
    def dec(*args, **kwargs):
        print('Hello')
        func(*args, **kwargs)
        print('Goodbye')
    return dec
@text_decor
def simple_func():
    print('I just simple python function')
simple_func()