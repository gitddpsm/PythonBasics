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