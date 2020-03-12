#WHILE
# No se recomienda usar while para iteradores
cuenta = 0

while cuenta < 4 :
    cuenta += 1
    print ("Hi dude")

##################
#FOR

print ("Iteracion con diccionario")
d = dict ()
d ["uno"] = 123
d ["dos"] = 345
for i in d :
    print ("%s %d" % (i,d[i]))


##################
#Bucles anidados 
for i in range (1,4) :
    for j in range (i):
        print (i , end=" ")
    print ()

##################
#Declaraciones de control de bucles

for letter in "Karemquiroz" :
    if letter == "a" or letter== "m" :
        continue
    #print ("Current letter", letter)

#Declaración de ruptura Saca el control del circuito

for letter in "Karemquiroz" :
    if letter == "r" or letter== "m" :
        break
    #print ("Current letter", letter)

#Declaracion de aprobacion - para escribir bucles vacios

for letter in "juanodicio" :
    pass
#print ("Last letter :" , letter)

for letter in "juanykarem":
    if letter == "y":
        pass
        print ("Esto es un pass")
    print ("Letra actual : ", letter)
print("Adios , nos vemos")