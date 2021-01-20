'''1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.'''
import time
from itertools import cycle as i_cycle

class TrafficLight:
    __colors = ('red','yellow','green')
    
    def __init__(self):
        self.__color = self.__colors[0]

    def running(self, signal):
        timer = (7, 2, signal)
        for el in i_cycle(zip(self.__colors, timer)):
            print(el)
            self.__color = el[0]
            sec = el[1]
            print(self.__color)
            time.sleep(sec)
