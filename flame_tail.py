import time
import random
from fire_elemental import Fire_Elemental
from Damola import slow_print



class Flame_Tail(Fire_Elemental):
  def __init__(self, name, health, max_health, status, is_alive, pet_level, pet_exp, is_evolved, element, skills, evolution):
    super().__init__(name, health, max_health, status, is_alive, pet_level, pet_exp, is_evolved, element, skills, evolution)
    self.species = "Flame Tail"
    self.skills["Firey Tail"] = self.firey_tail
    self.skills["Heat Scream"] = self.heat_scream
    self.skills["Claw Attack"] = self.claw_attack
    self.evolution = "Matchstick Menace"

  def get_skills(self):
    return self.skills

  def set_skills(self, skills):
    self.skills = skills    

  def firey_tail(self, opponent):
    slow_print(f"\n{self.name} initiates Firey Tail...\n")
    success_rate = random.randint(1, 100)
    if success_rate > self.hit_chance:
      slow_print(f"\n{self.name} shakes its tail and raises the temperature. The temperature is now unbearable for {opponent.name}...\n")
      damage = opponent.health * 0.25
      effective_string, damage = self.effectiveness(opponent, damage)
      damage = round(damage, 2)
      opponent.health -= damage
      self.health += damage
      time.sleep(1)
      slow_print(f"\n{self.name} used Firey Tail on {opponent.name} for {damage} damage and healed for the same amount.\n")
      slow_print(effective_string)
      time.sleep(0.5)
    else:
      slow_print("Firey Tail failed...")

  def heat_scream(self, opponent):
    slow_print(f"\n{self.name} screams and attempts to target its firey breath at {opponent.name}...\n")
    success_rate = random.randint(1,100)
    if success_rate > 50:
      damage = opponent.health * 0.6
      damage = round(damage, 2)
      opponent.health -= damage
      time.sleep(1)
      slow_print(f"\n{self.name} used Heat Scream on {opponent.name} for {damage} damage..\n")
      effective_string, damage = self.effectiveness(opponent, damage)
      slow_print(effective_string)
      time.sleep(0.5)
    else: 
      slow_print(f"\n{self.name}'s Heat Scream didn't reach {opponent.name}\n")

  def claw_attack(self, opponent):
    slow_print(f"\n{self.name} takes a giant leap towards {opponent.name} to attack with its claw..\n")
    success_rate = random.randint(1,100)
    if success_rate > self.hit_chance:
      damage = random.randint(3, 9)
      damage = round(damage, 2)
      opponent.health -= damage
      time.sleep(1)
      slow_print(f"\n{self.name} successfully used Claw Attack on {opponent.name} for {damage} damage..\n")
      effective_string, damage = self.effectiveness(opponent, damage)
      slow_print(effective_string)
      time.sleep(0.5)
    else: 
      slow_print(f"\n{self.name} missed {opponent.name} with their claws..\n")  



    



  