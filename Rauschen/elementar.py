import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp


def plotElement(anodenstrom, spannung, V_N):

    # plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
    # xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='kx', label='Messwerte')
    spannung /= V_N**2
    plt.plot(anodenstrom, spannung, 'kx', label='Messwerte')
    plt.xlabel(r'$I \:/\: \si{\milli\ampere}$')
    plt.ylabel(r'$U \:/\: \si{\volt\squared}$')
    plt.legend(loc='best')

    # in matplotlibrc leider (noch) nicht möglich
    plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
    plt.savefig('build/plotElement.pdf')
    plt.close()


if __name__ == '__main__':
    anodenstrom, spannung, V_N = np.genfromtxt('daten/elementar.txt',
                                               unpack='True')
    plotElement(anodenstrom, spannung, V_N)
    # werteZuTabelle(kreisfrequenz, spannung,
    #                rundungen=[3, 1])
