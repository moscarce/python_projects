class Flyer:
    def fly(self,dog):
        dog.fly()

class Bird:
    def fly(self):
        print('Flying')

class Chicken:
    def fly(self):
        print('Chicken flying')



flyer1 = Flyer()
bird1 = Bird()
chicken1 = Chicken()

flyer1.fly(bird1)
flyer1.fly(chicken1)