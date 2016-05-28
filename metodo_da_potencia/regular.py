# -*- coding: utf-8 -*-
from math import *
# Método da Pontência Regular
# Aluno: Marcos José Augusto de Oliveira Júnior
# Matricula: 370021

def iniciarMatriz(arquivo):
    return [ map(int,linha.split('|')[0].split(',')) for linha in arquivo ]

def iniciarVetor(arquivo):
    return list(int(linha.split('|')[1].replace('\n', '')) for linha in arquivo)

def definirTolerancia(arquivo):
    return float(arquivo.readline().split('|')[2])

def normalizacao(x):
    return sqrt(sum(i*i for i in x))

def toleravel(l_old, l_new, tol):
    return (abs(l_new - l_old)/abs(l_new)) < tol

def produtoMatrizVetor(A, x):
    result = []
    for linha in A:
        sum_linha = 0;
        for i in range(len(x)):
            sum_linha = sum_linha + x[i]*linha[i]
        result.append(sum_linha)

    return result

def produtoVetores(v_transp, v_norm):
    result = 0
    for i in range(len(v_transp)):
        result = result + v_transp[i]*v_norm[i]
    return result

def metodoDaPotencia(A, x, tol):
    l_old = 0
    l_new = 0
    v_new = x
    true = 1
    while true:
        l_old = l_new
        v_old = v_new
        phi = list(i/normalizacao(v_old) for i in v_old)
        v_new = produtoMatrizVetor(A, phi)
        l_new = produtoVetores(phi, v_new);

        if toleravel(l_old, l_new, tol):
            true = 0

    return l_old, phi

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
    print('Autovalor:')
    print autoValor
    print('Autovetor:')
    print autoVetor

def imprimirEmArquivo(A, x, tol, autoValor, autoVetor):
    arq = open('resultado.txt', 'w')
    texto = []
    texto.append('----- Resultado -----\n')
    texto.append('\nAutovalor:\n')
    texto.append(str(autoValor))
    texto.append('\nAutovetor:\n')
    texto.append(str(autoVetor))
    arq.writelines(texto)
    print('\n...Arquivo resultado.txt criado com sucesso!')
    arq.close()

def main():
    print "\n################## SEJA BEM-VINDO! ##################"
    print "Sistema para o metodo da Potência Regular\n"


    iniciar = raw_input("Tecle [ENTER] para iniciar\n")
    A, x, tol = iniciarSistema()

    autoValor, autoVetor = metodoDaPotencia(A, x, tol)

    imprimirNaTela(A, x, tol, autoValor, autoVetor)
    imprimirEmArquivo(A, x, tol, autoValor, autoVetor)
main()
