#to create a pokemon world!

class Pokemon:
    def __init__(self,entry,names,types,description,is_caught):
        self.entry = entry
        self.names = names
        self.types = types
        self.description = description
        self.is_caught = is_caught
        

    def speak(self):
        print(f"{self.names} says: " + self.names + " " + self.names)
    
    def display_info(self):
        print(f"Entry: {self.entry}")
        print(f"Name: {self.names}")
        print(f"Type: {self.types}")
        print(f"Description: {self.description}")
        print(f"Caught: {self.is_caught}")
        print(f"Speak: {self.speak}")

Pikachu = Pokemon(34,"Pikachu",["Electric"],"This Pokemon has electricity-storing pouches on its cheeks. These appear to become electrically charged during the night while Pikachu sleeps. It occasionally discharges electricity when it is dozy after waking up.","No")
Charizard = Pokemon(6,"Charizard",["Fire", "Flying"],"Charizard flies around the sky in search of powerful opponents. It breathes fire of such great heat that it melts anything. However, it never turns its fiery breath on any opponent weaker than itself.","Yes")
Bulbasaur = Pokemon(1,"Bulbasaur","Grass","Bulbasaur can be seen napping in bright sunlight. There is a seed on its back. By soaking up the sun's rays, the seed grows progressively larger.","No")

Pikachu.display_info()
Charizard.speak()
Bulbasaur.display_info()


"""
# Pokédex 📟
# Codédex

# Class definition
class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(self.name + ', ' + self.name + '!')
  
  def display_details(self):
    print('Entry Number: ' + str(self.entry))
    print('Name: ' + self.name)

    if len(self.types) == 1:
      print('Type: ' + self.types[0])
    else:
      print('Type: ' + self.types[0] + '/' + self.types[1])
    
    print('Description: ' + self.description)

    if self.is_caught:
      print(self.name + ' has already been caught!')
    else:
      print(self.name + ' hasn\'t been caught yet.')

# Pokémon objects
pikachu = Pokemon(25, 'Pikachu', ['Electric'], 'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.', True)
charizard = Pokemon(3, 'Charizard', ['Fire', 'Flying'], 'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.', False)
gyarados = Pokemon(130, 'Gyarados', ['Water', 'Flying'], 'It has an extremely aggressive nature. The HYPER BEAM it shoots from its mouth totally incinerates all targets.', False)

pikachu.speak()
charizard.speak()
gyarados.speak()"""