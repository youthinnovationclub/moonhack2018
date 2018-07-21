class solarSystem:
  """
  A solar system
  
  Attributes:
    planets: a list of planet objects
  """
  
  def __init__(self):
    self.planets = []
    
  def addPlanet(self, planet):
    self.planets.append(planet)
    
  # Returns planet object or False if planet not found
  def getPlanet(self, name):
    for planet in self.planets:
      if name == planet.get_name():
        return planet
    return None

class planet:
  """
  A planet of a solar system.
  
  Attributes:
    name: the name of the planet
    moons: a list of the names of the moons
  """
  
  def __init__(self, name, moons):
    self.name = name
    self.moons = moons
  
  def __str__(self):
    return self.name + " " + str(self.moons)
    
  # Returns list of moons
  def get_moons(self):
    return self.moons
    
  def get_name(self):
    return self.name
    
  def add_moon(self,moon):
    self.moons.append(moon)

# Initialise the Solar System and add the 8 planets
ourSolarSystem = solarSystem()
ourSolarSystem.addPlanet(planet("Mercury",[]))
ourSolarSystem.addPlanet(planet("Venus",[]))
ourSolarSystem.addPlanet(planet("Earth",["Moon"]))
ourSolarSystem.addPlanet(planet("Mars",[
        "Deimos",
        "Phobos"
      ]))
ourSolarSystem.addPlanet(planet("Jupiter",[
        "Metis",
        "Adrastea",
        "Amalthea",
        "Thebe",
        "Io",
        "Europa",
        "Ganymede",
        "Callisto",
        "Themisto",
        "Leda",
        "Himalia",
        "Lysithea",
        "Elara",
        "S/2000 J11",
        "S/2003 J12",
        "Carpo",
        "Euporie",
        "S/2003 J3",
        "S/2003 J18",
        "Orthosie",
        "Euanthe",
        "Harpalyke",
        "Praxidike",
        "Thyone",
        "S/2003 J16",
        "Iocaste",
        "Mneme",
        "Hermippe",
        "Thelxinoe",
        "Helike",
        "Ananke",
        "S/2003 J15",
        "Eurydome",
        "Arche",
        "Herse",
        "Pasithee",
        "S/2003 J10",
        "Chaldene",
        "Isonoe",
        "Erinome",
        "Kale",
        "Aitne",
        "Taygete",
        "S/2003 J9",
        "Carme",
        "Sponde",
        "Megaclite",
        "S/2003 J5",
        "S/2003 J19",
        "S/2003 J23",
        "Kalyke",
        "Kore",
        "Pasiphae",
        "Eukelade",
        "S/2003 J4",
        "Sinope",
        "Hegemone",
        "Aoede",
        "Kallichore",
        "Autonoe",
        "Callirrhoe",
        "Cyllene",
        "S/2003 J2"
      ]))
ourSolarSystem.addPlanet(planet("Saturn",[
        "Tarqeq",
        "Pan",
        "Daphnis",
        "Atlas",
        "Prometheus",
        "Pandora",
        "Epimetheus",
        "Janus",
        "Aegaeon",
        "Mimas",
        "Methone",
        "Anthe",
        "Pallene",
        "Enceladus",
        "Tethys",
        "Calypso",
        "Telesto",
        "Polydeuces",
        "Dione",
        "Helene",
        "Rhea",
        "Titan",
        "Hyperion",
        "Iapetus",
        "Kiviuq",
        "Ijiraq",
        "Phoebe",
        "Paaliaq",
        "Skathi",
        "Albiorix",
        "S/2007 S2",
        "Bebhionn",
        "Erriapo",
        "Siarnaq",
        "Skoll",
        "Tarvos",
        "Greip",
        "S/2004 S13",
        "Hyrrokkin",
        "Mundilfari",
        "S/2006 S1",
        "Jarnsaxa",
        "Narvi",
        "Bergelmir",
        "S/2004 S17",
        "Suttungr",
        "Hati",
        "S/2004 S12",
        "Bestla",
        "Farbauti",
        "Thrymr",
        "S/2007 S3",
        "Aegir",
        "S/2004 S7",
        "S/2006 S3",
        "Kari",
        "Fenrir",
        "Surtur",
        "Ymir",
        "Loge",
        "Fornjot"
      ]))
ourSolarSystem.addPlanet(planet("Uranus",[
        "Cordelia",
        "Ophelia",
        "Bianca",
        "Cressida",
        "Desdemona",
        "Juliet",
        "Portia",
        "Rosalind",
        "Cupid",
        "Belinda",
        "Perdita",
        "Puck",
        "Mab",
        "Miranda",
        "Ariel",
        "Umbriel",
        "Titania",
        "Oberon",
        "Francisco",
        "Caliban",
        "Stephano",
        "Trinculo",
        "Sycorax",
        "Margaret",
        "Prospero",
        "Setebos",
        "Ferdinand"
      ]))
ourSolarSystem.addPlanet(planet("Neptune",[
        "Naiad",
        "Thalassa",
        "Despina",
        "Galatea",
        "Larissa",
        "Proteus",
        "Triton",
        "Nereid",
        "Halimede",
        "Sao",
        "Laomedeia",
        "Psamathe",
        "Neso"
      ]))
ourSolarSystem.addPlanet(planet("Pluto", ["Charon"]))