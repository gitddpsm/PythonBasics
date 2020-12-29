'''1) Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''

def divider(a: int, b:int):  # -> int:
    try:
        result = a // b
    except ZeroDivisionError:
        print(f' Ошибка деления на 0 ')
        result = str('Nan')
    return result

def user_input():
    while True:
        user_input = input('iput int:\n>')
        if user_input.isdigit():
            user_input = int(user_input)
            return user_input
        elif user_input == 'x':
            print('enter canceled\n 0 set by default')
            return 0            
        else:
            print('Not a number, type "x" for cancel:')
   
output_divider = divider(user_input(), user_input())

input(f'Результат = {output_divider}\n>ok')
