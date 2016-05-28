# -*- coding: utf-8 -*-

# Método de Gauss Hermite
# Aluno: Marcos José Augusto de Oliveira Júnior
# Matricula: 370021

from math import e
from GaussHermiteData import graus

def f(x):
    return (e**(-x**2))*(1.0/(3+x**2));

def GaussHermite(numPontos):

    integral = 0;

    for i in range(0,numPontos):

    	xi = graus[numPontos][i]["ponto"]
    	peso = graus[numPontos][i]["peso"]

    	integral += peso*(e**(xi**2))*f(xi)

    return integral;

def integrar(nPontos):

    print "\nCalculando..."
    nIntegral = GaussHermite(nPontos);
    print "I =",nIntegral

def menu():
    nPontos = "Escolha o número de pontos de Hermite (2 - 6):\n" + "> "

    return input(nPontos)

def main():
    print "\n################## SEJA BEM-VINDO! ##################"
    print "Sistema para o metodo de Gauss-Hermite\n"

    iniciar = raw_input("Tecle [ENTER] para iniciar\n")

    nPontos = menu()
    integrar(nPontos)

main();
