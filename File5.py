#Declaraciones de control 
#Prints all letters except 'e' and 's'
"""Declaraciones de control de bucle : las instrucciones de control de bucle cambian la ejecución de su secuencia normal. Cuando la ejecución deja un ámbito, todos los objetos automáticos que se crearon en ese ámbito se destruyen. Python admite las siguientes declaraciones de control.
Continuar declaración: Devuelve el control al comienzo del bucle"""

#Continuar declaración: Devuelve el control al comienzo del bucle.

for letter in 'geeksforgeeks': 
    if letter == 'e' or letter == 's':
         continue
    #print ('Current Letter :', letter)
    
##################################

#Declaración de ruptura: saca el control del circuito
# break the loop as soon it sees 'e' or 's'

for letter in 'geeksforgeeks': 
    if letter == 'e' or letter == 's':
         break
#print ('Current Letter2 :', letter) """el print en break no va indentado"""

#Declaración de aprobación : Utilizamos la declaración de aprobación para escribir bucles vacíos. 
#Pass también se usa para instrucciones, funciones y clases de control vacías.
# An empty loop
for letter in 'geeksforgeeks':
    pass
#print ('Last Letter :', letter)


# Other example
for letter in 'Python': 
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)

print ("Good bye!")