'''3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.'''

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

count = 0
tmp = user_input = 3 # input_integer()

while tmp:  # Пока tmp True, то есть больше нуля
    # tmp = tmp // 10
    # Как только при отделении остатка от числа tmp доходит до 0 оно выдаёт False и цикл прекращается (🤯)
    tmp //= 10
    count += 1

nn_div = 10 ** count + 1
nnn_div = (10 ** (count * 2)) + nn_div

result = user_input + (user_input * nn_div) + (user_input * nnn_div)
print(f"Cумма чисел n + nn + nnn  = {result}")
