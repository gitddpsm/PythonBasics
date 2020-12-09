'''2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.'''

time_input = int(input("Введите время в секундах:"))
hours = time_input // 3600  # получаем количество_часов(hours) - 
minutes = (time_input - hours * 3600) // 60  # получаем количество_минут 
seconds = time_input - hours * 3600 - minutes * 60  #получаем секунды

def int_to_time(a):
    '''добавляем 0 если значение аргумента 1 символ '''    
    if len(str(a)) < 2:
        a = "0" + str(a)
    return a  

print(f'{int_to_time(hours)}:{int_to_time(minutes)}:{int_to_time(seconds)}')  #Вывод результата
