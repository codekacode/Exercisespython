#Programa para la suma de los dígitos de un número dado
def digitsSum(n):
    return (n%10)+(n//10)

###########

def digits_sum(num) :
    s = 0
    while num :
        s += num % 10
        num //= 10
    return s