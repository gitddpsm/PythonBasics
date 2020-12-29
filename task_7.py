'''Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.'''


def fact(n):
    result = 1
    print("==fact1==")
    for num in range(1, n+1):
        result *= num
        yield result

gen = fact(7)
for idx, itm in enumerate(gen, 1):
    print(idx, itm)

def fact2(n):
    prev2 = 1
    result2 = 1
    print("--fact2--")
    while prev2 <= n:
        yield result2
        prev2 += 1
        result2 *= prev2

a = fact2(7)
for foo, bar in enumerate(a, 1):
    print(foo, bar)