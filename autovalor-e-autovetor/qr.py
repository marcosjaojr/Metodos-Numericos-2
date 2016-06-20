# -*- coding: utf-8 -*-
from numpy import *
# Método QR
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

def arredondar(A, tempA, Q):
    fator = 4
    return A.round(fator).tolist(), tempA.round(fator).tolist(), Q.round(fator).tolist()

def toleravel(old, new, tol):
    return (absolute(old.round(5)-new.round(5)) <= tol*absolute(new)).all()

def imprimirNaTela(A, D, Q):
    print('\n----- Resultado -----')
    print('Matriz Inicial:')
    print('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in A]))
    print('\nMatriz Diagonal:')
    print('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in D]))
    print('\nMatriz acumulada Q:')
    print('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in Q]))

def imprimirEmArquivo(A, D, Q):
    arq = open('resultado.txt', 'w')
    texto = []
    texto.append('----- Resultado -----\n')
    texto.append('\nMatriz Inicial:\n')
    texto.append('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in A]))
    texto.append('\n\nMatriz Diagonal:\n')
    texto.append('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in D]))
    texto.append('\n\nMatriz acumulada Q:\n')
    texto.append('\n'.join(['|'.join(['{:4}'.format(item) for item in row]) for row in Q]))
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

def testarAutovetores(A, Q):
    n = len(Q)
    for i in range(n):
        coluna = (A*Q[:, i]).transpose().tolist()[0]
        print "\nA*coluna"+str(i+1)+"="
        print str(getNormal(coluna))+"*"+str(normalizar(coluna))

def householderMetodo(tempA,h):
    n = len(tempA)
    v = list((tempA[i,h]) for i in range(h,n))
    normV = getNormal(v)
    if v[0] < 0:
        v[0] = v[0] + normV
    else:
        v[0] = v[0] - normV

    nv = normalizar(v)
    N = inicializarComZero(n)
    for i in range(h,n):
        N[i] = nv[i-(h)]
    Qh = identity(n) - 2*multiply(matrix(N),matrix(N).transpose())
    return Qh

def decomposicaoQR(tempA):
    n = len(tempA)
    R = tempA
    Q = identity(n)

    for i in range(n-1):
        Qh = householderMetodo(R, i)
        R = Qh*R
        Q = Q*Qh.transpose()
    return Q, R

def algoritmoQR(A, tol):
    nValido = 1;

    tempA = A
    Q = identity(len(A))
    while nValido:
        tempQ, R = decomposicaoQR(tempA)
        Q = Q*tempQ # acumular matriz Q
        oldA = tempA
        tempA = tempQ.transpose()*tempA*tempQ

        if toleravel(oldA,tempA, tol):
            nValido = 0

    return tempA, Q


def main():
    print "\n################## SEJA BEM-VINDO! ##################"
    print "Sistema para o método QR\n"
    iniciar = raw_input("Tecle [ENTER] para iniciar\n")

    A, tol = iniciarSistema()

    tempA, Q = algoritmoQR(A, tol)
    testarAutovetores(A, Q)
    A, tempA, Q = arredondar(A, tempA, Q)

    imprimirNaTela(A, tempA, Q)
    imprimirEmArquivo(A, tempA, Q)
main()
