'''5) Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.'''

import re  # regular expressions module

def numbers_from_string(user_string = ""):
    '''Returns numbers found in string to list
    user_string: str'''  
    out = re.findall(r'\d+', user_string)
    return out

def summ_func(num_list):
    '''Return summ of elements in list
    num_list: list'''
    out = 0
    for el in num_list:
        out += int(el)
    return out

def exit_flag_fc(user_string, spc_char = 'x'):
    '''Returns -1 if spc_char not found in string , or index of result'''  
    flag = user_string.find(spc_char)
    return flag

exit_flag = -1
final_summ = 0

while exit_flag == -1:
    user_string = input("enter nums useing space, and/or 'x' to exit)")
    tmp_list = numbers_from_string(user_string)
    final_summ = final_summ + summ_func(tmp_list)
    print(f'final_summ {final_summ}')
    exit_flag = exit_flag_fc(user_string)

input('ok _>')
