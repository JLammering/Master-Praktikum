import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)


def fitfunktion_pol(phi, I_0, phi_verschieb, m):
    return I_0*(np.cos(m*phi + phi_verschieb)**2)


def fitfunktion_grundmode(x, I_0, r_verschieb, omega):
    return I_0*np.exp((-2*(x+r_verschieb)**2)/(omega**2))


def fitfunktion_transmode(x, I_01, r_verschieb1, omega1,
                          I_02, r_verschieb2, omega2):
    return (I_01*np.exp((-2*(x+r_verschieb1)**2)/(omega1**2)) +
            I_02*np.exp((-2*(x+r_verschieb2)**2)/(omega2**2)))


def plot(x, y, label, filename, x_label, y_label, fitfunktion, p_list, pname_list):
    plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
                 xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='kx', label='Messwerte '+label)

    werte_start = 0
    werte_ende = len(x)-1
    params, covariance = curve_fit(fitfunktion, unp.nominal_values(x[werte_start:werte_ende]),
                                   unp.nominal_values(y[werte_start:werte_ende]),
                                   p0=p_list)
    errors = np.sqrt(np.diag(covariance))
    for i, name in enumerate(pname_list):
        print('{0} = {1} ± {2}'.format(name, round(params[i], 5), round(errors[i], 5)))
    # print('I_0= ', params[0], '±', errors[0])
    # print('phi_verschieb= ', params[1], '±', errors[1])
    # print('m = ', params[2], '±', errors[2])
    # m = ufloat(params[0], errors[0])
    x_fit = np.linspace(noms(x[0])-(noms(x[-1]))*0.1, (noms(x[-1]))*1.1, 1000)
    label = 'hallo'
    plt.plot(x_fit, fitfunktion(x_fit, *params), label='Fit ' + label)

    # plotting
    plt.legend(loc='best')
    plt.xlim(noms(x[0])-(noms(x[-1]))*0.06, (noms(x[-1]))*1.06)

    #plt.xlabel(x_label)
    #plt.ylabel(y_label)
    plt.savefig('build/{}.pdf'.format(filename))
    plt.close()


if __name__ == '__main__':
    # polarisation
    I = np.genfromtxt('daten/polarisation.txt',
                      unpack='True')
    phi = np.linspace(0, 180, 19)
    phi = unp.uarray(phi, 1)
    I = unp.uarray(I, 0.005)
    plot(phi, I, "Polarisation", "polarisation", "phi", "I", fitfunktion_pol,
         [0.8, 100, 0], ["I_0", "phi_verschieb", "m"])

    # moden
    x, I = np.genfromtxt('daten/tem00.txt',
                         unpack='True')
    x = unp.uarray(x, 0.5)
    I = unp.uarray(I, 0.01)

    werteZuTabelle(noms(x).astype(int), noms(I), rundungen=[0, 3])
    plot(x, I, r'TEM$_{00}$', 'grundmode', r'$x/\si{\milli\meter}$',
         r'$I/\si{\micro\ampere}$', fitfunktion_grundmode, [2.97, 13, 50],
         ["I_0", "x_0", "omega"])

    x, I = np.genfromtxt('daten/tem01.txt',
                         unpack='True')
    x = unp.uarray(x, 0.5)
    I = unp.uarray(I, 0.01)
    werteZuTabelle(noms(x).astype(int), noms(I), rundungen=[0, 3])
    plot(x, I, r'TEM$_{00}$', 'transmode', r'$x/\si{\milli\meter}$',
         r'$I/\si{\micro\ampere}$', fitfunktion_transmode,
         [0.12, -5, 10, 0.08, -20, 10],
         ["I_01", "x_01", "omega1", "I_02", "x_02", "omega2"])