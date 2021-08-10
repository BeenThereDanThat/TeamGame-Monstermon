import time
import random
from character import Character
from Damola import slow_print


class Fire_Elemental(Character):
    def __init__(self, name, health, max_health, status, is_alive, pet_level, pet_exp, is_evolved, element, skills, evolution):
        super().__init__(name, health, max_health, status, is_alive, pet_level, pet_exp, is_evolved, element, skills, evolution)
        self.element = "fire"
        self.skills = {}
        self.skills["Flame Breath"] = self.flame_breath

    def flame_breath(self, opponent):
      slow_print(f"\n{self.name} attempts to use Flame Breath...\n")
      time.sleep(1.5)
      rand_chance = random.randint(1,100)
      if rand_chance > self.hit_chance:
        if "vulnerable" in opponent.status:
          damage = (opponent.health / 4) * 1.1
        else:
          damage = opponent.health / 4
        effective_string, damage = self.effectiveness(opponent, damage)
        opponent.health -= damage
        opponent.update_status("vulnerable")
        slow_print(f"\n{self.name} used Flame Breath on {opponent.name}.\n")
        time.sleep(.75)
        slow_print(f"Flame breath dealt {round(damage, 2)} damage!\n")
        time.sleep(.5)
        slow_print(f"{opponent.name} is now vulnerable.\n")
        slow_print(effective_string)
      else:
        slow_print(f"{self.name}'s Flame Breath didn't ignite...\n")
