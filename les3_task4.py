'''4) Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.'''

def my_func(x, y):
    outout = x ** y
    return outout

print(my_func(2, -2))

def fastExp(b, n):
    def even(n):  #проверка четности
        if n%2 == 0:
            return 1
        return 0
    if n == 0:
        return 1
    if even(n):
        return fastExp(b, n/2)**2
    return b*fastExp(b, n-1)

print(fastExp(2, 0))

def negative_exp(x, y):
    result = 1
    for el in range(abs(y)):
        result *= x
    if y >= 0:
        return result
    else: 
        return 1 / result

print(negative_exp(2, -2))
        
