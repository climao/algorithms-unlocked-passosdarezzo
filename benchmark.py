# -*- coding: utf-8 -*-

import box as b
import time
import sys
from random import randint

def benchmark(function, *args):
    '''
    Calculate the time to execute the function.

    Parameters
    ----------
    arg0 : function
        Function to be tested
    arg1 : object
        Arguments that will be applied in the function

    Returns
    -------
    None

    Example
    -------
    >>> benchmark_find(function, [12,85,5,1,98,54,32,8], 5)
    '''
    start = time.clock()
    indice = function(*args)
    stop = time.clock()

    caixa = b.Box()
    caixa.add_text_line(function.__name__)
    caixa.add_text_line('Return: ' + str(indice))
    caixa.add_text_line('Execution Time: ' + str(stop-start))
    caixa.print_box()

def generate_random_list(size, min=1, max=1000):
    '''
    Generates a list of random numbers between a range.

    Parameters
    ----------
    arg0 : int
        Size of the list
    arg1 : int
        Initial value of the range
    arg2 : int
        Last value of the range

    Returns
    -------
    list
        A list of a defined size with values between the determined range

    Example
    -------
    >>> generate_random_list(10, 1, 100)
    '''
    arranjo = []
    for i in range(size):
        arranjo.append(randint(min, max))

    return arranjo
