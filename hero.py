import random 
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          name: String
          starting_health: Integer
          current_health: Integer
        '''
        self.abilities = list()
        self.armors = list()
        
        self.name = name
        self.deaths = 0
        self.kills = 0
        self.starting_health = starting_health

        self.current_health = starting_health

    def fight(self, opponent):  
      ''' Current Hero will take turns fighting the opponent hero passed in.
      '''
      if self.abilities is not list() and opponent.abilities is not list():
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        if not self.is_alive() and not opponent.is_alive():
            print("Draw!")
        elif self.is_alive():
            print(self.name,"Wins!")
            self.add_kill(1)
            opponent.add_death(1)
            return 1
        else: 
            print (opponent.name,"Wins!")
            opponent.add_kill(1)
            self.add_death(1)
            return 2
      else:
        print("Draw!")
        return 3

    def add_ability(self, ability):
      ''' Add ability to abilities list '''

      # We use the append method to add ability objects to our list.
      self.abilities.append(ability)

    def attack(self):
      '''Calculate the total damage from all ability attacks.
          return: total_damage:Int
      '''

      # start our total out at 0
      total_damage = 0
        # loop through all of our hero's abilities
      for ability in self.abilities:
          # add the damage of each attack to our running total
          total_damage += ability.attack()
      # return the total damage
      return total_damage

    def add_armor(self, armor):
      '''Add armor to self.armors
        Armor: Armor Object
      '''
      self.armors.append(armor)
      return self.armors

    def defend(self):
      '''Calculate the total block amount from all armor blocks.
        return: total_block:Int
      '''
      total_block = 0
      for armor in self.armors:
        total_block += armor.block()
      return total_block

    def take_damage(self, damage):
      '''Updates self.current_health to reflect the damage minus the defense.
      '''
      self.current_health = self.current_health - damage

      return self.current_health
 

    def is_alive(self):  
      '''Return True or False depending on whether the hero is alive or not.
      '''
      if self.current_health <= 0:
        return False
      elif self.current_health > 0:
        return True

    def add_weapon(self, weapon):
      '''Add weapon to self.abilities'''
      self.abilities.append(weapon)

    def add_kill(self, num_kills):
      ''' Update self.kills by num_kills amount'''
      self.kills += num_kills
    
    def add_death(self, num_deaths):
      ''' Update deaths with num_deaths'''
      self.deaths += num_deaths
      
if __name__ == "__main__":

  hero1 = Hero("Grace Hopper", 200)
  hero1.take_damage(150)
  print(hero1.is_alive())
  hero1.take_damage(15000)
  print(hero1.is_alive())

  hero1 = Hero("Wonder Woman")
  hero2 = Hero("Dumbledore")
  ability1 = Ability("Super Speed", 300)
  ability2 = Ability("Super Eyes", 130)
  ability3 = Ability("Wizard Wand", 80)
  ability4 = Ability("Wizard Beard", 20)
  hero1.add_ability(ability1)
  hero1.add_ability(ability2)
  hero2.add_ability(ability3)
  hero2.add_ability(ability4)
  hero1.fight(hero2)

  hero = Hero("Wonder Woman")
  weapon = Weapon("Lasso of Truth", 90)
  hero.add_weapon(weapon)
  print(hero.attack())