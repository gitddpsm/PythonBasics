'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.'''

with open("task2_file", 'r') as f_obj:
    input_list = []
    line_num = 0
    for line in f_obj:
        line_num += 1
        print(f' in line {line_num}: {len(line.split())} words')
        input_list.append(line.replace('\n', '')) 
    f_obj.close()
    print(f'{len(input_list)} lines in file\n')
