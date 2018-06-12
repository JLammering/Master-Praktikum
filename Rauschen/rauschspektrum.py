import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp


def plotSpektrum(nu_M, spannung, V_N, delta_nu, dateiname):

    # plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
    # xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='kx', label='Messwerte')
    delta_nu *= 10**3

    spannung /= V_N**2
    x = nu_M
    y = spannung/delta_nu
    plt.plot(x, y, 'kx', label='Messwerte')
    plt.xlabel(r'$\nu_\text{M}\:/\: \si{\kilo\hertz}$')
    plt.ylabel(r'$W \:/\: a.u.$')
    plt.legend(loc='best')

    # in matplotlibrc leider (noch) nicht möglich
    plt.tight_layout(pad=0.5, h_pad=1.2, w_pad=1.08)
    plt.savefig('build/plotRauschspektrum'+dateiname+'.pdf')
    plt.close()


def commuteDeltaNu(nu_M):
    delta_nu = np.ones(len(nu_M))

    for i, elem in enumerate(nu_M):
        if elem >= 0.01 and elem < 0.1:
            delta_nu[i] = 0.15*elem - 0.3
        elif elem >= 0.1 and elem < 10:
            delta_nu[i] = 0.140*elem + 0.7
        elif elem >= 10 and elem < 50:
            delta_nu[i] = 0.135*elem + 0.05
        if elem >= 50 and elem < 100:  # R=2200ohm
            delta_nu[i] = 0.115*elem + 1.05

    return delta_nu


if __name__ == '__main__':
    nu_M, delta_nu, sigma_delta_nu, spannung, V_N = np.genfromtxt('daten/oxidkurveband.txt',
                                                                  unpack='True')
    plotSpektrum(nu_M, spannung, V_N, delta_nu, "Oxid")

    
    # werteZuTabelle(kreisfrequenz, spannung,
    #                rundungen=[3, 1])
