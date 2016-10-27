'''
Marcos Theophilo Gobbi Adamczuk

---------->para executar o programa digite no terminal:
python3 nome_do_programa.py

nota: os cálculos não foram feitos com frações,
mas com números do tipo double, portanto os resultados
são aproximações das respostas corretas
'''

from copy import deepcopy
from math import sqrt

def print_matriz(matriz):
    for i in matriz:
        for j in i:
            print('%.1f'%j, end = '\t')
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

def vetor_subtracao(a, b):
    #faz a - b
    soma = []
    for i in range(len(a)):
        soma.append(a[i] - b[i])
    return soma

def vetor_soma(a, b):
    #faz a + b
    soma = []
    print(a,b)
    for i in range(len(a)):
        soma.append(a[i] + b[i])
    return soma

def ortonormalizacao_completa(vetores):

    ortonormalizados = []

    for i in range(len(vetores)):

        projecao_soma = []
        for j in range(len(vetores[0])): projecao_soma.append(0)

        for j in range(i):
            projecao_soma = vetor_soma(projecao_soma, projecao(vetores[i], vetores[j]))

        v = vetor_subtracao(vetores[i], projecao_soma)
        v = to_versor(v)

        ortonormalizados.append(v)

    return ortonormalizados

matriz = [
    [2,3,5,7],
    [11,13,17,19],
    [23,29,31,41],
    [43,47,53,59]
]


vetores = [
    [1,2,3,4,5],
    [1,2,3,4,4],
    [1,1,3,4,3],
    [1,1,2,4,2],
    [1,1,1,1,1]
]
