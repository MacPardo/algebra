'''
para executar o programa digite no terminal:
python3 nome_do_programa.py

nota: os cálculos não foram feitos com frações,
mas com números do tipo double, portanto os resultados
são aproximações das respostas corretas
'''

from copy import deepcopy
from fractions import Fraction
from math import sqrt

def print_matriz(matriz):
    for i in matriz:
        for j in i:
            print(j, end = '\t')
        print()

def solve(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        total = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            total += mul * solve(m, sign * matrix[0][i])
        return total

def inverter_matriz(matriz):

    matriz = deepcopy(matriz)

    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

    return matriz

def to_versor(vetor):
    vetor = deepcopy(vetor)
    modulo = 0
    for i in vetor:
        modulo += i**2
    modulo = sqrt(modulo)
    for i in range(len(vetor)):
        vetor[i] /= modulo
    return vetor

def produto_interno(a, b):
    produto = 0
    for i in range(len(a)):
        produto += a[i] * b[i]
    return produto

def projecao(a, b):
    #calcula a projecao de A em B
    p_interno = produto_interno(a,b)
    b = deepcopy(b)
    for i in range(len(b)):
        b[i] *= p_interno
    return b

def ortonormalizacao(vetores):
    #vetores é uma matriz de vetores

    ortonormalizados = []
    #ortonormalizados é uma matriz dos vetores após
    #o processo de ortonormalização

    for i in range(len(vetores)):
        projecao_soma = 0
        for j in range(i):
            

matriz = [
    [2,3,5,7],
    [11,13,17,19],
    [23,29,31,41],
    [43,47,53,59]
]
