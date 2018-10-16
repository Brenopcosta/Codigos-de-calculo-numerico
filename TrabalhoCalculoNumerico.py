from math import *

erro = 0.00001

def concentracaoDeOD(t):
    return 1-7*(exp(-0.88*t))

def derivadaConcentracaoDeOD(t):
    return 6.16*(exp(-0.88*t))

def funcaoDeIteracao(t0):
    return t0-(concentracaoDeOD(t0) / derivadaConcentracaoDeOD(t0))

def metodoDeNewtonParaOCaso(t0,valorErro):
    tempoAnterior = t0
    tempoSeguinte = 0
    for contador in range (100):
        if derivadaConcentracaoDeOD(tempoAnterior) == 0 :
            break
        if (abs(funcaoDeIteracao(t0)) <=  valorErro):
            tempoSeguinte = tempoAnterior 
            break
        tempoSeguinte = funcaoDeIteracao(tempoAnterior)
        if ((tempoSeguinte - tempoAnterior ) < valorErro ):
            break
        tempoAnterior = tempoSeguinte
    return abs(tempoSeguinte)
            
