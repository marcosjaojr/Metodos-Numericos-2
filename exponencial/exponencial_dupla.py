# Exponencial dupla
# Aluno: Marcos Jose Augusto de Oliveira Junior
# Matricula: 370021

from math import *

# global
_a = 0
_b = 0
_tol = 0

def f(x):
  return ((1.0/4)*(x**((pi/2.0)*exp(x)))*(x**(-1.0/2))); # Apresenta singularidade no ponto x = 0 do intervalo [0,2]

def g(z):
  a = _a;
  b = _b;
  return f(x(z))*(((b - a)*(pi/4.0)*cosh(z))/(cosh((pi/2.0)*sinh(z))**2))

def x(z):
  a = _a;
  b = _b;
  return (1.0/2)*(a + b + (b - a)*tanh((pi/2.0)*sinh(z)));

def trapezio(a,b,n):
  integral=0.0
  h = float(b-a)/n
  
  for i in range(0,n):
    b = a + h
    integral += g(a) + g(a+h)
    a = b
    
  integral *= h/2

  return integral

def i_trapezio(a,b,tol):
  n = 1;
  inew = trapezio(a,b,n)
  while 1:
    n += 1;
    iold = inew;
    inew = trapezio(a,b,n);
    if (abs(inew - iold) <= (10**tol)):
      break;
  return inew;

def integrar(tol):
  dx = 0.1;
  ai = -dx;
  bi = dx;
  inew = i_trapezio(ai, bi, tol);
  while 1:
    ai -= dx
    bi += dx
    iold = inew;
    inew = i_trapezio(ai, bi, tol);
    if (abs(inew - iold) <= (10**tol)):
      break;
  return inew;

def main():
  print ("## CALCULO DE EXPONENCIAL DUPLA ##");
  print ("--            com singularidade   --\n");
  global _a
  global _b
  _a = input("Intervalo A:\n");
  _b = input("Intervalo B:\n");
  tol = input("Tolerancia, potencia negativa de 10 (Ex: entre 3 para 10^-3):\n");

  print 'Integral de ((1.0/4)*(x**((pi/2.0)*exp(x)))*(x**(-1.0/2))) em ['+str(_a)+','+str(_b)+'], com tolerancia de 10^' + str(-tol) + ':'
  print integrar(-tol);

main();
