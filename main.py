from classes import our_solar_system


target_planet = input('Enter the name of a planet: ')
target_planet = target_planet.capitalize()
planet = our_solar_system.get_planet(target_planet)
moons = planet.moons

if planet:
    print(moons if moons else '{} has no moons!'.format(planet))
else:
    print('{} is not a planet!'.format(planet))
