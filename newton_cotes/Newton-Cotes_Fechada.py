# -*- coding: utf-8 -*-

# Newton Cote Fechada
# Aluno: Marcos José Augusto de Oliveira Júnior
# Matricula: 370021
from math import *

#Global
_a = 0
_b = 0
_tol = 0

def f(x):
	return x**3 + sin(x);

def grau0(a, b, n):

	somatorio = 0
	h = float(b-a)/n

	ai = a;
	for i in range(0,n):
		bi = ai + h
		somatorio += f(ai)
		ai = bi

	integral = somatorio*(h)

	return integral

def grau1(a, b, n):

	somatorio = 0
	h = float(b-a)/n

	ai = a;
	for i in range(0,n):
		bi = ai + h
		somatorio += f(ai) + f(bi)
		ai = bi

	integral = somatorio*(h/2.0)

	return integral

def grau2(a, b, n):

	somatorio = 0
	h = float(b-a)/n

	ai = a
	for i in range(0,n):
		bi = ai + h
		x0 = ai
		x1 = ai + (h/2.0)
		x2 = bi
		somatorio += f(x0) + 4*f(x1) + f(x2)
		ai = bi

	integral = somatorio*(h/6.0)

	return integral

def grau3(a, b, n):

	somatorio = 0
	h = float(b-a)/n

	ai = a
	for i in range(0,n):
		bi = ai + h
		x0 = ai
		x1 = ai + (h/3.0)
		x2 = ai + 2*(h/3.0)
		x3 = bi
		somatorio += f(x0) + 3*f(x1) + 3*f(x2) + f(x3)
		ai = bi
	
	integral = somatorio*(h/8)

	return integral

def grau4(a, b, n):

	somatorio = 0
	h = float(b-a)/n

	ai = a
	for i in range(0,n):
		bi = ai + h
		x0 = ai
		x1 = ai + (h/4.0)
		x2 = ai + 2*(h/4.0)
		x3 = ai + 3*(h/4.0)
		x4 = bi
		somatorio += 7*f(x0) + 32*f(x1) + 12*f(x2) + 32*f(x3) + 7*f(x4)
		ai = bi

	integral = somatorio*(h/90.0)

	return integral

def grau5(a, b, n):

	somatorio = 0
	h = float(b-a)/n

	ai = a
	for i in range(0,n):
		bi = ai + h
		x0 = ai
		x1 = ai + (h/5.0)
		x2 = ai + 2*(h/5.0)
		x3 = ai + 3*(h/5.0)
		x4 = ai + 4*(h/5.0)
		x5 = bi
		somatorio += 19*f(x0) + 75*f(x1) + 50*f(x2) + 50*f(x3) + 75*f(x4) + 19*f(x5)
		ai = bi

	integral = somatorio*(h/288.0)

	return integral

def integrar(opcao):

	a = _a
	b = _b
	tol = _tol

	n = 1
	funcao = 0

	if opcao == 0:
		funcao = grau0
	elif opcao == 1:
		funcao = grau1
	elif opcao == 2:
		funcao = grau2
	elif opcao == 3:
		funcao = grau3
	elif opcao == 4:
		funcao = grau4
	elif opcao == 5:
		funcao = grau5
	else:
		print("Opcao invalida")

	if funcao:
		print "\nCalculando..."
		nIntegral = funcao(a, b, n)
		while 1:
			n += 1
			oIntegral = nIntegral
			nIntegral = funcao(a, b, n)
			if (abs(oIntegral - nIntegral) <= 10**tol):
				break;

		print "I =",nIntegral
		print "Com n =",n

def menu():
	opcoes = "Escolha um dentre os graus do polinomio:\n" + "0 - Grau 0\n" + "1 - Grau 1\n" + "2 - Grau 2\n" + "3 - Grau 3\n" +"4 - Grau 4\n" + "5 - Grau 5\n" + "> "

	return input(opcoes)

def main():
	print "\n################## SEJA BEM-VINDO! ##################"
	print "Sistema para o metodo de Newton-Cotes fechado\n"

	iniciar = raw_input("Tecle [ENTER] para iniciar\n")

	global _a
	global _b
	global _tol

	_a = input("Limite inicial da integral:\n")
	_b = input("Limite final da integral:\n")
	_tol = input("Tolerancia (potencia negativa de 10, Ex: digite -5 para 10 elevado a -5):\n")

	opcao = menu()
	integrar(opcao)

main()
