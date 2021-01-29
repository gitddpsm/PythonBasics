'''6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}'''

from random import randint
from os import path

file_content = {}
with open(path.join(path.dirname(__file__), 'learn_plan'), 'r', encoding='UTF-8') as file:
    for line in file:
        line_content = line.split(':')
        file_content[line_content[0]] = line_content[1].split()

output_dict = {}
for key,value in file_content.items():
    output_dict[key] = 0
    for item in value:
        try:
            output_dict[key] += int(item.split('(')[0])
        except ValueError:
            continue    

print(output_dict) 
                 