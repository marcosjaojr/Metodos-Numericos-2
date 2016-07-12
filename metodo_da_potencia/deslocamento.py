# -*- coding: utf-8 -*-
from math import *
from numpy import matrix

def iniciarMatriz(arquivo):
    return [ map(int,linha.split('|')[0].split(',')) for linha in arquivo ]

def iniciarVetor(arquivo):
    return list(int(linha.split('|')[1].replace('\n', '')) for linha in arquivo)

def definirTolerancia(arquivo):
    return float(arquivo.readline().split('|')[2])

def normalizacao(x):
    return sqrt(sum(i*i for i in x))

def toleravel(l_old, l_new, tol):
    return (abs(abs(l_new) - abs(l_old))/abs(l_new)) < tol

def matrizIdentidade(n):
    return [[1 if j==i else 0 for j in range(n)] for i in range(n)]

def produtoMatrizVetor(A, x):
    result = []
    for linha in A:
        sum_linha = 0;
        for i in range(len(x)):
            sum_linha = sum_linha + x[i]*linha[i]
        result.append(sum_linha)

    return result

def produtoMatrizEscalar(A, b):
    result = []
    for i in range(len(A)):
        linha = []
        for j in range(len(A)):
            linha.append(A[i][j] * b)
        result.append(linha)

    return result

def montarAb(A, u):
    return [[(A[i][j] - u) if j==i else A[i][j] for j in range(len(A))] for i in range(len(A))]

def getU(A, col):
    return A[col][col];

def produtoVetores(v_transp, v_norm):
    result = 0
    for i in range(len(v_transp)):
        result = result + v_transp[i]*v_norm[i]
    return result

def matrizInversa(A):
    return (matrix(A)**-1).tolist()

def metodoDaPotenciaInversa(A, x, tol):
    invA = matrizInversa(A);
    l_old = 0
    l_new = 0
    v_new = x
    true = 1
    while true:
        l_old = l_new
        v_old = v_new
        phi = list(i/normalizacao(v_old) for i in v_old)
        v_new = produtoMatrizVetor(invA, phi)
        l_new = produtoVetores(phi, v_new);

        if toleravel(l_old, l_new, tol):
            true = 0

    return l_old**-1, phi

def metodoDeslocamento(A, x, tol):
    autoVal = []
    autoVet = []
    I = matrizIdentidade(len(A))

    for i in range(len(A)):
        u = input('u: ')
        Ab = montarAb(A,u)

        valor, vetor = metodoDaPotenciaInversa(Ab, x, tol)
        autoVal.append(valor + u)
        autoVet.append(vetor)

        # print(u)
        # print('\n')
        # print(Ab)
        # print('valor: ' + str(valor) + '\n')
        # print(str(valor + u) + '\n')

    return autoVal, autoVet

def iniciarSistema():
    arquivo = open('matriz.db', 'r')
    A = iniciarMatriz(arquivo)
    arquivo = open('matriz.db', 'r')
    x = iniciarVetor(arquivo)
    arquivo = open('matriz.db', 'r')
    tol = definirTolerancia(arquivo)
    return A, x, tol

def imprimirNaTela(A, x, tol, autoValor, autoVetor):
    print('\n----- Parâmetros -----')
    print('Matriz:')
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in A]))
    print('\nVetor inicial:')
    print(x)
    print('\nTolerância:')
    print(tol)
    print('\n----- Resultado -----')
    print('Autovalores:')
    print autoValor
    print('\n')
    print('Autovetores:')
    for vet in autoVetor:
        print(str(vet))
    print('\n')

def imprimirEmArquivo(A, x, tol, autoValor, autoVetor):
    arq = open('resultado_inversa.txt', 'w')
    texto = []
    texto.append('----- Resultado -----\n')
    texto.append('\nAutovalor:\n')
    texto.append(str(autoValor))
    texto.append('\nAutovetor:\n')

    for vet in autoVetor:
        texto.append(str(vet))

    arq.writelines(texto)
    print('\n...Arquivo resultado_inversa.txt criado com sucesso!')
    arq.close()

def main():
    print "\n################## SEJA BEM-VINDO! ##################"
    print "Sistema para o metodo da Potência Inversa\n"


    iniciar = raw_input("Tecle [ENTER] para iniciar\n")
    A, x, tol = iniciarSistema()

    # autoValor, autoVetor = metodoDaPotenciaInversa(A, x, tol)
    autoValor, autoVetor = metodoDeslocamento(A, x, tol)

    imprimirNaTela(A, x, tol, autoValor, autoVetor)
    # imprimirEmArquivo(A, x, tol, autoValor, autoVetor)
main()
