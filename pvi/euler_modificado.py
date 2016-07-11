# -*- coding: utf-8 -*-
from numpy import *

def toleravel(l_old, l_new, tol):
    return (abs(abs(l_new) - abs(l_old))/abs(l_new)) < tol

def F(t,s):
    return 1-t+4*s;

def metodoEulerModificado(t0, s0, tF, n):
    h = (tF-t0)/n;
    x = t0;
    s = array([s0] * n);
    print('\nUsando passo de: ' + str(h))
    for i in xrange(n-1):
        s[i+1] = s[i] + 0.5 * h * (F(x,s[i]) + F(x+h, s[i] + h*F(x,s[i])))
        # print('s[' + str(x) + '] = ' + str(s[i]))
        x = x+h;

    return s;

def imprimirResultado(s, t0, tF, n):
    h = (tF-t0)/n;

    print "\n######## RESULTADO ########\n"

    for i in range(len(s)):
        print('s['+str(t0)+'] = ' + str(s[i]))
        t0 = t0+h
    print '\n'

def inicializaSistema():
    t0 = input("Valor de t0: ")
    s0 = input("Valor de s0: ")
    tF = input("Até que valor de t voce deseja calcular: ")
    n = input("Quantos valores devem ser calculados: ")

    return t0, s0, tF, n

def main():
    print "\n################## SEJA BEM-VINDO! ##################"
    print "Sistema para o metodo de Euler Modificado\n"

    iniciar = raw_input("Tecle [ENTER] para iniciar\n")

    t0, s0, tF, n = inicializaSistema();

    s = metodoEulerModificado(float(t0), float(s0), float(tF), n)
    imprimirResultado(s, float(t0), float(tF), n)
main()
