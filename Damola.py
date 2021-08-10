import sys
import time
import os

def clear():
  os.system("clear")

def slow_print(word):
  for letter in word:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(.035)

def int_checker(message):
  while True:
    try:
      integer = int(input(message))
      return integer
    except ValueError:
      print("Enter a valid option.")