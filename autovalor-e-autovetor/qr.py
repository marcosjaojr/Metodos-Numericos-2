# -*- coding: utf-8 -*-
from numpy import *
# Método QR
# Aluno: Marcos José Augusto de Oliveira Júnior
# Matricula: 370021

def iniciarMatriz():
    arquivo = open('matriz.db', 'r')
    return matrix([ map(float,linha.split('|')[0].split(',')) for linha in arquivo ])

def arredondar(A, tempA, Q):
    fator = 4
    return A.round(fator).tolist(), tempA.round(fator).tolist(), Q.round(fator).tolist()

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
    # TODO: substituir for por while com critério de parada
    tempA = A
    Q = identity(len(A))
    for i in range(0,tol):
          tempQ, R = decomposicaoQR(tempA)
          Q = Q*tempQ # acumular matriz Q
          tempA = tempQ.transpose()*tempA*tempQ

    return tempA, Q
    

def main():
    print "\n################## SEJA BEM-VINDO! ##################"
    print "Sistema para o método QR\n"
    iniciar = raw_input("Tecle [ENTER] para iniciar\n")
    
    A = iniciarMatriz()
    # TODO: Ler tolerância do arquivo de texto

    tempA, Q = algoritmoQR(A, 30)
    testarAutovetores(A, Q)
    A, tempA, Q = arredondar(A, tempA, Q)
    
    imprimirNaTela(A, tempA, Q)
    imprimirEmArquivo(A, tempA, Q)
main()
