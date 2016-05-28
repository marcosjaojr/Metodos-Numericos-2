# -*- coding: utf-8 -*-

# Newton Cote Aberto
# Aluno: Marcos José Augusto de Oliveira Júnior
# Matricula: 370021

#Vetores com [pnto,peso]
graus = [[],[{ "ponto": 0, "peso": 0 }],
[{ "ponto": -0.577350269, "peso": 1.0 },{ "ponto": 0.577350269, "peso": 1.0 }],
[{ "ponto": -0.774596669, "peso": 0.555555556 },{ "ponto": 0, "peso": 0.888888889 },{ "ponto": 0.774596669, "peso": 0.555555556 }],
[{ "ponto": -0.861136312, "peso": 0.347854845 },{ "ponto": -0.339981043, "peso": 0.652145155 },{ "ponto": 0.339981043, "peso": 0.652145155 },{ "ponto": 0.861136312, "peso": 0.347854845 }],
[{ "ponto": -0.906179845, "peso": 0.236926885 },{ "ponto": -0.538469309, "peso": 0.478628670 },{ "ponto": 0, "peso": 0.568888889 },{ "ponto": 0.538469309, "peso": 0.478628670 },{ "ponto": 0.906179845, "peso": 0.236926885 }]]

def f(x):
    return x**4 + x;

def GaussLegendre(a, b, numPontos, n):

    tamanhoSubIntevalo = float(b - a)/n;
    ai = a;
    integral = 0;

    for numIntervalos in range(1,n+1):

        #Andando com o bi
        bi = ai + tamanhoSubIntevalo
        #Zerando o resultado do SubIntervalo
        resultadoSubIntervalo = 0

        for i in range(0,numPontos):

        	ponto = graus[numPontos][i]["ponto"]
        	peso = graus[numPontos][i]["peso"]

        	#Calculando quem sera o xi para esse intervalo, no caso ai e bi
        	xi = ( ponto*(bi - ai) + ai + bi  )/2
        	resultadoSubIntervalo += peso*f(xi)

        #Calculando a integral peso*f(parametrizacao(xi))
        integral += resultadoSubIntervalo
        #Andando no subintervalo
        ai = bi

    return integral * tamanhoSubIntevalo /2;

def integrar(a, b, tol, numPontos):

    n = 2

    print "\nCalculando..."
    oIntegral = GaussLegendre(a, b, numPontos, n)
    nIntegral = GaussLegendre(a, b, numPontos, n+1)
    while abs(oIntegral - nIntegral) > 10**tol:
        n += 1
        oIntegral = nIntegral
        nIntegral = GaussLegendre(a, b, numPontos, n+1)
    print "I =",nIntegral
    print "Com n =",n

def menu():
    nPontos = "Escolha o número de pontos de Legendre (1 - 5)\n" + "> "

    return input(nPontos)

def main():
    print "\n################## SEJA BEM-VINDO! ##################"
    print "Sistema para o metodo de Gauss-Legendre\n"

    iniciar = raw_input("Tecle [ENTER] para iniciar\n")

    a = input("Limite inicial da integral:\n")
    b = input("Limite final da integral:\n")
    tolerancia = input("Tolerancia (potencia negativa de 10, Ex: digite -5 para 10 elevado a -5):\n")

    nPontos = menu()
    integrar(a, b, tolerancia, nPontos)

main();
