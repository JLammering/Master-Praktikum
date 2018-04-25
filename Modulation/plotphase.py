import matplotlib.pyplot as plt
import numpy as np
from functions import linmean
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp


def plotphase(kreisfrequenz, spannung):
    verschiebung = 250e-9  # s
    kreisfrequenz = unp.uarray(kreisfrequenz, 0.005)
    spannung = unp.uarray(spannung, 0.001)
    kreisfrequenz *= 10**(6)
    umlaufdauer = (2*np.pi)/kreisfrequenz
    phase = 2*np.pi*verschiebung/umlaufdauer
    # print('Umlaufdauer=', umlaufdauer)
    # print('Phase= ', phase)
    x = unp.cos(phase)
    y = spannung

    plt.errorbar(unp.nominal_values(x), unp.nominal_values(y), xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='kx', label='Messwerte')
    plt.xlabel(r'$\cos(\Delta\phi)$')
    plt.ylabel(r'$U \:/\: \si{\volt}$')
    plt.legend(loc='best')

    # in matplotlibrc leider (noch) nicht möglich
    plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
    plt.savefig('build/plotphase.pdf')
    plt.close()

    return phase


def werteZuTabelle(*werteArray, rundungen):
    ''' Funktion um Werte in Tabelle auszugeben'''

    if len(werteArray) != len(rundungen):  # Fehleruntersuchung
        print('Dimension werteArray= ', len(werteArray), ' != ',
              'Dimension rundungen= ', len(rundungen))
        return

    for i in range(len(werteArray[0])):  # geht durch die Zeilen
        for k in range(len(werteArray)):  # geht durch die Spalten
            if k == len(werteArray)-1:  # am Ende Backslashes
                print(round(werteArray[k][i], rundungen[k]), end='\\\\\n')
            else:  # vorher mit Undzeichen
                print(round(werteArray[k][i], rundungen[k]), end=' & ')


if __name__ == '__main__':
    kreisfrequenz, spannung = np.genfromtxt('daten/gleichspannungphase.txt', unpack='True')
    phase = plotphase(kreisfrequenz, spannung)
    werteZuTabelle(kreisfrequenz, spannung, unp.nominal_values(phase),
                   rundungen=[3, 1, 2])  # , unp.nominal_values(phase))
