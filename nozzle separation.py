import math

# def amount_of_water(spray_radius, step_size, x, separation) :
#   # domain = [0, nozzle_separation]  
#   def chord(x, separation): 
#     math.sqrt(spray_radius**2 - (x - separation)^2)

#   water = chord(x, )
#   return  



def chord(x, nozzle_separation, spray_radius):
  return 2*(math.sqrt(spray_radius**2 - (x - nozzle_separation)^2))

print(chord(0, 0, 25))
print(chord(25, 0, 25))