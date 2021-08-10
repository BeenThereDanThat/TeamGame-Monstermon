import time
from character import Character
from Damola import slow_print


class Earth_Elemental(Character):
    def __init__(self, name, health, max_health, status, is_alive, pet_level, pet_exp, is_evolved, element, skills, evolution):
        super().__init__(name, health, max_health, status, is_alive, pet_level, pet_exp, is_evolved, element, skills, evolution)
        self.element = "earth"
        self.skills = {}
        self.skills["Earthquake"] = self.earthquake


    def get_element(self):
      return self.element
    
    def set_element(self, element):
      self.element = element

    def earthquake(self, opponent):
      damage = (opponent.health * 0.3)
      opponent.update_status("trapped")
      effective_string, damage = self.effectiveness(opponent, damage)
      damage = round(damage, 2)
      opponent.health -= damage
      slow_print(f"\n{self.name} used Earthquake on {opponent.name}")
      slow_print(f"\nEarthquake dealt {damage} damage and trapped {opponent.name} in the ground for 1 round!\n")
      slow_print(effective_string)
      time.sleep(0.5)

    





