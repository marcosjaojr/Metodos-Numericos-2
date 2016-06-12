# -*- coding: utf-8 -*-
from numpy import *
# Método de Householder
# Aluno: Marcos José Augusto de Oliveira Júnior
# Matricula: 370021

def iniciarMatriz():
    arquivo = open('matriz.db', 'r')
    return [ map(float,linha.split('|')[0].split(',')) for linha in arquivo ]

def imprimirNaTela(A, T, H):
    print('\n----- Resultado -----')
    print('Matriz Inicial:')
    print('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in A]))
    print('\nMatriz Tridiagonal:')
    print('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in T]))
    print('\nMatriz de Householder:')
    print('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in H]))

def imprimirEmArquivo(A, T, H):
    arq = open('resultado.txt', 'w')
    texto = []
    texto.append('----- Resultado -----\n')
    texto.append('\nMatriz Inicial:\n')
    texto.append('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in A]))
    texto.append('\n\nMatriz Tridiagonal:\n')
    texto.append('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in T]))
    texto.append('\n\nMatriz de Householder:\n')
    texto.append('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in H]))
    arq.writelines(texto)
    print('\n...Arquivo resultado.txt criado com sucesso!')
    arq.close()

def getNormal(v):
    return sqrt(sum(i*i for i in v))

def normalizar(v):
    normal = getNormal(v)
    return list(i/normal for i in v)

def inicializarComZero(n):
    return list(0 for i in range(0,n))

def householderMetodo(tempA,h):
    n = len(tempA[h])
    v = list((tempA[i][h]) for i in range(h+1,n))
    normV = getNormal(v)
    if v[0] > 0:
        v[0] = v[0] + normV
    else:
        v[0] = v[0] - normV

    nv = normalizar(v)
    N = inicializarComZero(n)
    for i in range(h+1,n):
        N[i] = nv[i-(h+1)]
    Qh = identity(n) - 2*multiply(matrix(N),matrix(N).transpose())
    return Qh

def getTridiagonal(A):
    n = len(A[0])
    H = identity(n)
    tempA = A
    for h in range(0,n-1):
        Qh = householderMetodo(tempA,h)
        H = H*Qh
        tempA = (Qh*matrix(tempA)*Qh).tolist()
    T = matrix(tempA).round(4).tolist();
    H = H.round(4).tolist()
    return T, H;

def main():
    print "\n################## SEJA BEM-VINDO! ##################"
    print "Sistema para o metodo de Householder\n"


    iniciar = raw_input("Tecle [ENTER] para iniciar\n")
    A = iniciarMatriz()
    T, H = getTridiagonal(A)

    imprimirNaTela(A, T, H)
    imprimirEmArquivo(A, T, H)
main()
