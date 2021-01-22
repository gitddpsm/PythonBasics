'''3. Реализовать базовый класс 
Worker (работник), 
атрибуты: name, surname, position (должность), 
_income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, 
{
    "wage": wage, 
    "bonus": bonus
}. 
Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы:
(get_full_name) получения полного имени сотрудника
(get_total_income) дохода с учетом премии. 
'''
#    run tmp_task_3.py for test class

class Worker:
    ''' from dawn till dusk '''
    
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus
        }

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super(Position, self).__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(self.name , ' ', self.surname)

    def get_total_income(self):
        print(self._income['wage'], ' ', self._income['bonus'])

