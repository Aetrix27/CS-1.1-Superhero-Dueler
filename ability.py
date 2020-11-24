import random

class Ability:
    def __init__(self, name, max_damage):
        '''
       Initialize the values passed into this
       method as instance variables.
        '''
        self.name = name
        self.max_damage = max_damage

    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''
      random_value = random.randint(0, int(self.max_damage))
      return random_value
      
