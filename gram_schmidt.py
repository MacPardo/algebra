'''
Marcos Theophilo Gobbi Adamczuk

---------->PARA EXECUTAR O PROGRAMA digite no terminal:
python3 nome_do_programa.py

nota: os cálculos não foram feitos com frações,
mas com números do tipo double, portanto os resultados
são aproximações das respostas corretas
'''

from copy import deepcopy
from math import sqrt

def print_matriz(matriz): #ok
    for i in matriz:
        for j in i:
            print('%.1f'%j, end = '\t')
        print()

def solve(matrix, mul): #ok
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

def versor(vetor): #ok
    vetor = deepcopy(vetor)
    modulo = 0
    for i in vetor:
        modulo += i**2
    modulo = sqrt(modulo)
    for i in range(len(vetor)):
        vetor[i] /= modulo
    return vetor

def produto_interno(a, b): #ok
    produto = 0
    for i in range(len(a)):
        produto += a[i] * b[i]
    return produto

def projecao(a, b): #ok
    #calcula a projecao de A em B
    p_interno = produto_interno(a,b)
    b = deepcopy(b)
    for i in range(len(b)):
        b[i] *= p_interno
    return b

def vetor_subtracao(a, b): #ok
    #faz a - b
    soma = []
    for i in range(len(a)):
        soma.append(a[i] - b[i])
    return soma

def vetor_soma(a, b): #ok
    #faz a + b
    soma = []
    for i in range(len(a)):
        soma.append(a[i] + b[i])
    return soma

def ortonormalizacao_completa(vetores): #ok
    ortonormalizados = []

    for i in range(len(vetores)):

        projecoes = []
        for j in range(len(vetores[0])):
            projecoes.append(0)

        for j in range(i):
            projecoes = vetor_soma(projecoes, projecao(vetores[i], ortonormalizados[j]))

        ortonormalizados.append(versor(vetor_subtracao(vetores[i], projecoes)))

    return ortonormalizados

def ler_arquivo(nome_arquivo):
    linhas = open(nome_arquivo, 'r').readlines()

    vetores = []

    for i in linhas:
        if len(i) == 0 or i[0] != '(': continue
        vetor = []
        num_string = ""
        for j in i:
            if j in "(,)":
                if(num_string != ""): vetor.append(int(num_string))
                num_string = ''
            elif j in "0123456789":
                num_string += j
        vetores.append(vetor)

    return vetores

def main():
    nome_arquivo = "ortogonaliza.txt"
    vetores = ler_arquivo(nome_arquivo)

    linhas_originais = open(nome_arquivo, 'r').readlines()

    linhas = []

    if(solve(vetores, 1) != 0):
        resposta = ortonormalizacao_completa(vetores)
        for linha in resposta:
            nova_linha = []
            linhas.append(nova_linha)
            nova_linha.append('(')
            for numero in range(len(linha)):
                nova_linha.append('%.2f' % linha[numero])
                if numero < len(linha) - 1: nova_linha.append(',')
            nova_linha.append(')')
    else:
        linhas.append(["OS VETORES NAO FORMAM BASE"])

    escrever = open(nome_arquivo, 'w')
    for linha in linhas_originais:
        escrever.write(linha)
    escrever.write('\n')
    for linha in linhas:
        escrever.write(''.join(linha) + '\n\n')
    escrever.close()

if __name__ == '__main__': main()
