titis = ["Audis","Toyota","Volkswagen"]
accesorios = ["Timon", "Parabrisas" , "Llantas"]

prices = {1:30000, 2:450000, 3:698444, 4: 4098 , 5:6543, 6:7463}

for i , c in enumerate(titis, start=1) :
    print ("titi : %s price : %s" % (c , prices [i]))

for i , a in enumerate(accesorios, start=1) :
    print ("accesorio : %s price : %s"
    %(a , prices[i+len(titis)]))


"""# Two separate lists
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS kit", "Car repair-tool kit"]

# Single dictionary holds prices of cars and 
# its accessories.
# First three items store prices of cars and
# next two items store prices of accessories.
prices = {1:"570000$", 2:"68000$", 3:"450000$",
          4:"8900$", 5:"4500$"}

# Printing prices of cars
for index, c in enumerate(cars, start=1):
    print ("Car: %s Price: %s"%(c, prices[index]))

# Printing prices of accessories
for index, a in enumerate(accessories,start=1):
    print ("Accessory: %s Price: %s"\
           %(a,prices[index+len(cars)]))"""