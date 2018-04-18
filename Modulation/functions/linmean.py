import numpy as np
from uncertainties import ufloat


def linregress(x, y):
    '''calculate a linear regression and returns slope and intercept
    with error'''
    assert len(x) == len(y)

    x, y = np.array(x), np.array(y)

    N = len(y)
    Delta = N * np.sum(x**2) - (np.sum(x))**2

    A = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / Delta
    B = (np.sum(x**2) * np.sum(y) - np.sum(x) * np.sum(x * y)) / Delta

    sigma_y = np.sqrt(np.sum((y - A * x - B)**2) / (N - 2))

    A_error = sigma_y * np.sqrt(N / Delta)
    B_error = sigma_y * np.sqrt(np.sum(x**2) / Delta)

    return A, A_error, B, B_error


def mittelwert(sigma):
    '''calculate mean of values with errors'''
    laenge = len(sigma)
    sum = ufloat(0, 0)
    for i in range(0, laenge):
        sum += sigma[i]
    return (1/laenge)*sum
