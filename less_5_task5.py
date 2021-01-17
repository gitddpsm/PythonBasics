'''5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

from random import randint
from os import path

file_path = path.join(path.dirname(__file__), 'generated')

number_list = [randint(1, 20) for i in range(randint(5,10))]
nums_string = ' '.join(str(el) for el in number_list)

with open(file_path, 'w', encoding='UTF-8') as file:
    file.writelines(nums_string)

summ = 0    
with open(file_path, 'r') as file:
    for line in file:
        for x in line.split(' '):
           summ += int(x)
print(summ)
