# -*- coding: utf-8 -*-

# Método de Gauss Laguerre
# Aluno: Marcos José Augusto de Oliveira Júnior
# Matricula: 370021

from math import e
from GaussLaguerreData import graus

def f(x):
    return (e**(-x))*(1.0/(1+x**2));

def GaussLaguerre(numPontos):

    integral = 0;

    for i in range(0,numPontos):

    	xi = graus[numPontos][i]["ponto"]
    	peso = graus[numPontos][i]["peso"]

    	integral += peso*(e**(xi))*f(xi)

    return integral;

def integrar(nPontos):

    print "\nCalculando..."
    nIntegral = GaussLaguerre(nPontos);
    print "I =",nIntegral

def menu():
    nPontos = "Escolha o número de pontos de Laguerre (2 - 6):\n" + "> "

    return input(nPontos)

def main():
    print "\n################## SEJA BEM-VINDO! ##################"
    print "Sistema para o metodo de Gauss-Laguerre\n"

    iniciar = raw_input("Tecle [ENTER] para iniciar\n")

    nPontos = menu()
    integrar(nPontos)

main();
