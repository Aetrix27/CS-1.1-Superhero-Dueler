#animal.py
class Animal:
  def __init__(self, name):
    self.name = name

  def eat(self):
    print('{} is eating'.format(self.name))

  def drink(self):
    print('{} is drinking'.format(self.name))

class Frog(Animal):
    def jump(self):
        print('{} is jumping'.format(self.name))

my_animal = Animal('Bell')
my_frog = Frog('Froggy')
my_frog.eat()
my_frog.drink()
my_frog.jump()
my_animal.eat()
my_animal.drink()