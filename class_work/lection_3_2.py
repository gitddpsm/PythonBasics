
def is_some(number: int, count: int) -> bool:
    '''Функция возвращает результат проверки является ли число n разрядным
    :number: int число
    :count: int количество разрядов
    :return:  bool: 
    '''
    return 1 <= (number // 10 ** (count -1)) < 10

b = {24323, 5}

print(is_some(*b))

a = {
    'count': 5,
    'number': 234,
}

print(is_some(**a))

print(is_some(number=5,count=235))
print(is_some(count=2256,number=5))

'''
zip
map
'''

def dd_map(func, iter_obj):
    '''Map this shit'''
    for item in iter_obj:
        yield func(item)

a = dd_map(str, [1, 2, 3, 4, 5])

print(a)

def dd_sum(*stuff):
    result = 0
    for n in stuff:
        result += n
    return result

print(dd_sum(1, 2, 3, 4,5))

def dd_sum_2(*stuff, factor=1):
    print('factor ', factor)
    result = 0
    for n in stuff:
        result += n
    return result * factor

print(dd_sum_2(1, 2, 3, 4, 5, factor=5))

def dd_sum_3(*stuff, **kwargs):
    print('kwargs ', kwargs)
    print(stuff)
    result = 0
    for n in stuff:
        result += n
    return result  

print(dd_sum_3(1, 2, 3, 4, 5, factor=562))

a = 1
b = 10

c = []

for n in range(a, b+1):
    c.append(n**2)
print(c)

d = [n**2 for n in range(a, b+1)]
print(d)

list_a = [1, 2, 3, 4, 5]
list_b = [100, 200, 300, 400, 500]

list_combinations = [(n_a, n_b) for n_a in list_a for n_b in list_b]

print(list_combinations)
print(list_combinations[2])

#result = {1: 1 ** 2, 2: 2**2}
list_result = {n: n ** 2 for n in list_a}
print(list_result)

list_result = {n: n ** 2 for n in list_a if n & 1}
print(list_result)

list_result = {n: n ** 2 for n in list_a if not n & 1}
print(list_result)

list_result = tuple( n ** 2 for n in list_a if n & 1)
print(list_result)

list_result = tuple( n ** 2 for n in list_a if not n & 1)
print(list_result)

'''result = []
for n_a in list_a:
    for n_b in list_b:'''
