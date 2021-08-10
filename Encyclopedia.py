from Damola import slow_print,clear



def encyclopedia():
  
  while True:
    slow_print("Please select a catagory\n1.)Rules Of Play\n2.)Pets\n3.)Exit\n")
    menu_options = input("> ")

    if menu_options == "1":
      clear()
      print("1. Pick a pet and battle\n\n2. Using your pets skills, try to defeat your opponent\n\n3. Win Battles and level up your pet\n\n4. some elements are stronger against other elements e.g water against fire\n\n5.Have Fun!")
      input("Press Enter To Continue")

    elif menu_options == "2":
      clear()
      print("""
        Fire Tortoise - The master of the slow burn and hot to the touch 

        Leafy Egg - Dont underestimate this deadly embryo
      
        Angry Hosepipe - A very moody garden Applience, with all the power of Poseidon

        Fire Tail - They say every tail has its own tale
      """)
      input("Press Enter To continue... ")

    elif menu_options == "3":
      break

    else:
      print("Invalid option, try again")
  
  

