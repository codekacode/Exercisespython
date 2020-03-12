""" FOR  IN contiene un iterador de listas, dictonary, n arrays dimensionales,
 etc. El iterador recupera cada componente e imprime datos mientras realiza el 
 bucle. El iterador disminuye o incrementa automaticamente"""

#cars = ["Audi","Toyota","Volkswagen"]

#for y in cars :
    #print (y)

# Indexación usando la función Range: también podemos usar indexación usando range 
# () en Python

#cars = ["Audi","Toyota","Volkswagen"]

#for i in range(len(cars)) :
    #print (cars[i])

# Accessing items using enumerate()

"""titis = ["Audis","Toyota","Volkswagen"]

for  i , x in enumerate(titis) :
    print (i , x)
"""

# Accessing items and indexes enumerate()

"""cars = ["Aston" , "Audi", "McLaren "]
for x in enumerate(cars):
    print (x[0], x[1])"""

#Print return valor of enumerate()

"""cars = ["Aston" , "Audi", "McLaren "]
print (enumerate(cars))
"""

# demonstrating the use of start in enumerate 1

cars = ["Aston" , "Audi", "McLaren "]
for x in enumerate(cars, start=1):
    print (x[0] , x[1])