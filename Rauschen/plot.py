import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp


def plotphase(kreisfrequenz, spannung):

    # plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
    # xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='kx', label='Messwerte')
    plt.plot(kreisfrequenz, spannung, 'kx', label='Messwerte')
    plt.xlabel(r'$\cos(\Delta\phi)$')
    plt.ylabel(r'$U \:/\: \si{\volt}$')
    plt.legend(loc='best')

    # in matplotlibrc leider (noch) nicht möglich
    plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
    plt.savefig('build/plotphase.pdf')
    plt.close()


if __name__ == '__main__':
    kreisfrequenz, spannung = np.genfromtxt('../Modulation/daten/gleichspannungphase.txt',
                                            unpack='True')
    plotphase(kreisfrequenz, spannung)
    werteZuTabelle(kreisfrequenz, spannung,
                   rundungen=[3, 1])
