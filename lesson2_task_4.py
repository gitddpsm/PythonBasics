"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""
b = input()

b = b.split()
line = 0
for i in b:
    print(f'{line}: {i[:10]}')
    line += 1
