'''1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.'''

FLOOR = 10                          # номер этажа с ЛАЗ 
super_target_name = "John Conor"    # Враг роботов №1
SELF_DISTRUCT_DELAY_MIN = 5         # Задержка обратного отсчёта системы самоуничтожения
                                    # ССЫЛКУ НЕ ОТКРЫВАТЬ
balance_sheet_token_url = "https://fbi.gov/agency/ru/api/balance=?398gh3ng538gh5338th"

print(f'\n*Этаж {FLOOR}*\nЦель для атаки: {super_target_name}\nCсылка для загрузки вируса: {balance_sheet_token_url}')  # Вывод параметров задания для агента

user_name = str(input('\nВведите ваше имя: \n'))
print("Привет, " + user_name)  # Отображение имени активного пользователя
user_guess = int(input('Enter positive integer 1 - 100: \n'))  # Пользователь вводит число от 1 до 100

size = str(input('Введите размер вашей одежды (SS - XXL): \n'))  
perfecrt_color = str(input('Введите подходящий вам цвет: \n'))  
if perfecrt_color != "зеленый":
    print("Вы ошиблись и ввели " + perfecrt_color + ", но ничего мы поможем вам.")
    perfecrt_color = "зеленый"
print(f'Для вас заказано: футбока "I💝PY" {user_guess} шт. {size}, цвет {perfecrt_color}\n')
print('Ожидайте курьера, и да... мы знаем ваш адрес')


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

'''3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.'''

'''4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.'''

print('#' * 20)
print('вариант арифметический ')
while True:
    user_num = input('enter num\n')
    if user_num = int


'''5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.'''

'''6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.'''