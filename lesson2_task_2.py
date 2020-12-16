"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
#a_list = [0, 3, 0.2,"3213",4,True,6,7,8] # заполнение через input().
"""

a_list = []
for i in range(int(input("Задайте количество элементов: "))):
    a_list.append(input())

print('=' * 30)
last_el = None


if len( a_list )% 2 != 0:
    last_el = a_list.pop(len(a_list) - 1)

el = 0
while el < len(a_list) -1:
    a_list[el], a_list[el + 1] = a_list[el + 1], a_list[el]
    el +=2


if last_el != None:
    a_list.append(last_el)

print(a_list)
