# -*- coding: utf-8 -*-

import time
import sys
from random import randint

def benchmark(funcao, *arranjo, **procurado):
    '''
    '''
    start = time.clock()
    indice = funcao(*arranjo, **procurado)
    stop = time.clock()

    print '\n*************************************\n' + funcao.__name__
    print 'Retorno: ' + str(indice)
    print 'Tempo de execucao: ' + str(stop-start)

def benchmark_sort(funcao, *arranjo):
    '''
    '''
    start = time.clock()
    indice = funcao(*arranjo)
    stop = time.clock()

    print '\n*************************************\n' + funcao.__name__
    print 'Tempo de execucao: ' + str(stop-start)
    return indice

def generate_random_list(size, min=1, max=1000):
    '''
    Gera uma lista do tamanho especificado de elementos aleatórios.
    '''
    arranjo = []
    for i in range(size):
        arranjo.append(randint(min, max))

    return arranjo

def linear_search(arranjo, procurado):
    '''
    Realiza uma busca linear do valor procurado e retorna o indice.
    Caso não localize o valor procurado retorna -1.
    '''
    retorno = -1
    for i in range(len(arranjo)):
        if arranjo[i] == procurado:
            retorno = i

    return retorno

def better_linear_search(arranjo, procurado):
    '''
    Realiza uma busca linear otimizada do valor procurado e retorno o indice.
    Caso não localize o valor procurado retorna -1.
    '''
    for i in range(len(arranjo)):
        if arranjo[i] == procurado:
            return i

    return -1

def sentinel_linear_search(arranjo, procurado):
    '''
    Realiza uma busca linear sem necessitar verificar o fim do array porque
    utiliza um sentinela para a condição de parada do laço.
    Caso não localize retorna -1.
    '''
    n = len(arranjo) - 1
    ultimo = arranjo[n]
    arranjo[n] = procurado

    i = 0
    while arranjo[i] != procurado:
        i += 1

    arranjo[n] = ultimo
    if i < n or arranjo[n] == procurado:
        return i

    return -1

def binary_search(arranjo, procurado):
    '''
    '''
    p = 0
    r = len(arranjo) - 1
    while p <= r:
        q = (p + r)/2

        if arranjo[q] == procurado:
            return q
        elif arranjo[q] > procurado:
            r = q - 1
        else:
            p = q + 1

    return -1

def selection_sort(arranjo):
    '''
    '''
    for i in range(len(arranjo)):
        for j in range(i + 1, len(arranjo)):
            if arranjo[i] > arranjo[j]:
                arranjo[i], arranjo[j] = arranjo[j], arranjo[i]
    return arranjo

def bubble_sort(arranjo):
    '''
    Retorna uma lista ordenada de valores.
    Melhor O(n)
    Pior O(n^2)
    '''
    n = len(arranjo)

    for i in range(n):
        for j in range(i + 1, n):
            if arranjo[i] > arranjo[j]:
                arranjo[i], arranjo[j] = arranjo[j], arranjo[i]

    return arranjo

def insertion_sort(arranjo):
    '''
    '''
    n = len(arranjo)

    for indice in range(1, n):
        chave = arranjo[indice]
        j = indice - 1

        while j >= 0 and arranjo[j] > chave:
            arranjo[j + 1] = arranjo[j]
            j -= 1

        arranjo[j + 1] = chave
    return arranjo

def merge_sort(arranjo):
    '''
    Ordena o arranjo do menor para o maior.
    Pior e Mehor caso: 0(nlg n)
    Como é realizada diversas cópias de partes do vetor, esse algoritmo
    utiliza-se de mais memória em comparação com os outros algoritmos de ordenação.
    '''
    p = 0
    r = len(arranjo)

    if p >= r:
        return arranjo

    q = (p + r)/2
    merge_sort(a[p:q])
    merge_sort(a[q:r])
    merge(arranjo, p, q, r)


#**************************************************

a = generate_random_list(45, 0, 60)

benchmark(linear_search, a, a[40])

benchmark(better_linear_search, a, a[40])

benchmark(sentinel_linear_search, a, a[40])

#benchmark_sort(selection_sort, a)

a = benchmark_sort(insertion_sort, a)
print(a)
benchmark(binary_search, a, a[40])

