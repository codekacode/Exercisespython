num = int(input("Introduzca un numero : ")) #num=4

for i in range(0,num):
    for j in range (0,num-i-1): #4-0-1=3
        print(end = "? ")
    for j in range (0,i+1):
        print ("*",end="/ ")
    print ()