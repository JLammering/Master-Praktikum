import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp


def plotDurchlass(spannung, nu, V_N, amplitude, dateiname):
    # plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
    # xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='kx', label='Messwerte')
    print('max U^2= ', max(spannung))
    amplitude *= 10**(-3)  # abschwächer

    if V_N is not None:  # umrechnen da verschieden verstärkt
        spannung /= V_N**2  # auf V_N = 1 normieren
        plt.yscale('log')
    spannung /= amplitude**2
    plt.plot(nu, spannung, 'kx', label='Messwerte')
    #plt.xlabel(r'$\nu/\si{\kilo\hertz}$')
    #plt.ylabel(r'$U_\text{A}^2 \:/\: \si{\volt\squared}$')
    plt.legend(loc='best')

    # in matplotlibrc leider (noch) nicht möglich
    plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
    plt.savefig('build/plotdurchlass'+dateiname+'.pdf')
    plt.close()

    # integration:
    nu *= 10**(3)  # auf Hz umrechnen
    int = (max(nu) - min(nu))/len(nu) * sum(spannung)
    print("Integral der Durchlasskurve= ", int)
    file = open("build/eichung"+dateiname+".txt", "w")
    file.write(str(int))
    file.close()


if __name__ == '__main__':
    nu, spannung = np.genfromtxt('daten/eichung.txt', unpack='True')
    plotDurchlass(spannung, nu, None, 0.2, "einfach")

    nu2, spannung2, V_N2 = np.genfromtxt('daten/eichung2.txt', unpack='True')
    plotDurchlass(spannung2, nu2, V_N2, 0.5, "Korrelator")
    # werteZuTabelle(kreisfrequenz, spannung,
    #               rundungen=[3, 1])
