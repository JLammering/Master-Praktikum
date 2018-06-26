import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp


def plotKennlinie(anodenstrom, anodenspannung, dateiname, heizstrom):
    y = unp.uarray(anodenstrom, 0.05)
    x = unp.uarray(anodenspannung, 5)
    plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
                 xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='kx', label='Messwerte')
    # plt.plot(anodenstrom, anodenspannung, 'kx', label=('Messwerte'))
    plt.xlabel(r'$I \:/\: \si{\milli\ampere}$')
    plt.ylabel(r'$U \:/\: \si{\volt}$')
    # plt.ylim(0, 0.9)
    plt.legend(loc='best')

    # in matplotlibrc leider (noch) nicht möglich
    plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
    plt.savefig('build/plotKennlinie'+dateiname+'.pdf')
    plt.close()


if __name__ == '__main__':
    anodenspannung1, anodenstrom1 = np.genfromtxt('daten/kennlinie1.txt',
                                                  unpack='True')
    print("0.9A")
    werteZuTabelle(anodenstrom1, anodenspannung1.astype(int),
                   rundungen=[1, 0])
    plotKennlinie(anodenstrom1, anodenspannung1, "1", "0.9 A")



    anodenspannung2, anodenstrom2 = np.genfromtxt('daten/kennlinie2.txt',
                                                  unpack='True')
    print("1A")
    werteZuTabelle(anodenstrom2, anodenspannung2.astype(int),
                   rundungen=[1, 0])
    plotKennlinie(anodenstrom2, anodenspannung2, "2", "1 A")

    anodenspannung3, anodenstrom3 = np.genfromtxt('daten/kennlinie3.txt',
                                                  unpack='True')
    print("0.95A")
    werteZuTabelle(anodenstrom3, anodenspannung3.astype(int),
                   rundungen=[1, 0])
    plotKennlinie(anodenstrom3, anodenspannung3, "3", "0.95 A")
    # werteZuTabelle(kreisfrequenz, spannung,
    #                rundungen=[3, 1])
