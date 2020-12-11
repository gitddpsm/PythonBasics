''' DRY '''
'''
'''

def is_some(number: int, count: int) -> bool:
    '''Функция возвращает результат проверки является ли число n разрядным
    :number: int число
    :count: int количество разрядов
    :return:  bool: 
    '''
    return 1 <= (number // 10 ** (count -1)) < 10

a: bool = is_some(123, 3)   #аннотация
b: float = is_some(123, 4)  #аннотация не влияет на выполнение
c = is_some(12, 5)
d = is_some(124523446, 6)

print(a, b, c, d)
print(any((a, b, c, d)))
print(all((a, b, c, d)))
#

def some(number):
    # как использовать Степень делимого для определения условия ?
    '''
    >>> some(34235253)
    NO
    >>> some(53)
    NO
    >>> some(353)
    YES
    '''
    answer = ('NO','YES')
    print(answer[1 <= (number // 100) < 10])

some(353)