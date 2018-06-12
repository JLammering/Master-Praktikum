import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp


def plotSpektrum(nu_M, spannung, V_N, delta_nu):

    # plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
    # xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='kx', label='Messwerte')

    spannung /= V_N**2
    x = nu_M
    y = spannung/delta_nu
    plt.plot(x, y, 'kx', label='Messwerte')
    plt.xlabel(r'$\nu_\text{M}\:/\: \si{\kilo\hertz}$')
    plt.ylabel(r'$U_ \:/\: \si{\volt}$')
    plt.legend(loc='best')

    # in matplotlibrc leider (noch) nicht möglich
    plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
    plt.savefig('build/plotphase.pdf')
    plt.close()


if __name__ == '__main__':
    nu_M, delta_nu, sigma_delta_nu, spannung, V_N = np.genfromtxt('daten/oxidkurveband.txt',
                                                                  unpack='True')
    plotSpektrum(nu_M, spannung, V_N, delta_nu)
    werteZuTabelle(kreisfrequenz, spannung,
                   rundungen=[3, 1])
