#calulation of radius of planets in solar system

#importing module
from math import pi
from random import choice as ch


planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

#acccessing the planet
random_planet = ch(planets)


 
def area():
    return 4*pi*r**2 


#calculating the radius of the planets

if random_planet == 'Mercury':
    r = 2440
    print(f"Radius of {random_planet} is {r} km")
    print(f"Area of {random_planet} is", area(), "km^2")

elif random_planet == 'Venus':
    r = 6052
    print(f"Radius of {random_planet} is {r} km")
    print(f"Area of {random_planet} is", area(),"km^2")
    
elif random_planet == 'Earth':
    r = 6371
    print(f"Radius of {random_planet} is {r} km")
    print(f"Area of {random_planet} is" , area() , "km^2")
   
elif random_planet == 'Mars':
    r = 3390
    print(f"Radius of {random_planet} is {r} km")
    print(f"Area of {random_planet} is ", area() ,"km^2")
    
elif random_planet == 'Saturn':
    r = 58232
    print(f"Radius of {random_planet} is {r} km")
    print(f"Area of {random_planet} is", area(), "km^2")
    
else:
    print("Invalid planet name")

