"""
https://github.com/gitddpsm/PythonBasics/pull/8
"""
class VinCodeError(Exception):
    def __init__(self, txt):
        self.txt = txt

    @classmethod
    def vin_Validator(cls, vincode):
        if not isinstance(vincode, str):
            raise cls('Wrong vin type, need string')
        elif len(vincode) < 10:
            raise cls('Not correct vin length')
        return vincode
class Car:
    def __init__(self, name, vincode):
        self.name = name
        self.vincode = VinCodeError.vin_Validator(vincode)

if __name__ == '__main__':
    try:
        car1 = Car('name1', '12')
    except VinCodeError:
        print('create a new car')
        car1= Car('Name', 'dasd123afaf')

    print(car1.name)
    print(car1.vincode)
