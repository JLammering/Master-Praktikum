import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
import scipy.integrate as integrate

def plotDurchlass(spannung, nu, V_N, amplitude, dateiname):
    # plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
    # xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='kx', label='Messwerte')
    amplitude *= 10**(-3)  # abschwächer

    if V_N is not None:  # umrechnen da verschieden verstärkt
        spannung /= V_N**2  # auf V_N = 1 normieren
        plt.yscale('log')
    spannung /= amplitude**2
    x = unp.uarray(nu, 0.01)
    y = unp.uarray(spannung, 0.005)
    plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
                 xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='kx', label='Messwerte')
    #plt.xlabel(r'$\nu/\si{\kilo\hertz}$')
    #plt.ylabel(r'$U_\text{A}^2 \:/\: \si{\volt\squared}$')
    plt.legend(loc='best')

    # in matplotlibrc leider (noch) nicht möglich
    plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
    plt.savefig('build/plotdurchlass'+dateiname+'.pdf')
    plt.close()

    # integration:
    x *= 10**(3)  # auf Hz umrechnen
    int = (max(x) - min(x))/len(x) * sum(y)
    print("Integral der Durchlasskurve= ", int)
    int_trapez = np.trapz(noms(y), x=noms(x))
    print("Integral mit trapz = ", int_trapez)
    int_scipy = integrate.simps(noms(y), x=noms(x))
    print("Integral mit scipy = ", int_scipy)
    int = ufloat(int_scipy, 0)
    file = open("build/eichung"+dateiname+".txt", "w")
    file.write(str(int.n))
    file.write(" ")
    file.write(str(int.s))
    file.close()


if __name__ == '__main__':
    nu, spannung = np.genfromtxt('daten/eichung.txt', unpack='True')
    werteZuTabelle(nu, spannung,
                   rundungen=[3, 3])
    plotDurchlass(spannung, nu, None, 0.2, "einfach")

    nu2, spannung2, V_N2 = np.genfromtxt('daten/eichung2.txt', unpack='True')
    print("Datentyp=", type(V_N2[0]), type(spannung2[0]))
    werteZuTabelle(nu2, spannung2, V_N2.astype(int),
                   rundungen=[3, 3, 0])
    plotDurchlass(spannung2, nu2, V_N2, 0.5, "Korrelator")
