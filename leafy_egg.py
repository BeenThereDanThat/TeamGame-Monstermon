import random
import time
from earth_elemental import Earth_Elemental
from random import randint
from Damola import slow_print

class Leafy_Egg(Earth_Elemental):
  def __init__(self, name, health, max_health, status, is_alive, pet_level, pet_exp, is_evolved, element, skills, evolution):
    super().__init__(name, health, max_health, status, is_alive, pet_level, pet_exp, is_evolved, element, skills, evolution)
    self.species = "Leafy Egg"
    self.element = "earth"
    self.skills["Ivy Wrap"] = self.ivy_wrap
    self.skills["Acid Yolk"] = self.acid_yolk
    self.skills["Egg Bowl"] = self.egg_bowl
    self.evolution = "Terra Zygote"
    
  
  def ivy_wrap(self, opponent):
    success_rate = randint(1,100)
    if success_rate > self.hit_chance:
      heal = random.randint(3, 10)
      slow_print(f"\n{self.name} used Ivy Wrap\n")
      slow_print(f"The Ivy Wrap successfully healed {self.name} for {heal} hp\n")
      time.sleep(0.5)
    else:
      slow_print(f"\n{self.name} attempted to use Ivy Wrap but failed!\n")  

  def acid_yolk(self, opponent):
    opponent.update_status("burn")
    slow_print(f"\n{self.name} used Acid Yolk on {opponent.name}\n")
    slow_print(f"Acid Yolk inflicted burn on {opponent.name} for their next 2 turns!\n")
    time.sleep(0.5)
    
  def egg_bowl(self, opponent):
    damage = random.randint(3, 7)
    effective_string, damage = self.effectiveness(opponent, damage)
    opponent.health -= damage
    slow_print(f"\n{self.name} used Egg Bowl on {opponent.name}\n")
    slow_print(f"Egg bowl dealt {round(damage, 2)} damage!\n")
    slow_print(effective_string)
    time.sleep(0.5)

    ''' Simple melee strike 40% of full health DONE '''
    






