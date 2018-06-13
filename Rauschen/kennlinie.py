import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp


def plotKennlinie(anodenstrom, anodenspannung, dateiname, heizstrom):

    # plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
    # xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='kx', label='Messwerte')
    plt.plot(anodenstrom, anodenspannung, 'kx', label=('Messwerte bei Iheiz'+heizstrom))
    plt.xlabel(r'$I \:/\: \si{\milli\ampere}$')
    plt.ylabel(r'$U \:/\: \si{\volt}$')
    #plt.ylim(0, 0.9)
    plt.legend(loc='best')

    # in matplotlibrc leider (noch) nicht möglich
    plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
    plt.savefig('build/plotKennlinie'+dateiname+'.pdf')
    plt.close()


if __name__ == '__main__':
    anodenstrom1, anodenspannung1 = np.genfromtxt('daten/kennlinie1.txt',
                                                unpack='True')
    plotKennlinie(anodenstrom1, anodenspannung1, "1", "0.9 A")


    anodenstrom2, anodenspannung2 = np.genfromtxt('daten/kennlinie2.txt',
                                                unpack='True')
    plotKennlinie(anodenstrom2, anodenspannung2, "2", "1 A")

    anodenstrom3, anodenspannung3 = np.genfromtxt('daten/kennlinie3.txt',
                                                unpack='True')
    plotKennlinie(anodenstrom3, anodenspannung3, "3", "0.95 A")
    # werteZuTabelle(kreisfrequenz, spannung,
    #                rundungen=[3, 1])
