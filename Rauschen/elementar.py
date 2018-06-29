import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy import constants
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)


def fitfunktion(I, m):
    return m*I


def plotElement(anodenstrom, spannung, V_N, R):
    spannung /= (V_N**2 * 1000**2 * 10)  # verstärkung rausrechnen
    x = anodenstrom*10**(-3)
    y = spannung/(R**2)  # I^2 bestimmt
    plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
    xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='kx', label='Messwerte')

    # fitten:
    params, covariance = curve_fit(fitfunktion, unp.nominal_values(x),
                                   unp.nominal_values(y),
                                   p0=[1])
    errors = np.sqrt(np.diag(covariance))
    print('m= ', params[0], '±', errors[0])
    m = ufloat(params[0], errors[0])
    x_fit = np.linspace(-0.0001, max(noms(x))+0.001)
    plt.plot(x_fit, fitfunktion(x_fit, *params), label='Fit')

    plt.xlim(0, 0.0045)
    plt.ylim(0, 1.75e-17)
    plt.xlabel(r'$I_0 \:/\: \si{\ampere}$')
    plt.ylabel(r'$I^2 \:/\: \si{\ampere\squared}$')
    delta_nu = ufloat(24.4, 0.4)
    delta_nu *= 10**3
    e0 = m/(2*delta_nu)
    print("e0 = ", e0)
    e0theorie = ufloat(constants.physical_constants["elementary charge"][0],
               constants.physical_constants["elementary charge"][2])
    print("Abweichung von Theorie= ", abweichungen(e0theorie, e0))
    plt.legend(loc='best')

    # in matplotlibrc leider (noch) nicht möglich
    plt.tight_layout(pad=0.2, h_pad=1.08, w_pad=1.08)
    plt.savefig('build/plotElement.pdf')
    plt.close()


if __name__ == '__main__':
    anodenstrom, spannung, V_N = np.genfromtxt('daten/elementar.txt',
                                               unpack='True')
    werteZuTabelle(anodenstrom, spannung, V_N.astype('int'), rundungen=[1, 3, 0])
    plotElement(unp.uarray(anodenstrom, 0.1), unp.uarray(spannung, 0.05), V_N, ufloat(4680, 1))
    # werteZuTabelle(kreisfrequenz, spannung,
    #                rundungen=[3, 1])
