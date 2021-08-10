import os
import keyboard
import random
from player import Player
from fire_tortoise import Fire_Tortoise
from leafy_egg import Leafy_Egg
from angry_hosepipe import Angry_Hosepipe
from flame_tail import Flame_Tail

from Damola import slow_print, clear, int_checker
from time import sleep

# class Game(object):
#   def __init__(self,turn,encounter,pause,tutorial):
#     self.turns = turn
#     self.encounter = encounter
#     self.pause = pause
#     self.tutorial = tutorial

#   def get_turn(self):
#     return self.turn

#   def get_encounter(self):
#     return self.encounter

#   def get_pause(self):
#     return self.pause

#   def get_tutorial(self):
#     return self.tutorial

#   def set_turn(self,turns):
#     self.turn = turns

#   def set_encounter(self,encounter):
#     self.encounter = encounter

#   def set_pause(self,pause):
#     self.pause = pause

#   def set_tutorial(self,tutorial):
#     self.tutorial = tutorial

#   def clear():
#     os.system("clear")


def new_game():
    new_player_name = input(
        "Enter a name for your new player\n> ").capitalize().strip()
    new_player = Player(new_player_name, health=1, status=None)
    player = new_player.get_name()
    print("\nHello,", player)
    # self, name, health, max_health, moves, status, is_alive, pet_level, pet_exp, is_evolved, element
    while True:
        print(
            "which pet would you like to choose?\n1) Fire Tortoise\n2) Leafy Egg\n3) Flame Tail\n4) Angry Hosepipe"
        )
        choose_pet = input("> ").strip()
        if choose_pet == "1":
            player_pet = Fire_Tortoise("",
                                       20,
                                       20,
                                       status=None,
                                       is_alive=True,
                                       pet_level=1,
                                       pet_exp=0,
                                       is_evolved=False,
                                       element="fire",
                                       skills={},
                                       evolution="Magma Snapper")
            break
        elif choose_pet == "2":
            player_pet = Leafy_Egg("",
                                   20,
                                   20,
                                   status=None,
                                   is_alive=True,
                                   pet_level=1,
                                   pet_exp=0,
                                   is_evolved=False,
                                   element="earth",
                                   skills={},
                                   evolution="Terror Zygote")
            break
        elif choose_pet == "3":
            player_pet = Flame_Tail("",
                                    20,
                                    20,
                                    status=None,
                                    is_alive=True,
                                    pet_level=1,
                                    pet_exp=0,
                                    is_evolved=False,
                                    element="fire",
                                    skills={},
                                    evolution="Matchstick Menace")
            break
        elif choose_pet == "4":
            player_pet = Angry_Hosepipe("",
                                        20,
                                        20,
                                        status=None,
                                        is_alive=True,
                                        pet_level=1,
                                        pet_exp=0,
                                        is_evolved=False,
                                        element="water",
                                        skills={},
                                        evolution="Livid Sea Snake")
            break
        else:
            print("Please enter a valid option")

    pet_name = input(
        "what would you like to name your pet?\n> ").capitalize().strip()
    player_pet.set_name(pet_name)
    return player_pet


# all above code creates new instances of player and pet as a freash start to save to a new file
def pause_game():
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('p'):  # if key 'p' is pressed
                pause_options = input(
                    "Your Game is Paused\n\n\n0)Resume Game\n1)Save Game\n2)Load Game\n3)Exit Game"
                )

                if pause_options == "0":
                    pass
                elif pause_options == "1":
                    #save Game
                    pass
                elif pause_options == "2":
                    #load game
                    pass
                elif pause_options == "3":
                    print("Would you like to save game before leaving? (Y/N)")
                    save_chk = input(">").lower()
                    exitLoop = True
                    while exitLoop:
                        if save_chk == "y":
                            slow_print("Saving game...")
                            # will call function to save game data to external file
                            slow_print("Exiting game...")
                            new_game()
                        elif save_chk == "n":
                            slow_print("Exiting game...")
                            new_game()
                        else:
                            print("Please enter Y/N")
                            save_chk = input(">").lower()

                break  # finishing the loop
        except:
            break  # if user pressed a key other than the given key the loop will break


def player_attack(pet, enemy):
    skills = pet.get_skills()
    for i, skill in enumerate(skills):
        print(f"{i+1}) {skill}")
    while True:
        skill_choice = int_checker("> ")
        skills_list = list(pet.skills)
        if skill_choice > 4 or skill_choice < 1:
            print("Enter a valid option")
        else:
            index = skill_choice - 1
            chosen_skill = skills_list[index]
            if skill_choice == 1:
                pet.skills[chosen_skill](enemy)
                break
            elif skill_choice == 2:
                pet.skills[chosen_skill](enemy)
                break
            elif skill_choice == 3:
                pet.skills[chosen_skill](enemy)
                break
            elif skill_choice == 4:
                pet.skills[chosen_skill](enemy)
                break
            else:
                print("Enter a valid option")


def enemy_attack(pet, enemy):
    enemy_skills = list(enemy.skills)
    enemy_choice = random.choice(enemy_skills)
    enemy.skills[enemy_choice](pet)


# def turn(turn_num):
#   turn = turn_num
#   turn = 0
#   pass.56.5
#   #player attack
#   #if opponent parilized
#     #pass
#   #elif
#     #opponent attack

#   turn+=1
#   return turn


def fight(pet, enemy, turn):

    while (pet.is_alive) and (enemy.is_alive):
        clear()
        print(
            f"{pet.name}  VS  {enemy.name}\n{round(pet.health)}/{pet.max_health} "
            + (" " * len(pet.name)) +
            f"{round(enemy.health)}/{enemy.max_health}\n")
        skip = debuffs(pet, turn)
        if pet.health <= 0:
            pet.set_health(0)
            pet.set_is_alive(False)
            pet.dead()
            return
        if skip == False:
            player_attack(pet, enemy)
        sleep(2)
        if enemy.health <= 0:
            enemy.set_health(0)
            enemy.set_is_alive(False)
            enemy.dead()
            break
        skip = debuffs(enemy, turn)
        if enemy.health <= 0:
            enemy.set_health(0)
            enemy.set_is_alive(False)
            enemy.dead()
            break
        if skip == False:
            enemy_attack(pet, enemy)
        sleep(1)
        if pet.health <= 0:
            pet.set_health(0)
            pet.set_is_alive(False)
            pet.dead()
            return
        sleep(2)
        turn += 1
    pet.encounter += 1
    fight_exp(pet, turn)


def burning(pet, turn):
    damage = pet.health / 4
    damage = round(damage, 2)
    if "burning" in pet.status:
        slow_print(f"\n{pet.name} was burned for {damage} damage..\n")
        pet.health -= damage
        if turn >= (pet.burn_applied + 1):
            pet.change_status("burning", "r")
        sleep(1)
    else:
        return 0


def burn(pet, turn):
    if "burn" in pet.status:
        pet.update_status("burning")
        pet.change_status("burn", "r")
        pet.burn_applied = turn
    else:
        pass


def crowd_control(pet):
    if "trapped" in pet.status:
        slow_print(
            f"\n{pet.name} has been trapped in the ground and cannot attack!\n"
        )
        pet.change_status("trapped", "r")
        sleep(1)
        return True
    else:
        return False


def debuffs(pet, turn):
    burn(pet, turn)
    burning(pet, turn)
    skip = crowd_control(pet)
    return skip


def fight_exp(player_pet, turn):
    match_exp = 0
    if turn <= 2:
        match_exp += 1000
        slow_print(f"\nyou gained 1000 exp")
    elif turn > 2 and turn <= 10:
        match_exp += 500
        slow_print(f"\nyou gained 500 exp")
    elif turn > 10 and turn <= 20:
        match_exp += 250
        slow_print(f"\nyou gained 250 exp")
    else:
        match_exp += 150
        slow_print(f"\nyou gained 150 exp")

    total_exp = player_pet.get_pet_exp()
    total_exp += match_exp
    slow_print(f"\nYou now have {total_exp} exp\n")
    player_pet.set_pet_exp(total_exp)

    sleep(1)
    level_up(player_pet)


def level_up(player_pet):
    level = player_pet.get_pet_level()
    exp = player_pet.get_pet_exp()
    max_hp = player_pet.get_max_health()
    if exp >= 1000:
        exp -= 1000
        level += 1
        max_hp += 10
        player_pet.set_max_health(max_hp)
        player_pet.set_health(max_hp)
        slow_print(f"\n{player_pet.name} leveled up to level {level}")
    player_pet.set_pet_exp(exp)
    player_pet.set_pet_level(level)
    evolve(player_pet)


def evolve(player_pet):
    level = player_pet.get_pet_level()
    evolved = player_pet.get_is_evolved()
    if evolved == False:
        if level >= 10:
            player_pet.set_is_evolved(True)
            slow_print(
                f"\n{player_pet.name} has evolved into a {player_pet.evolution}"
            )
            player_pet.set_species(player_pet.evolution)
        else:
            pass
    else:
        pass


def print_skills(pet):
    skills = pet.get_skills()
    for i, skill in enumerate(skills):
        print(f"{i+1}) {skill}")


# class New_Game(Game):
#   def __init__(self,turn,encounter,pause,tutorial,new):
#     super().__init__(self,turn,encounter,pause,tutorial)
#     self.new = new
