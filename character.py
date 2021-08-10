import time
from player import Player


class Character(Player):
    def __init__(self, name, health, max_health, status, is_alive, pet_level, pet_exp, is_evolved, element, skills, evolution):
        super().__init__(name, health, status)
        self.hit_chance = 10
        self.is_alive = is_alive
        self.pet_level = pet_level
        self.pet_exp = pet_exp
        self.is_evolved = is_evolved
        self.max_health = max_health
        self.element = ""
        self.burn_applied = 0
        self.species = ""

    def get_is_alive(self):
        return self.is_alive

    def get_pet_level(self):
        return self.pet_level

    def get_pet_exp(self):
        return self.pet_exp

    def get_is_evolved(self):
        return self.is_evolved

    def get_max_health(self):
        return self.max_health

    def get_hit_chance(self):
        return self.hit_chance

    def get_element(self):
      return self.element

    def get_skills(self):
      return self.skills

    def get_species(self):
      return self.species

    def set_species(self, species):
      self.species = species

    def set_skills(self, skills):
      self.skills = skills

    def set_is_alive(self, is_alive):
        self.is_alive = is_alive
    
    def set_pet_level(self, pet_level):
        self.pet_level = pet_level

    def set_pet_exp(self, pet_exp):
        self.pet_exp = pet_exp

    def set_is_evolved(self, is_evolved):
        self.is_evolved = is_evolved

    def set_max_health(self, max_health):
        self.max_health = max_health
    
    def set_element(self, element):
      self.element = element
    
    def set_hit_chance(self):
      if "intimidated" in self.status:
        self.hit_chance = 30
      else:
        self.hit_chance = 10

    def dead(self):
      print(f"\n{self.name} has fainted!\n")
      time.sleep(2)

    def effectiveness(self, opponent, damage):
      elements = ["fire", "water", "earth"]
      for i,t in enumerate(elements):
        if self.element == t:

          if opponent.element == t:
            damage = damage * 1
            effective_string = "It had normal effectiveness.\n"
          
          elif opponent.element == elements[(i + 1) % 3]:
            damage *= 0.75
            effective_string = "It wasn't very effective...\n"
          
          elif opponent.element == elements[(i + 2) % 3]:
            damage *= 1.25
            effective_string = "It was super effective!\n"
            
      return effective_string, damage