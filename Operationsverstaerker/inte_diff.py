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


def plot(x, y, file, R, C):
    plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
    xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='x', label='Messwerte')

    # fitten:
    params, covariance = curve_fit(fitfunktion_int, unp.nominal_values(x),
                                   unp.nominal_values(y),
                                   p0=[0.1])
    errors = np.sqrt(np.diag(covariance))
    print('k= ', params[0], '±', errors[0])
    k = ufloat(params[0], errors[0])

    print('Abweichung von R*C = ', abweichungen(R*C, k), '%')
    x_fit = np.linspace(4, 1000)
    plt.plot(x_fit, fitfunktion_int(x_fit, *params), label='Fit')

    plt.xlim(0, 990)
    plt.ylim(0, 0.6)
    xlabel = r'$\omega\:/\:\si{\hertz}$'
    ylabel = r"$V'$"
    xlabel, ylabel = 'test', 'test'
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
    plot(2*np.pi*nu_int, U_a_int/U_1_int, 'integrator', R_int, C_int)
