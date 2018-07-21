#!/bin/python3
from classes import *

targetPlanet = input("Type the name of a planet:")

targetPlanet = targetPlanet.capitalize()
#print(targetPlanet)

myPlanet = ourSolarSystem.getPlanet(targetPlanet)

if myPlanet is not None:
  moons = (myPlanet.get_moons())
  if len(moons) > 0:
    print(moons)
  else:
    print(targetPlanet + " has no moons!")
    
else:
    print(targetPlanet+ " is not a planet!")
    









