import math
def questao11(x):
    return (math.sqrt(x+1))- math.sqrt(x)

def questao12(x):
    return 1 / ((math.sqrt(x))+ (math.sqrt(x+1)))

def questao21(x):
    return math.log(x-(math.sqrt(pow(x,2)+1)))

def questao22(x):
    return (1-math.cos(x))/pow(x,2)


def geradorDeResultadosParaAFuncao22(x):
    while x<=20:
        if x == 0 :
            continue
        y = questao22(x)
        print (y)
        x=x+1
