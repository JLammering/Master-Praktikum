import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy import constants
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)


def fitfunktion_int(omega, k):
    return 1/(omega * k)


def fitfunktion_diff(omega, k):
    return omega*k


def plot(x, y, file, R, C, fitfunktion, k_guess, x_fit, xlim=None, ylim=None):
    plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
    xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='x', label='Messwerte')

    # fitten:
    params, covariance = curve_fit(fitfunktion, unp.nominal_values(x),
                                   unp.nominal_values(y),
                                   p0=[k_guess])
    errors = np.sqrt(np.diag(covariance))
    print('k= ', params[0], '±', errors[0])
    k = ufloat(params[0], errors[0])

    print('Abweichung von R*C = ', abweichungen(R*C, k), '%')
    x_fit = np.linspace(x_fit[0], x_fit[1])
    plt.plot(x_fit, fitfunktion(x_fit, *params), label='Fit')

    if xlim is not None:
        plt.xlim(xlim[0], xlim[1])
        plt.ylim(ylim[0], ylim[1])
    xlabel = r'$\omega\:/\:\si{\hertz}$'
    ylabel = r"$V'$"
    #xlabel, ylabel = 'test', 'test'
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc='best')

    # in matplotlibrc leider (noch) nicht möglich
    plt.tight_layout(pad=0.2, h_pad=1.08, w_pad=1.08)
    plt.savefig('build/'+file+'.pdf')
    plt.close()


if __name__ == '__main__':
    #integrator
    C_int = ufloat(970e-9, 10e-9)#nF
    R_int = ufloat(99.7e3, 0.5e3)#kohm
    print('R*C = ', C_int*R_int)
    nu_int, U_a_int, U_1_int = np.genfromtxt('daten/integrator.txt', unpack='True')
    ind_sort = np.argsort(nu_int)
    werteZuTabelle(2*np.pi*noms(nu_int)[ind_sort], noms(U_a_int)[ind_sort], noms(U_1_int)[ind_sort].astype('int'), noms(U_a_int/U_1_int)[ind_sort], rundungen=[2, 1, 0, 2])
    U_a_int = unp.uarray(U_a_int, 5)
    U_1_int = unp.uarray(U_1_int, 5)
    nu_int = unp.uarray(nu_int, 5)
    plot(2*np.pi*nu_int, U_a_int/U_1_int, 'integrator', R_int, C_int, fitfunktion_int, 0.1, (4, 1000), (0, 990), (0, 0.6))

    #Differentiator
    C_diff = ufloat(970e-9, 10e-9)#nF
    R_diff = ufloat(1.002e3, 0.05e3)#kohm
    print('R*C = ', C_diff*R_diff)
    nu_diff, U_a_diff, U_1_diff = np.genfromtxt('daten/differentiator.txt', unpack='True')
    ind_sort = np.argsort(nu_diff)
    werteZuTabelle(2*np.pi*noms(nu_diff)[ind_sort], noms(U_a_diff)[ind_sort], noms(U_1_diff)[ind_sort].astype('int'), noms(U_a_diff/U_1_diff)[ind_sort], rundungen=[2, 1, 0, 2])
    U_a_diff = unp.uarray(U_a_diff, 5)
    U_1_diff = unp.uarray(U_1_diff, 5)
    nu_diff = unp.uarray(nu_diff, 5)
    plot(2*np.pi*nu_diff, U_a_diff/U_1_diff, 'differentiator', R_diff, C_diff, fitfunktion_diff, 0.01, (-100, 7000), (-1, 6900), (-0.2, 7))
