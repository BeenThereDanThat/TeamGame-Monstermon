import time
import random
import sys
from fire_tortoise import Fire_Tortoise
from leafy_egg import Leafy_Egg
from flame_tail import Flame_Tail
from angry_hosepipe import Angry_Hosepipe
from Damola import slow_print, clear
from game import new_game, fight, print_skills
from Encyclopedia import encyclopedia


def title_screen():
  print("""
  
█████████████████████████████████████████████████████████████
█▄─█▀▀▀█─▄█▄─▄▄─█▄─▄███─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▄▄─███─▄─▄─█─▄▄─█
██─█─█─█─███─▄█▀██─██▀█─███▀█─██─██─█▄█─███─▄█▀█████─███─██─█
▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀
  
██████╗░███████╗████████╗  ██████╗░░█████╗░████████╗████████╗██╗░░░░░███████╗
██╔══██╗██╔════╝╚══██╔══╝  ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝
██████╔╝█████╗░░░░░██║░░░  ██████╦╝███████║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░
██╔═══╝░██╔══╝░░░░░██║░░░  ██╔══██╗██╔══██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░
██║░░░░░███████╗░░░██║░░░  ██████╦╝██║░░██║░░░██║░░░░░░██║░░░███████╗███████╗
╚═╝░░░░░╚══════╝░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝

░█████╗░██████╗░███████╗███╗░░██╗░█████╗░
██╔══██╗██╔══██╗██╔════╝████╗░██║██╔══██╗
███████║██████╔╝█████╗░░██╔██╗██║███████║
██╔══██║██╔══██╗██╔══╝░░██║╚████║██╔══██║
██║░░██║██║░░██║███████╗██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝
  """)
  main_menu_select = input("1)Start New Game\n2)Exit Game\n> ")

  if main_menu_select == "1":
    # newgame = Game(1, None, None, None)
    player = new_game()
    prompt(player)

  elif main_menu_select == "2":
    pass

def game():
  pass

def prompt(pet):
  clear()
  print("Select an option:")
  print("1)Next encounter\n2)Heal pet\n3)Pet stats\n4)Encyclopedia\n5)Exit")
  action = input("> ").strip()
  acceptable_actions = ["1", "2", "3", "4", "5"]
  while action not in acceptable_actions:
    print(f"Invalid choice, try again.")
    action = input("> ").strip()
  if action == "1":
    encounters(pet)
  elif action == "2":
    free_heal(pet)
  elif action == "3":
    pet_stats(pet)
  elif action == "4":
    choose_encyclopedia(pet)
  else:
    pass

def choose_encyclopedia(pet):
  encyclopedia()
  prompt(pet)

def free_heal(pet):
  clear()
  print("------Nurse------")
  print("You can spend your heal token to get a free heal on your pet.")
  print("You only get one of these so use it wisely!")
  print(f"Heal Token: {pet.heal_token}")
  if pet.heal_token == 0:
    print("You don't have a heal token to use..")
    input("Press enter to return.")
    prompt(pet)
  else:
    print("Select an option:")
    print("1)Use heal token\n2)Return")
    user_choice = input("> ").lower().strip()
    loop = True
    while loop:
      if user_choice == "1":
        max_hp = pet.get_max_health()
        pet.set_health(max_hp)
        pet.set_heal_token(0)
        loop = False
        prompt(pet)
      elif user_choice == "2":
        loop = False
        prompt(pet)
      else:
        print("Enter a valid option\n")

def pet_stats(pet):
  clear()
  print(f"-------{pet.name}-------")
  print(f"Species: {pet.species}")
  print(f"Element: {pet.element.capitalize()}")
  print(f"Health: {pet.health}/{pet.max_health}")
  print(f"level: {pet.pet_level}")
  print(f"exp: {pet.pet_exp}")
  print("Skills:")
  print_skills(pet)
  input("\nPress enter to go back")
  prompt(pet)


def encounters(pet):
  if pet.encounter == 1:
    encounter_1(pet)
    prompt(pet)
  elif pet.encounter == 2:
    encounter_2(pet)
    prompt(pet)
  elif pet.encounter == 3:
    encounter_3(pet)
    prompt(pet)
  elif pet.encounter == 4:
    encounter_4(pet)
    prompt(pet)

def win(pet):
  clear()
  print("CONGRATUALTIONS YOU WIN!")

def encounter_1(pet):
  opponent = Leafy_Egg("Leafy Egg", 20, 20, "", True, 1, 0, False, "fire", {}, "")
  fight(pet, opponent, 1)

def encounter_2(pet):
  opponent = Fire_Tortoise("Fire Tortoise", 25, 25, "", True, 2, 0, False, "earth", {}, "")
  fight(pet, opponent, 1)

def encounter_3(pet):
  opponent = Flame_Tail("Flame Tail", 30, 30, "", True, 3, 0, False, "fire", {}, "")
  fight(pet, opponent, 1)

def encounter_4(pet):
  opponent = Fire_Tortoise("Fire Tortoise", 35, 35, "", True, 4, 0, False, "fire", {}, "")
  fight(pet, opponent, 1)

title_screen()
