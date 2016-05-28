# Newton Cote Aberto
# Aluno: Marcos Jose Augusto de Oliveira Junior
# Matricula: 370021
from math import *

def f(x):
	return x**4 + x;

def calcularXi(intervaloA, intervaloB, i, numIntervalos):
	return intervaloA + i * (intervaloB - intervaloA) / numIntervalos

def grau0(a, b, n):

	somatorio = 0;
	subIntervalo = float(b-a)/n;
	ai = a;
	for i in range(0,n):
		bi = ai + subIntervalo
		x1 = calcularXi(ai,bi,1,2)
		somatorio += f(x1)
		ai = bi
	integral = somatorio*subIntervalo

	return integral

def grau1(a, b, n):

	somatorio = 0;
	subIntervalo = float(b-a)/n;
	ai = a;
	for i in range(0,n):
		bi = ai + subIntervalo
		x1 = calcularXi(ai,bi,1,3)
		x2 = calcularXi(ai,bi,2,3)
		somatorio += f(x1) + f(x2)
		ai = bi
	integral = somatorio*subIntervalo/2

	return integral

def grau2(a, b, n):

	somatorio = 0;
	subIntervalo = float(b-a)/n;
	ai = a;
	for i in range(0,n):
		bi = ai + subIntervalo
		x1 = calcularXi(ai,bi,1,4)
		x2 = calcularXi(ai,bi,2,4)
		x3 = calcularXi(ai,bi,3,4)
		somatorio += 2*f(x1)
		somatorio -= f(x2)
		somatorio += 2*f(x3)
		ai = bi
	integral = somatorio*subIntervalo/3

	return integral

def grau3(a, b, n):

	somatorio = 0;
	subIntervalo = float(b-a)/n;
	ai = a;
	for i in range(0,n):
		bi = ai + subIntervalo
		x1 = calcularXi(ai,bi,1,5)
		x2 = calcularXi(ai,bi,2,5)
		x3 = calcularXi(ai,bi,3,5)
		x4 = calcularXi(ai,bi,4,5)
		somatorio += 11*f(x1)
		somatorio += f(x2)
		somatorio += f(x3)
		somatorio += 11*f(x4)
		ai = bi
	integral = somatorio*subIntervalo/24

	return integral

def grau4(a, b, n):

	somatorio = 0;
	subIntervalo = float(b-a)/n;
	ai = a;
	for i in range(0,n):
		bi = ai + subIntervalo
		x1 = calcularXi(ai,bi,1,6)
		x2 = calcularXi(ai,bi,2,6)
		x3 = calcularXi(ai,bi,3,6)
		x4 = calcularXi(ai,bi,4,6)
		x5 = calcularXi(ai,bi,5,6)
		somatorio += 11*f(x1)
		somatorio -= 14*f(x2)
		somatorio += 26*f(x3)
		somatorio -= 14*f(x4)
		somatorio += 11*f(x5)
		ai = bi
	integral = somatorio*subIntervalo/20

	return integral

def grau5(a, b, n):

	somatorio = 0;
	subIntervalo = float(b-a)/n;
	ai = a;
	for i in range(0,n):
		bi = ai + subIntervalo
		x1 = calcularXi(ai,bi,1,7)
		x2 = calcularXi(ai,bi,2,7)
		x3 = calcularXi(ai,bi,3,7)
		x4 = calcularXi(ai,bi,4,7)
		x5 = calcularXi(ai,bi,5,7)
		x6 = calcularXi(ai,bi,6,7)
		somatorio += 611*f(x1)
		somatorio -= 453*f(x2)
		somatorio += 562*f(x3)
		somatorio += 562*f(x4)
		somatorio -= 453*f(x5)
		somatorio += 611*f(x6)
		ai = bi
	integral = somatorio*subIntervalo/1440

	return integral

def integrar(a, b, tol, opcao):
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
		oIntegral = funcao(a, b, n)
		nIntegral = funcao(a, b, n+1)
		while abs(oIntegral - nIntegral) > 10**tol:
			n += 1
			oIntegral = nIntegral
			nIntegral = funcao(a, b, n+1)
		print "I =",oIntegral
		print "Com n =",n

def menu():
	opcoes = "Escolha um dentre os graus do polinomio:\n" + "0 - Grau 0\n" + "1 - Grau 1\n" + "2 - Grau 2\n" + "3 - Grau 3\n" +"4 - Grau 4\n" + "5 - Grau 5\n" + "> "

	return input(opcoes)

def main():
	print "\n################## SEJA BEM-VINDO! ##################"
	print "Sistema para o metodo de Newton-Cotes aberto\n"

	iniciar = raw_input("Tecle [ENTER] para iniciar\n")

	a = input("Limite inicial da integral:\n")
	b = input("Limite final da integral:\n")
	tolerancia = input("Tolerancia (potencia negativa de 10, Ex: digite -5 para 10 elevado a -5):\n")

	opcao = menu()
	integrar(a, b, tolerancia, opcao)

main()
