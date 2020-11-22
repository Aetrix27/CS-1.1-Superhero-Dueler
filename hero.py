import random 
from ability import Ability
from armor import Armor

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          name: String
          starting_health: Integer
          current_health: Integer
        '''

        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health

    def fight(self, opponent):  
      ''' Current Hero will take turns fighting the opponent hero passed in.
      '''
      # TODO: Fight each hero until a victor emerges.
      # Phases to implement:
      # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
      if not self.abilities and not opponent.abilities:
        print("Draw")
      else:
        while opponent.is_alive() and self.is_alive():
          opponent.take_damage(self.attack())
          print(opponent.current_health)

          if self.is_alive() == False:
            print(f"{opponent.name} won!")
          elif opponent.is_alive() == False:
            print(f"{self.name} won!")

          self.take_damage(opponent.attack())

          if self.is_alive() == False:
            print(f"{opponent.name} won!")
          elif opponent.is_alive() == False:
            print(f"{self.name} won!")

      # 1) else, start the fighting loop until a hero has won
      # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
      # 3) After each attack, check if either the hero (self) or the opponent is alive
      # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
      
      
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
      # TODO: Add armor object that is passed in to `self.armors`

    def defend(self, damage_amt):
      '''Calculate the total block amount from all armor blocks.
        return: total_block:Int
      '''
      total_block = 0
      for armor in self.armors:
        total_block += armor.block()
      return total_block
      # TODO: This method should run the block method on each armor in self.armors

    def take_damage(self, damage):
      '''Updates self.current_health to reflect the damage minus the defense.
      '''
      self.current_health = damage - self.defend(damage)

      return self.current_health
      # TODO: Create a method that updates self.current_health to the current
      # minus the the amount returned from calling self.defend(damage).

    def is_alive(self):  
      '''Return True or False depending on whether the hero is alive or not.
      '''

      if self.current_health <= 0:
        return False
      elif self.current_health > 0:
        return True

      # TODO: Check the current_health of the hero.
      # if it is <= 0, then return False. Otherwise, they still have health
      # and are therefore alive, so return True


if __name__ == "__main__":

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