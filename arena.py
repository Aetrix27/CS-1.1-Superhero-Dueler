from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = input(
            "What is the max damage of the ability?  ")

        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        max_damage = input("What is the max damage?")
        name = input("What is the name of the weapon?")

        return Weapon(name, max_damage)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        name = input("What is the name?")
        max_block = input("What is the max block?")

        return Armor(name, max_block)
    
    def create_hero(self):
        '''Prompt user for Hero information
        return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                created_ability = self.create_ability()
                hero.add_ability(created_ability)
            elif add_item == "2":
                created_weapon = self.create_weapon()
                hero.add_weapon(created_weapon)
            elif add_item == "3":
                created_armor = self.create_armor()
                hero.add_armor(created_armor)
            return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)
        self.team_two.attack(self.team_one)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        t1_alive_count = 0
        t2_alive_count = 0
        t1_kills = 0
        t1_deaths = 0
        t2_kills = 0
        t2_deaths = 0

        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        for hero in self.team_one.heroes:
            t1_kills += hero.kills
            t1_deaths += hero.deaths
        if t1_deaths == 0:
            t1_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(t1_kills/t1_deaths))

        for hero in self.team_two.heroes:
            t2_kills += hero.kills
            t2_deaths += hero.deaths
        if t2_deaths == 0:
            t2_deaths = 1

        print(self.team_one.name + " average K/D was: " + str(t2_kills/t2_deaths))

        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)
       
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)
        

        if(t1_alive_count > t2_alive_count):
            print("t1 wins!")
        elif(t1_alive_count > t2_alive_count):
            print("t2 wins!")
        else:
            print("There is a draw between t1 and t2!")

        
if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()