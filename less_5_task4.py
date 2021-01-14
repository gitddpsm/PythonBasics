'''4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.'''

import os

file_full_path = os.path.join(os.path.dirname(__file__), 'digits_spelling.txt')
mfile_full_path = os.path.join(os.path.dirname(__file__), 'modyfied_spelling.txt')

replace_cheme = {
    'One' : 'Один',
    'Two' : 'Два',
    'Three' : 'Три',
    'Four' : 'Четыре'
}

write_line = ''
with open(mfile_full_path, 'w', encoding='UTF-8') as file_out:
    print('Clear out File')

with open(file_full_path, 'r', encoding='UTF-8') as file_in:
    for line in file_in:
        in_line = line.replace('\n', '').split(' — ')
        for element in in_line:
            try:
                if element != any(replace_cheme.keys()):
                    write_line += replace_cheme[element] + ' — '
            except KeyError:
                write_line += element + '\n'
                with open(mfile_full_path, 'a', encoding='UTF-8') as file_out:
                    file_out.writelines(write_line)
                    write_line = ''
