'''6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}'''

from random import randint
from os import path

file_content = []
with open(path.join(path.dirname(__file__), 'learn_plan'), 'r', encoding='UTF-8') as file:
    for line in file:
        file_content.append(line)
print(content)

'''
number_list = [randint(1, 20) for i in range(randint(5,10))]
nums_string = ' '.join(str(el) for el in number_list)


summ = 0    
with open(file_path, 'r') as file:
    for line in file:
        for x in line.split(' '):
           summ += int(x)
print(summ)
'''