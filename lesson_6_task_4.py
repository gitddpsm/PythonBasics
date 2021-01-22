'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
'''

class Car:
    ''' My lovely car class
    self, name = 'noname', color = 'nocolor', speed :int  = 0, is_police :bool = False  '''
    
    def __init__(self, name = 'noname', color = 'nocolor', speed :int  = 0, is_police :bool = False ):
        self.speed = speed
        self.color = color 
        self.name = name
        self.is_police = is_police

    def go(self, speed :int = 15):
        print(f'{self.name} on run, speed up')
        self.speed += speed
        
    def stop(self):
        self.speed = 0
        print(f'{self.name} stoped')

    def turn(self, direction):
        if direction in ('left', 'right'): # ... , 'Fw', 'Bw')
            print(f'{self.name} goes {direction} direction')
        else:
            raise ValueError('values must be left or right')

    def show_speed(self):
        print(f'{self.name} current speed {self.speed}')


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
        if self.speed > 60:
            print(f'Warning speed > 60')
        super().show_speed()


class PoliceCar(Car):
    '''self, name, speed, is_police : bool = True'''
    def __init__(self, name, speed, is_police : bool = True ):
        self.is_police = is_police
        super().__init__(name, 'police color cheme', speed, True)

vehicle = Car('tesla', 'red', 110)

vehicle.go(70)
vehicle.turn('left')
vehicle.show_speed()
vehicle.stop()
vehicle.show_speed()

car1 = TownCar('Towncar', 'white' , 20)
car2 = SportCar('Sportcar', 'black')
car2.go()
car3 = WorkCar('WorkCar', 'yellow' )
car3.go(50)
car4 = PoliceCar('Sherif', 60)
print()

car1.show_speed()
car2.show_speed()
car3.show_speed()
car4.show_speed()
print()

car1.stop()
car1.go()
print()

print(f"Скорость {car2.name} = {car2.speed}")
car2.go()
print(f"Скорость {car2.name} = {car2.speed}")
car2.go(250)
print(f"Скорость {car2.name} = {car2.speed}")

print(f"{type(car4)} это машина полиции? {car4.is_police}")
print(f"{type(car1)} это машина полиции? {car1.is_police}")

vehicle.go()
vehicle.show_speed()