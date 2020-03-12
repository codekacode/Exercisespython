"""Función zip (Ambos iteradores se usarán en una construcción de bucle único):
 esta función es útil para combinar elementos de datos de iteradores de tipo 
 similar (list-list o dict-dict, etc.) en la posición i-ésima. Utiliza la longitud 
 más corta de estos iteradores de entrada. Se omiten otros elementos de iteradores 
 de mayor longitud. En caso de iteradores vacíos, devuelve Sin salida.

Por ejemplo, el uso de zip para dos listas (iteradores) ayudó a combinar un solo 
automóvil y su accesorio requerido"""

titis = ["Audis","Toyota","Volkswagen","Mini"]
accesorios = ["Timon", "Parabrisas" ,"Sonido", "Llantas", "GPS"]

for t , a in zip(titis , accesorios):
    print ("titis: %s , accesorios: %s" % (t,a))

#El reverso de estos iteradores de la función zip se conoce como descomprimir usando el operador "*".
titi , acceso = zip(*[("Audi", "GPS"),("Volvo","Timon")])

print (titi)
print (acceso)