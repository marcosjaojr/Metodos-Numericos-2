# -*- coding: utf-8 -*-

# Newton Cote Aberto
# Aluno: Marcos José Augusto de Oliveira Júnior
# Matricula: 370021

from math import *

def f(x):
    return (1.0/sqrt(1-x**2))*(1.0/(2+x**2));

def getPonto(numPontos, i):
    val = ((i-(1.0/2))/numPontos);
    return cos(val*pi)

def getPeso(numPontos):
    return pi/numPontos

def GaussChebyshev(numPontos):

    integral = 0;

    for i in range(1,numPontos+1):

    	xi = getPonto(numPontos, i)
    	peso = getPeso(numPontos)

    	integral += peso*(sqrt(1-xi**2))*f(xi)

    return integral;

def integrar(nPontos):

    print "\nCalculando..."
    nIntegral = GaussChebyshev(nPontos);
    print "I =",nIntegral

def menu():
    nPontos = "Escolha o número de pontos de Chebyshev:\n" + "> "

    return input(nPontos)

def main():
    print "\n################## SEJA BEM-VINDO! ##################"
    print "Sistema para o metodo de Gauss-Chebyshev\n"

    iniciar = raw_input("Tecle [ENTER] para iniciar\n")

    nPontos = menu()
    integrar(nPontos)

main();
