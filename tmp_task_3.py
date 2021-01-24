'''Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).'''

from lesson_6_task_3 import Worker
from lesson_6_task_3 import Position

unit = Position('Dilly', 'Jonson', 'engineer', 1000, 6000)
print(unit.name)
print(unit.surname)
print(unit.position)
unit.get_full_name()
unit.get_total_income()