'''4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.'''

def input_integer():
    # Проверяет ввод, возвращает введенное число 
    # Дает возможность повторить ввод при ошибке
    while True:
        _input = input('\nEnter a number:\n')   
        if _input.isdigit():
            _input = int(_input)
            return _input
        else:
            print('Error! signature you have typed is not a number!')

user_num = input_integer()
result = 0
while user_num and result != 9:
    tmp = user_num % 10
    if tmp > result:
        result = tmp
    user_num //= 10

print(result)
