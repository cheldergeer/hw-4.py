1
class Vehicle:
def __init__(self, max_speed, mileage):
self.max_peed = max_speed
self.mileage = mileage

2
class Bus(Vehicle):
 def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)
        
        def seating_capacity(self):
 print('seating_capacity method')

3
print(type(Bus))

Bus_obj = Bus(100, 100)
print(type(Bus_obj))

4
School_bus = Bus(140, 1000)
print(isinstance(School_bus, Venicle))
print(issubclass(Bus, Venicle))


5
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students
        
        class SchoolBus(School, Bus):
    def bus_school_color(self):
        print('bus_school_color method')
        
        6
        Sch_bus = SchoolBus(12, 400)
Sch_bus.seating_capacity()
Sch_bus.bus_school_color()


7

class Bear:
    def __init__(self, name):
        self.name = name
        
        
        
        def make_sound(self, sound=''):
        print(f"{self.name} sound is ")
        if not sound:
            print('Roaar')
        else:
            print(sound)
            
            
            
            
            class Wolf:
    def __init__(self, name):
        self.name = name
        
        
        
         def make_sound(self, sound=''):
        print(f"{self.name} sound is ")
        if not sound:
            print('Owooo')
        else:
            print(sound)
            
            
            
            winnie_pooh = Bear('Winnie')
grey_wolf = Wolf('Grey')

for animal in (winnie_pooh, grey_wolf):
    animal.make_sound()
    animal.make_sound('Aaaa')
    
    
    
    8
    class City():
    def __new__(cls, name, population):
        if population > 1500:
            return super().__new__(cls)
        else:
            return print("Your city is too small")

    def __init__(self, name, population):
        self.name = name
        self.population = population


A_ins = City('Kovel', 600)



9

class City:
    def __new__(cls, name, population):
        if population > 1500:
            return super().__new__(cls)
        else:
            return print("Your city is too small")

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        return f"The population of the city {self.name} is {self.population}"


City1 = City('Kovel', 10560)
print(City1)




10

class Add:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
       if self.number > 10 or other.number > 10:
            self.number *= other.number
       return self.number + other.number

a = Add(45)
b = Add(2)
print(f"result = {a+b}")
#result = 92
a = Add(5)
b = Add(2)
print(f"result = {a+b}")


11
class CallSumm:
    def __call__(self, a, b):
        return a + b


call1 = CallSumm()
print("Result = ", call1(12, 13))



12
class MyOrder:
    def __init__(self, card, customer):
        self.card = card
        self.customer = customer

    def __bool__(self):
        return len(self.card) > 0

order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
#True
print(bool(order_2))
#False
