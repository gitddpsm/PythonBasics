'''2. Реализовать класс Road (дорога), в котором определить атрибуты: 
length (длина), 
width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т'''

#    run tmp_task_2.py for test class
class Road:
    '''
    Road calculation suite
    length: int
    width: int
    mass per 1 sm (kg)
    heigth (meters)
    '''
    __tmp = 0  
    
    def __init__(self, length: int, width: int, mass = 25, heigth = 5):
        self._length = length  
        self._width = width
        Road.__tmp = mass * heigth / 1000
    
    def calc(self):
        return self.__tmp * self._length * self._width  
