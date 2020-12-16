"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

year_times_list: list = ['зима', 'весна', 'лето', 'осень']
year_times_dict = {
    0: 'зима',
    1: 'весна',
    2: 'лето',
    3: 'осень',
}

def range_limited_in():
    '''Проверяет введеные параметры в пределах 1 до 12'''
    while True:
        _input = input("\nВведите месяц в виде целого числа от 1 до 12:\n~ # ")
        if _input.isdigit():
            _input = int(_input)
            if 0 < _input < 13:
                return _input
    print("Ошибка: введены неверные параметры. Попробуйте еще раз!\n")
    
month = range_limited_in()

month = 0 if month == 12 else month  # если месяц 12 то месяц 0 иначе без изменений 

print("Используя список: " + year_times_list[month // 3])
print("Используя словарь: " + year_times_dict.get(month // 3))
