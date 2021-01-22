'''5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''
class Stationery:
    ''' (канцелярская принадлежность). '''
    def __init__(self, title = 'default'):
        self.title = title
    def draw(self):
        '''(отрисовка). Метод выводит сообщение “Запуск отрисовки.” '''
        print("“Запуск отрисовки.”")
    
        
#Создать три дочерних класса 
class Pen(Stationery): 
    '''(ручка) 
    переопределение метода draw.    '''
    def __init__(self):
        super().__init__('pen')
    def draw(self, item:str = 'текст'):
        print(f" {self.title} написан {item} ”")

class Pencil(Stationery): 
    '''(карандаш) '''
    def __init__(self):
        super().__init__('pencil')
    def draw(self):
        print(f" item 3 = {self.title} ”")

class Handle(Stationery): 
    ''' (маркер) '''
    def __init__(self):
        super().__init__('маркер')
    def draw(self):
        print(f" item 3 = {self.title} ”")
        
'''        Создать экземпляры классов и проверить, 
        что выведет описанный метод для каждого экземпляра.'''

stationery = Stationery()
stationery.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()

handle.draw() 
pen.draw('test text for pen')
'''
'''