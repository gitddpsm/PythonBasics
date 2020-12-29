'''
lect 4 task 1
'''

from sys import argv

_, hour, price, bonus, *__ = argv

try:
    result = float(hour) * float(price) + float(bonus)
    print(result)
except ValueError as e:
    print('Ошибка ввода')
    print(e)
