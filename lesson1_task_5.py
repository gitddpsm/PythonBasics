'''UNDER CONSTRUCTION'''
'''5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.'''

def input_integer():
    # Проверяет ввод, возвращает введенное число 
    # Дает возможность повторить ввод при ошибке
    while True:
        _input = input()   
        if _input.isdigit():
            _input = int(_input)
            return _input
        else:
            print('Error! signature you have typed is not a number!\n')

print('\nУкажите объем выручки:')
revenue = input_integer()                         # Выручка
print('\nУкажите объем издержек:')
cost = input_integer()                            # Издержки
profit = revenue - cost                           # Прибыль = выручка - издержки

if revenue < cost:
    print('\nУбыток — издержки больше')
else:
    print('\nПрибыль — выручка больше издержек')  # Рентабельность = выручка/прибыль
    profitability = revenue / profit              # Запрос числа сотрудников
    print('\nУкажите количество сотрудников:')
    staff = input_integer()

'''  (Вычислить) прибыль на 1 сотрудника = прибыль / число сотрудников '''
print("На одного сотрудника прибыль составляет")
print(str(round(profit / staff, 2)) + " у.е.\n")
print(f'#DBG рентабельность = {profitability}')
