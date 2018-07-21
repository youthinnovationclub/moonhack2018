#!/bin/python3
from classes import *
import random

print("Welcome to a quiz, how well do you know your moons?")
planet = random.randint(1,7)
if planet == 1:
  answer = input("What is the name of Earth's moon?")
  if answer == str(ourSolarSystem.getPlanet("Earth")).split("'")[1]:
    print("Congrats you got it right!")
  else:
    print("You got it wrong, better luck next time. The correct answer is " , ourSolarSystem.getPlanet("Earth"))
elif planet == 2:
  answer = input("What is the name of Mars's first moon?")
  if answer == str(ourSolarSystem.getPlanet("Mars")).split("'")[1]:
    print("Congrats you got it right!")  
  else:
    print("You got it wrong, better luck next time.")
elif planet == 3:
  answer = input("What is the name of Jupiter's first moon?")
  if answer == str(ourSolarSystem.getPlanet("Jupiter")).split("'")[1]:
    print("Congrats you got it right!")  
  else:
    print("You got it wrong, better luck next time.")
elif planet == 4:
  answer = input("What is the name of Saturn's first moon?")
  if answer == str(ourSolarSystem.getPlanet("Saturn")).split("'")[1]:
    print("Congrats you got it right!")  
  else:
    print("You got it wrong, better luck next time.")
elif planet == 5:
  answer = input("What is the name of Uranus's first moon?")
  if answer == str(ourSolarSystem.getPlanet("Uranus")).split("'")[1]:
    print("Congrats you got it right!")  
  else:
    print("You got it wrong, better luck next time.")
elif planet == 6:
  answer = input("What is the name of Neptune's first moon?")
  if answer == str(ourSolarSystem.getPlanet("Neptune")).split("'")[1]:
    print("Congrats you got it right!")  
  else:
    print("You got it wrong, better luck next time.")
elif planet == 7:
  answer = input("What is the name of Pluto's moon?")
  if answer == str(ourSolarSystem.getPlanet("Pluto")).split("'")[1]:
    print("Congrats you got it right!")  
  else:
    print("You got it wrong, better luck next time.")