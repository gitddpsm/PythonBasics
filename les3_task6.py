'''6) Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. 
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().'''

def int_func(word):
    return word.title()
 
def mass_titles(words_string):
    tmp_list = words_string.split()
    out_str = ''
    for el in tmp_list:
        out_str = (f'{out_str} {int_func(el)}')
    return out_str


print(mass_titles('sdjfh sdkjhfkj dskjhf eqwrio qwp'))    


def int_func_exampl(string: str):
    return ''.join((string[0].upper(), string[1:])) if string else string

def user_temp(string: str):
    return ''.join(map(int_func_exampl, string.split('')))


assert int_func_exampl('') == '', "int_func('')"

input('ok >')
