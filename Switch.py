"""Unlike every other programming language we have used before, Python does not have a switch or case statement. 
To get around this fact, we use dictionary mapping."""

def numl_a_string (argument) :
    switchis = {
        0 : "zero",
        1 : "one",
        2 : "two",
    }
    return switchis.get(argument , "nada") #Nada podria ir o no , revisar

if __name__ == "__main__" :
    argument = 2 
    print (numl_a_string(argument))