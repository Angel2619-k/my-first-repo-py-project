#Hometown and Dream City
class City:
  def __init__(self,name,country,population,landmark):
    self.name = name
    self.country = country
    self.population = population
    self.landmark = landmark
Hometown = City('Surat','India',25000,'Surat Fort')
Dreamcity = City('Stanford','USA',5000,'Stanford University')
print(vars(Hometown))
print(vars(Dreamcity))
