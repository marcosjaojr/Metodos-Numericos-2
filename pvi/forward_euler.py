# -*- coding: utf-8 -*-
from numpy import *

def forward_euler( F, s0, t ):

    n = len(t)
    s = array([s0] * n)
    for i in xrange(n - 1):
        s[i+1] = s[i] + (t[i+1] - t[i]) * F(s[i], t[i])

    return s

def F(s,t):
    return 1-t+4*s

def imprimir_valores(t, s):
    print "\n--- RESULTADO ---"
    for i in xrange(min(len(t),len(s))):
        print "s("+str(t[i])+") = "+str(s[i])

def iniciar_sistema():
    _a = input("Início do intervalo:\n> ")
    _b = input("Final do intervalo:\n> ")
    _s0 = input("Valor inicial:\n> ")
    _n = input("Quantidade de números:\n> ")
    return (_a, _b, _s0, _n)

def main():
    print "\n################## SEJA BEM-VINDO! ##################"
    print "Sistema para o metodo de Forward Euler\n"

    iniciar = raw_input("Tecle [ENTER] para iniciar\n")
    a, b, s0, n = iniciar_sistema()

    t = linspace(float(a), float(b), n)
    s = forward_euler(F, float(s0), t)

    imprimir_valores(t, s)

main()
