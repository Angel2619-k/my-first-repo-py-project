#My Pokedex

class Pokemon:
  def __init__(self,Enternumber,name,types,description,is_caught,level,height,weight):
    self.Enternumber = Enternumber
    self.name = name 
    self.types = types
    self.description = description
    self.is_caught = is_caught
    self.level = level
    self.height = height 
    self.weight = weight

  # what they speak
  def speak(self):
    print(f"{self.name} {self.name}")


  # Their details
  def display_details(self):
    print(self.Enternumber)
    print(self.name)
    print(self.types)
    print(self.level)
    print(self.height)
    print(self.weight)
    if self.is_caught:
      print(self.name + " has already been caught")
    else :
      print(self.name + " has not been caught")

#pokemon 

Raichu = Pokemon (26, "Raichu" , ["Electric"] ,"When its electricity builds, its muscles are stimulated, and it becomes more aggressive than usual." , True , 10 ,0.6,29.9)

Rhyhorn = Pokemon (111, "Rhyhorn", ["Ground , Rock"], "claims an area with over a six mile radius as its territory",False, 15, 2.5,50.59)

#output
Raichu.speak()
Raichu.display_details()
print("\n")
Rhyhorn.speak()
Rhyhorn.display_details()
