import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp


def plotDurchlass(spannung, nu):
    amplitude = 0.2
    # plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
    # xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='kx', label='Messwerte')
    spannung /= amplitude**2
    plt.plot(nu, spannung, 'kx', label='Messwerte')
    #plt.xlabel(r'$\nu/\si{\kilo\hertz}$')
    #plt.ylabel(r'$U_\text{A}^2 \:/\: \si{\volt\squared}$')
    plt.legend(loc='best')

    # in matplotlibrc leider (noch) nicht möglich
    plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
    plt.savefig('build/plotdurchlass.pdf')
    plt.close()

    # integration:
    int = (max(nu) - min(nu))/len(nu) * sum(spannung) * 10**6
    print("Integral der Durchlasskurve= ", int)
    file = open("build/eichung1.txt", "w")
    file.write(str(int))
    file.close()


if __name__ == '__main__':
    nu, spannung = np.genfromtxt('daten/eichung.txt', unpack='True')
    plotDurchlass(spannung, nu)
    # werteZuTabelle(kreisfrequenz, spannung,
    #               rundungen=[3, 1])
