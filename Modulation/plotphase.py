import matplotlib.pyplot as plt
import numpy as np
from functions import linmean
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp


def plotphase(kreisfrequenz, spannung):
    verschiebung = 250e-9  # s
    kreisfrequenz *= 10**(6)
    umlaufdauer = (2*np.pi)/kreisfrequenz
    phase = 2*np.pi*verschiebung/umlaufdauer
    print('Umlaufdauer=', umlaufdauer)
    print('Phase= ', phase)
    x = np.cos(phase)

    plt.plot(x, spannung, 'kx', label='Messwerte')
    plt.xlabel(r'$\cos(\phi)$')
    plt.ylabel(r'$U \:/\: \si{\volt}$')
    plt.legend(loc='best')

    # in matplotlibrc leider (noch) nicht möglich
    plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
    plt.savefig('build/plotphase.pdf')
    plt.close()


if __name__ == '__main__':
    kreisfrequenz, spannung = np.genfromtxt('daten/gleichspannungphase.txt', unpack='True')
    plotphase(kreisfrequenz, spannung)
