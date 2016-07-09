from numpy import *

def preditor_corretor5(F,s0,t):

    n = len(t)
    s = array([s0] * n)

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

def F(s,t):
    return 1-t+4*s

def imprimir_valores(t, s):
    for i in xrange(min(len(t),len(s))):
        print "s("+str(t[i])+") = "+str(s[i])

def main():
    n = 51
    t = linspace(0.0, 10.0, n)
    s = preditor_corretor5(F, 1.0, t)

    imprimir_valores(t, s)

main()
