'''3) Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.'''

def my_func(a,b,c):
    my_list = sorted([a, b, c])
    #print(sum(my_list[-2:]))
    return sum(my_list[-2:])

print(my_func(5, 1 ,2))
