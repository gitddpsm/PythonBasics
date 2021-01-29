'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
'''
import os

file_name = 'employers_data.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)

with open(file_path, 'r',encoding='UTF=8') as file:
    file_data = file.read().split()

work_dict = {item : int(file_data[index + 1]) for index, item in enumerate(file_data) if index % 2 == 0}

# Фамилии сотрудников с окладом менее 20000
print([key for key, value in work_dict.items() if any(value < 20000 for element in work_dict.values())])

# Средняя ЗП 
value_list = [value for key, value in work_dict.items()]
print(sum(value_list) // len(value_list))
