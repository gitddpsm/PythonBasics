'''7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.

import os

'''

import os
import json

file_data_in = os.path.join(os.path.dirname(__file__), 'firm_data_in')
file_data_out = os.path.join(os.path.dirname(__file__), 'firm_data_out')
firm_data_all = {}
firm_data_positive = {}
sum_profit = 0

with open(file_data_in, 'r', encoding='UTF-8') as file_in:
    for line in file_in:
        line_parse = line.replace('\n','').split()
        profit = int(line_parse[2]) - int(line_parse[3])          
        firm_data_all[line_parse[0]] = profit
        if profit > 0:
            firm_data_positive[line_parse[0]] = profit          
            sum_profit += profit
            
a_profit ={
    'average profit': round(sum_profit / len(firm_data_positive), 2)
    }
#print(f" average profit: {a_profit.get('average profit')}")
with open(file_data_out, 'w', encoding='utf-8') as file_out:
    out_data = [firm_data_positive, a_profit]
    json.dump(out_data, file_out)
