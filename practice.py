#Effectively a notebook program, you can ignore this

# rng = range(10)
# print(list(rng))
#rng = range(10,-10,-2)
#print(list(rng))

#strings = ["my", "world", "apple", "pear"]
#lengths = map(len, strings)
#print(list(lengths))
#lengths = map(lambda x: x + "s", strings)
#print(list(lengths))

#def longer_than_4(string):
#    return len(string) > 4

#strings = ["my", "world", "apple", "pear"]
#filtered = filter(longer_than_4, strings)
#print(list(filtered))

#IDEA: A House of Leaves style game using pygame; learn more about PyGame to do so. 

#def system_specs(system_name, *components, **details):
    #print(f"System: {system_name}")
    #print("\n Following Components Installed: ")
    #for component in components:
        #print(f"- {component}")

    #print("\n System Details: ")
    #for key, value in details.items():
        #print(f"- {key}: {value}")

#system_specs(
    #"Gaming PC",
    #"CPU: Intel i9",
    #"GPU: NVIDIA RTX 3080",
    #"RAM: 32 GB",
    #"SSD: 1 TB",
    #OS = "Windows 11",
    #Warranty = "2 Years"
#)

#Args handle positional arguments (everything in quotations) and puts them in a tuple
#Kwargs takes the functions/keyword arguments and puts them into a dictionary as key value pairs

#IDEA: JavaScript website tracking player actions in my Vampire: The Masquerade tabletop campaign.

#classses in python
#Class is just a blueprint for an object

#class Microwave:
    #def __init__(self, brand: str, power_rating: str):
        #self.brand = brand
        #self.power_rating = power_rating
        #self.turned_on: bool = False
        #self.turned_off: bool = True

#    def turn_on(self) -> None:
  #      if self.turned_on:
 #           print(f"Microwave ({self.brand}) is already turned on.")
   #     else:
    #        self.turned_on = True
     #       print(f"Microwave ({self.brand}) is now turned on.")

#    def turn_off(self) -> None:
 #       if self.turned_off:
  #          print(f"Microwave ({self.brand}) is already turned off.")
   #     else:
    #        self.turned_off = True
     #       print(f"Microwave ({self.brand}) is now turned off.")

#smeg: Microwave = Microwave(brand='Smeg', power_rating='B')

