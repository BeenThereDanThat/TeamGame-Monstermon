import time
from character import Character
from Damola import slow_print


class Water_Elemental(Character):
    def __init__(self, name, health, max_health, status, is_alive, pet_level, pet_exp, is_evolved, element, skills, evolution):
        super().__init__(name, health, max_health, status, is_alive, pet_level, pet_exp, is_evolved, element, skills, evolution)
        self.element = "water"
        self.skills = {}
        self.skills["Hydrosoak"] = self.hydrosoak


    def get_element(self):
      return self.element
    
    def set_element(self, element):
      self.element = element

    def hydrosoak(self, opponent):
      damage = (opponent.health * 0.15)
      effective_string, damage = self.effectiveness(opponent, damage)
      damage = round(damage, 2)
      heal = damage
      opponent.health -= damage
      self.health += heal
      
      slow_print(f"\n{self.name} used Hydrosoak on {opponent.name} ")
      slow_print(f"\nHydrosoak dealt {damage} damage and healed {self.name} for {heal} hp\n")
      slow_print(effective_string)
      time.sleep(0.5)