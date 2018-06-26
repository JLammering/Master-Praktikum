import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy import constants
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)


def fitfunktion(U, m):
    return m*U


def plotWiderstand(widerstand, spannung, V_N, dateiname, T):
    spannung = unp.uarray(spannung, 0.005)
    widerstand = unp.uarray(widerstand, 1)
    y = spannung / V_N**2
    x = widerstand
    plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
                 xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='kx', label='Messwerte')

    # fitten:
    params, covariance = curve_fit(fitfunktion, unp.nominal_values(x),
                                   unp.nominal_values(y),
                                   p0=[0.1])
    errors = np.sqrt(np.diag(covariance))
    print('m= ', params[0], '±', errors[0])
    m = ufloat(params[0], errors[0])
    x_fit = np.linspace(-5, max(noms(x))+1000)
    plt.plot(x_fit, fitfunktion(x_fit, *params), label='Fit')

    # kBoltzmann
    if dateiname == "1" or dateiname == "2":
        int, intf = np.genfromtxt('build/eichungeinfach.txt', unpack='True')
    else:
        int, intf = np.genfromtxt('build/eichungKorrelator.txt', unpack='True')

    int = ufloat(int, intf)
    T = ufloat(296.15, 2)  # K
    k_B = m/(4*int*T)
    print('k_B_', dateiname, " = ", k_B)
    kBTheorie = ufloat(constants.physical_constants["Boltzmann constant"][0],
               constants.physical_constants["Boltzmann constant"][2])
    print("Abweichung von Theorie= ", abweichungen(kBTheorie, k_B))

    plt.xlabel(r'$R/\si{\ohm}$')
    plt.ylabel(r'$U_\text{A} \:/\: \si{\volt\squared}$')
    plt.xlim(0, 1.01*max(noms(x)))
    plt.legend(loc='best')

    # in matplotlibrc leider (noch) nicht möglich
    #plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
    plt.savefig('build/plotWiderstand'+dateiname+'.pdf')
    plt.close()


def rauschzahl(spannung, T, widerstand, delta_nu, V_N):
    k = ufloat(constants.physical_constants["Boltzmann constant"][0],
               constants.physical_constants["Boltzmann constant"][2])
    # e = ufloat(constants.physical_constants["elementary charge"][0],
    #            constants.physical_constants["elementary charge"][2])
    Vges = (1000**2)*(V_N**2)*10
    F = spannung/(4*k*T*widerstand*delta_nu*Vges)
    return F


if __name__ == '__main__':
    widerstand1, spannung1, V_N1 = np.genfromtxt('daten/widerstand1.txt', unpack='True')
    werteZuTabelle(widerstand1, spannung1*10**(-3), V_N1,
                   rundungen=[0, 3, 0])
    plotWiderstand(widerstand1, spannung1*10**(-3), V_N1, "1", ufloat(296.15, 2))

    widerstand2, spannung2, V_N2 = np.genfromtxt('daten/widerstand2.txt', unpack='True')
    werteZuTabelle(widerstand2, spannung2*10**(-3), V_N2,
                   rundungen=[0, 3, 0])
    plotWiderstand(widerstand2*10**3, spannung2 * 10**(-3), V_N2, "2", ufloat(296.15, 2))

    widerstand1Korr, spannung1Korr, V_N1Korr = np.genfromtxt('daten/widerstand1Korr.txt', unpack='True')
    werteZuTabelle(widerstand1Korr, spannung1Korr, V_N1Korr,
                   rundungen=[1, 3, 0])
    plotWiderstand(widerstand1Korr, spannung1Korr, V_N1Korr*10, "1Korr", ufloat(293.15, 2))  # *10 wegen der Verstärkung des selektivverstärkers

    widerstand2Korr, spannung2Korr, V_N2Korr = np.genfromtxt('daten/widerstand2Korr.txt', unpack='True')
    werteZuTabelle(widerstand2Korr, spannung2Korr, V_N2Korr,
                   rundungen=[2, 2, 0])
    plotWiderstand(widerstand2Korr*10**3, spannung2Korr, V_N2Korr*10, "2Korr", ufloat(293.15, 2))

    F = rauschzahl(0.492, ufloat(296.15, 2), 499, 49*10**3, 20)
    F_korr = rauschzahl(ufloat(0.219, 0.01), ufloat(289.15, 2), 500, 0.14*5000+0.7, 10*200)
    print("rauschzahl_einfach(500 ohm) = ", F)
    print("rauschzahl_korr(500 ohm) = ", F_korr, " mit delta_nu = ", 0.14*5000+0.7)

    # werteZuTabelle(kreisfrequenz, spannung,
    #               rundungen=[3, 1])
