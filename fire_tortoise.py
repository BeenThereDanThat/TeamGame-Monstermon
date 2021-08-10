import random
import time
from fire_elemental import Fire_Elemental
from Damola import slow_print, clear


class Fire_Tortoise(Fire_Elemental):
  def __init__(self, name, health, max_health, status, is_alive, pet_level, pet_exp, is_evolved, element, skills, evolution):
    super().__init__(name, health, max_health, status, is_alive, pet_level, pet_exp, is_evolved, element, skills, evolution)
    self.species = "Fire Tortoise"
    self.skills["Grand Dash"] = self.grand_dash
    self.skills["Spinning Shell"] = self.spinning_shell
    self.skills["Healer's Heart"] = self.healers_heart
    self.evolution = "Magma Snapper"

  def get_skills(self):
    return self.skills

  def set_skills(self, skills):
    self.skills = skills

  def spinning_shell(self, opponent):
    slow_print(f"\n{self.name} attempts to use Spinning Shell...\n")
    time.sleep(1.5)
    rand_chance = random.randint(1,100)
    if rand_chance > self.hit_chance:
      opponent.update_status("intimidated")
      opponent.set_hit_chance()
      slow_print(f"\n{self.name} used Spinning Shell!\n")
      time.sleep(0.5)
      slow_print(f"{opponent.name} is Intimidated!\n")
      time.sleep(0.5)
    else:
      slow_print("Spinning Shell failed...\n")

  def grand_dash(self, opponent):
    slow_print(f"\n{self.name} attempts to use Grand Dash...\n")
    time.sleep(1.5)
    rand_chance = random.randint(1,100)
    if rand_chance > self.hit_chance:
      damage = random.randint(4, 8)
      if "vulnerable" in self.status:
        damage *= 1.1
      effective_string, damage = self.effectiveness(opponent, damage)
      opponent.health -= round(damage, 2)
      slow_print(f"\n{self.name} hit {opponent.name} with a Grand Dash for {damage} damage!\n")
      slow_print(effective_string)
    else:
      slow_print(f"{self.name} missed their Grand Dash...\n")

  def healers_heart(self, enemy):
    slow_print(f"\n{self.name} attempts to use Healer's Heart...\n")
    time.sleep(1.5)
    success_rate = random.randint(1,100)
    if success_rate >= 41:
      heal = self.max_health * .35
      self.health += heal
      if self.health > self.max_health:
       self.set_health(self.max_health)
      slow_print("\nHealer's Heart succeeded!\n")
      slow_print(f"{self.name} healed themself for {heal} hp\n")
    else:
      slow_print("Healer's Heart failed...\n")
      slow_print(f"{self.name} healed for nothing\n")