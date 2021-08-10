import random
from Water_elemental import Water_Elemental
from random import randint
from Damola import slow_print

class Angry_Hosepipe(Water_Elemental):
  def __init__(self, name, health, max_health, status, is_alive, pet_level, pet_exp, is_evolved, element, skills, evolution):
    super().__init__(name, health, max_health, status, is_alive, pet_level, pet_exp, is_evolved, element, skills, evolution)
    self.species = "Angry Hosepipe"
    self.element = element
    self.skills["Sonic Sonar"] = self.sonic_sonar
    self.skills["Whirlpool"] = self.whirlpool
    self.skills["Tidal Wave"] = self.tidal_wave
    self.evolution = "Livid Sea Snake"      
  


    
    
  
  def sonic_sonar(self, opponent):
    success_rate = randint(50,100)
    damage = random.randint(2, 6)
    opponent.health -= damage
    if success_rate > self.hit_chance:
      slow_print(f"\n{self.name} used Sonic sonic_sonar on {opponent.name}\nDealing {damage} Damage")
    else:
      slow_print("Sonic Sonar Failed!")

  def whirlpool(self, opponent):
    slow_print(f"\n{self.name} used Whirlpool on {opponent.name}\n")
    slow_print(f"{opponent.name} is confused\n")
    
  def tidal_wave(self, opponent):
    damage = opponent.health * 0.3
    opponent.health -= damage
    slow_print(f"\n{self.name} used Tidal Wave on {opponent.name}\n")
    slow_print(f"Tidal Wave dealt {damage} damage!\n")

    
    






