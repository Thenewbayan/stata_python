class Wheel:
    def __init__(self, size:int, brend:str, weather:str, brend_t:str=''):
        self.size=size
        self.brend=brend
        self.tyre=Tyre(weather, brend_t if brend_t else brend)

class Tyre:
    def __init__ (self, weather:str, brend:str):
        self.weather=weather
        self.brend=brend
    def __repr__(self) -> str:
        return f'{"letnay" if self.weather=="summer" else "winter"} brandname {self.brend}'

class Car:
    def __init__(self, mark:str, color:str, year:int, size_w:int=17, brend_w:int='Belshina'):
        self.mark=mark
        self.color=color
        self.year=year
        self.wheels=[Wheel(size_w, brend_w, 'summer'), 
                     Wheel(size_w, brend_w, 'summer'), 
                     Wheel(size_w, brend_w, 'summer'), 
                     Wheel(size_w, brend_w, 'summer')]
    def __str__(self):
        return f'ЬФшина марки {self.mark}, {self.color}, {self.year}'

    def horn(self):
        print(f' Машина {self.mark} delaet "bibibi"')


my_car=Car('MAzda', 'black', '2022')
my_car.horn()
new_car=Car('Tesla', 'red', '2023', 20, 'Michelin')
new_car.horn()
my_car.wheels[1].brend='Zapaska'
my_car.wheels[1].size=15

print(my_car.mark)
print(my_car.wheels[0].brend)

for wheel in my_car.wheels:
    print(wheel.size, wheel.brend, wheel.tyre)

print(my_car)



