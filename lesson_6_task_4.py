'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
'''

class Car:
    ''' My lovely car class '''
    _directions = ('L', 'R', 'Fw', 'Bw')
    
    def __init__(self, speed, color, name, is_police : bool ):
        self.speed = speed 
        self.color = color 
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} on run')

    def stop(self):
        print(f'{self.name} stoped')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} turning {self.direction} direction')
    
    def show_speed(self):
        print(f' Current speed {self.speed}')

vehicle = Car(100, 'red', 'tesla', False)

vehicle.go()
vehicle.stop()
vehicle.turn('left')

'''Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
'''

class TownCar(Car): 
    ''' TownCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)  должно выводиться сообщение о превышении скорости.'''
    def show_speed(self):
        if self.speed > 60:
            print(f'Warning speed > 60')
        super().show_speed()


class SportCar(Car):
    pass 


class WorkCar(Car): 
    '''WorkCar переопределите метод show_speed. При значении скорости 40 (WorkCar) должно выводиться сообщение о превышении скорости.'''
    def show_speed(self):
        print(f'Current speed {self.speed}')


class PoliceCar:
    def __init__(self,  is_police : bool ):
        self.speed = speed 
        self.color = color 
        self.name = name
        self.is_police = is_police
    