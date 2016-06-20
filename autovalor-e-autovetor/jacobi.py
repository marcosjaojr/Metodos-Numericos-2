# -*- coding: utf-8 -*-
from numpy import *
# Método de Jacobi
# Aluno: Marcos José Augusto de Oliveira Júnior
# Matricula: 370021

def iniciarMatriz():
    arquivo = open('matriz2.db', 'r')
    return matrix([ map(float,linha.split('|')[0].split(',')) for linha in arquivo ])

def definirTolerancia():
    arquivo = open('matriz2.db', 'r')
    return float(arquivo.readline().split('|')[1])

def iniciarSistema():
    return iniciarMatriz(), definirTolerancia()

def toleravel(old, new, tol):
    return (absolute(old.round(5)-new.round(5)) <= tol*absolute(new)).all()

def arredondar(A, D, J):
    fator = 5
    return A.round(fator).tolist(), D.round(fator).tolist(), J.round(fator).tolist()

def imprimirNaTela(A, D, J):
    print('\n----- Resultado -----')
    print('Matriz Inicial:')
    print('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in A]))
    print('\nMatriz Diagonal:')
    print('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in D]))
    print('\nMatriz de Jacobi:')
    print('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in J]))

def imprimirEmArquivo(A, D, J):
    arq = open('resultado.txt', 'w')
    texto = []
    texto.append('----- Resultado -----\n')
    texto.append('\nMatriz Inicial:\n')
    texto.append('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in A]))
    texto.append('\n\nMatriz Diagonal:\n')
    texto.append('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in D]))
    texto.append('\n\nMatriz de Jacobi:\n')
    texto.append('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in J]))
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

def matrizRotacao(i, j, tempA):
    if(tempA[i,i] == tempA[j,j]):
        teta = pi/4
    else:
        teta = (1.0/2)*arctan((2*tempA[i,j])/(tempA[j,j]-tempA[i,i]))
    r = identity(len(tempA))
    r[i,i] = cos(teta)
    r[j,j] = cos(teta)
    r[j,i] = -sin(teta)
    r[i,j] = sin(teta)

    return r

def algoritmoJacobi(A, tol):
    nValido = 1

    n = len(A)
    tempA = A
    J = identity(n)
    while nValido:
        for j in range(0,n-1):
            for i in range(j+1,n):
                tempJ = matrizRotacao(i,j,tempA)
                oldA = tempA
                tempA = tempJ.transpose()*tempA*tempJ
                J = J.dot(tempJ)

        if(toleravel(oldA, tempA, tol)):
            nValido = 0

    return tempA, J;

def main():
    print "\n################## SEJA BEM-VINDO! ##################"
    print "Sistema para o metodo de Jacobi\n"


    iniciar = raw_input("Tecle [ENTER] para iniciar\n")
    A, tol = iniciarSistema()

    D, J = algoritmoJacobi(A, tol)
    A, D, J = arredondar(A, D, J)

    imprimirNaTela(A,D,J)
    imprimirEmArquivo(A, D, J)
main()
