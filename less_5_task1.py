'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.'''

text = []

def usr_input():
    while True:
        string = input('>')
        if string == '':
            break
        text.append(f'{string}\n')
        
usr_input()
print(text)

f = open("my_file", 'w')
f.writelines(text)
f.close()


with open("my_file", 'r') as f_obj:
    for line in f_obj:
        print(line)
