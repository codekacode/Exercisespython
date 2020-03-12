#El bloque else justo después de for / while se ejecuta solo cuando el ciclo 
#NO termina con una declaración de interrupción.

"""for i in range(1,5):
    print (i)
else :
    print("Sin descanso/ se ejecuta porque no hay break")"""

# Program to check if an array consists 
# of even number

"""def evenumbers (lista) :
    for l in lista :
        if l % 2 == 0 :
            print ("Hay numeros pares en la lista")
            break
    else :
        print ("No hay numeros pares en la lista")

print ("Lista 1 :" )
evenumbers([5,3,6])

print ("Lista 2 :" )
evenumbers([1,3,5])"""

count = 4
while count < 1 :
    count += 1
    print (count)


else:
    print ("no break")
