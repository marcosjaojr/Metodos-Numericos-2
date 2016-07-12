#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Marcos Augusto <370021>
    Zedequias Santos <344062>
    Trabalho final
    Métodos Numéricos II
    UFC
"""

import numpy

#-----------------------------------------------------------------------------

m = [] # massas
k = [] # constantes elasticas
c = [] # constantes de amortecimento
inicio_1 = 2 # posição inicial do bloco 1
inicio_2 = 4 # posição inicial do bloco 2

def f1(t):
    return 4*sin(t)
    # return 0

def f2(t):
    return 3*sin(t)
    # return 0

def F(s,t):
    sNew = zeros((4))

    sNew[0] = s[2]
    sNew[1] = s[3]
    sNew[2] = (k[1]*(s[1]-s[0]) + c[1]*(s[3]-s[2]) - k[0]*s[0] - c[0]*s[2] + f1(t)) / m[0]
    sNew[3] = (-k[1]*(s[1]-s[0]) - c[1]*(s[3]-s[2]) + f2(t)) / m[1]
    return sNew

def get_s0(x1, x2, n):
    s0 = zeros((n,4))

    s0[0][0] = float(x1)
    s0[0][1] = float(x2)
    s0[0][2] = -10.0 # v1
    s0[0][3] = 0.0 # v2

    return s0


#-----------------------------------------------------------------------------

def forward_euler( F, s, t ):

    n = len(t)
    for i in xrange(n - 1):
        s[i+1] = s[i] + (t[i+1] - t[i]) * F(s[i],t[i])

    return s

#-----------------------------------------------------------------------------

def backward_euler( F, s, t ):

    n = len(t)
    for i in xrange(n - 1):
        s[i+1] = s[i] + (t[i+1] - t[i]) * F(s[i], t[i])
        s[i+1] = s[i] + (t[i+1] - t[i]) * F(s[i+1],t[i+1])

    return s

#-----------------------------------------------------------------------------

def runge_kutta5( F, s, t ):

    n = len( t )

    for i in xrange( n - 1 ):
        h = t[i+1] - t[i]
        k1 = h * F(s[i], t[i])
        k2 = h * F(s[i] + (2/5.0)*k1, t[i] + 2 * (h/5.0))
        k3 = h * F(s[i] + (11/64.0)*k1 + (5/64.0)*k2, t[i] + (h/4.0))
        k4 = h * F(s[i] + (3/16.0)*k1 + (5/16.0)*k2, t[i] + 2*(h/4.0))
        k5 = h * F(s[i] + (9/32.0)*k1 - (27/32.0)*k2 + (3/4.0)*k3 + (9/16.0)*k4, t[i] + 3*(h/4.0))
        k6 = h * F(s[i] - (9/28.0)*k1 + (35/28.0)*k2 - (12/7.0)*k4 + (8/7.0)*k5, t[i+1])
        s[i+1] = s[i] + (7.0 * k1 + 35.0 * k3 + 12.0 * k4 + 32.0 * k5 + 7.0 * k6) / 90.0

    return s

#-----------------------------------------------------------------------------

def metodoEulerModificado(t, s, F):
    h = t[1] - t[0]

    for i in range(len(t)-1):
        Fi = F(s[i], t[i])
        s[i+1] = s[i] + 0.5 * h * (Fi + F(s[i] + h*Fi, t[i+1]))

    return s;


#-----------------------------------------------------------------------------

def preditor_corretor5(F,s,t):

    n = len(t)

    # Runge-Kutta de grau 5.
    F1 = F2 = F3 = F4 = 0
    for i in xrange(min(4, n - 1)):
        h = t[i+1] - t[i]
        F0 = F(s[i], t[i])
        k1 = h * F0
        k2 = h * F(s[i] + (2/5.0)*k1, t[i] + 2 * (h/5.0))
        k3 = h * F(s[i] + (11/64.0)*k1 + (5/64.0)*k2, t[i] + (h/4.0))
        k4 = h * F(s[i] + (3/16.0)*k1 + (5/16.0)*k2, t[i] + 2*(h/4.0))
        k5 = h * F(s[i] + (9/32.0)*k1 - (27/32.0)*k2 + (3/4.0)*k3 + (9/16.0)*k4, t[i] + 3*(h/4.0))
        k6 = h * F(s[i] - (9/28.0)*k1 + (35/28.0)*k2 - (12/7.0)*k4 + (8/7.0)*k5, t[i+1])
        s[i+1] = s[i] + (7.0 * k1 + 35.0 * k3 + 12.0 * k4 + 32.0 * k5 + 7.0 * k6) / 90.0
        F1, F2, F3, F4 = (F0, F1, F2, F3)

    # Preditor-Corretor de grau 5.
    for i in xrange(4, n - 1):
        h = t[i+1] - t[i]
        F0 = F(s[i], t[i])
        w = s[i] + h * (1901.0 * F0 - 2774.0 * F1 + 2616.0 * F2 - 1274.0 * F3 + 251.0 * F4) / 720.0
        Fw = F(w, t[i+1])
        s[i+1] = s[i] + h * (251.0 * Fw + 608.0 * F0 - 150.0 * F1 - 8.0 * F2 + 19.0 * F3) / 720.0
        F1, F2, F3, F4 = (F0, F1, F2, F3)

    return s

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

if __name__ == "__main__":
    from pylab import *

    def inicializaSistema():
        m1 = input("Massa do primeiro carrinho: ")
        m2 = input("Massa do segundo carrinho: ")
        k1 = input("Constante elástica da primeira mola: ")
        k2 = input("Constante elástica da segunda mola: ")
        c1 = input("Constante de amortecimento da primeira mola: ")
        c2 = input("Constante de amortecimento da segunda mola: ")
        x1 = input("Posição inicial do primeiro carrinho: ")
        x2 = input("Posição inicial do segundo carrinho: ")

        m.append(m1)
        m.append(m2)
        k.append(k1)
        k.append(k2)
        c.append(c1)
        c.append(c2)

        return x1, x2


    x1, x2 = inicializaSistema();

    n = 21
    t = linspace(float(0), float(2), n)

    s_euler = forward_euler(F, get_s0(x1,x2,n), t)
    s_euler_modificado = metodoEulerModificado(t, get_s0(x1,x2,n), F)
    s_rk5 = runge_kutta5(F, get_s0(x1,x2,n), t)
    s_pc = preditor_corretor5(F, get_s0(x1,x2,n), t)
    s_b_euler = backward_euler(F,get_s0(x1,x2,n), t)


#   figura( 1 )
    subplot( 2, 2, 1 )
    plot( t, [ y1 + inicio_1 for y1 in s_euler[:,0]], 'b-o', t, [ x1 + inicio_2 for x1 in s_euler[:,1]], 'g-o')
    xlabel( '$t$' )
    ylabel( '$x$' )
    title( 'Solucao usando Euler' )
    legend( ( 'x1', 'x2' ), loc='lower left' )

#   figura( 2 )
    subplot( 2, 2, 2 )
    plot( t, [ y2 + inicio_1 for y2 in s_euler_modificado[:,0]], 'b-o', t, [ x2 + inicio_2 for x2 in s_euler_modificado[:,1]], 'g-o')
    xlabel( '$t$' )
    ylabel( '$x$' )
    title( 'Solucao usando Euler modificado' )
    legend( ( 'x1', 'x2' ), loc='upper right' )

#   figura( 3 )
    subplot( 2, 2, 3 )
    plot( t, [ y3 + inicio_1 for y3 in s_rk5[:,0]], 'b-o', t, [ x3 + inicio_2 for x3 in s_rk5[:,1]], 'g-o')
    xlabel( '$t$' )
    ylabel( '$x$' )
    title( 'Solucao usando Runge-Kutta grau 5' )
    legend( ( 'x1', 'x2' ), loc='lower left' )

#   figura( 4 )
    subplot( 2, 2, 4 )
    plot( t, [ y4 + inicio_1 for y4 in s_pc[:,0]], 'b-o', t, [ x4 + inicio_2 for x4 in s_pc[:,1]], 'g-o')
    xlabel( '$t$' )
    ylabel( '$x$' )
    title( 'Solucao usando preditor corretor' )
    legend( ( 'x1', 'x2' ), loc='lower left' )

    figure()
    plot( t, [ y4 + inicio_1 for y4 in s_pc[:,0] ], 'b-o', t, [ y3 + inicio_1 for y3 in s_rk5[:,0] ], 'g-o', t, [ y2 + inicio_1 for y2 in s_euler_modificado[:,0] ], 'y-o', t, [ y1 + inicio_1 for y1 in s_euler[:,0] ], 'r-o', t, [ y1 + inicio_1 for y1 in s_b_euler[:,0] ], 'm-o')
    xlabel( '$t$'  )
    ylabel( '$x$'  )
    title( 'Solucao usando preditor corretor'  )
    legend( ( 'PC', 'RK5', 'Euler Modificado', 'Forward Euler', 'Backward Euler'  ), loc='lower right'  )


    show()
