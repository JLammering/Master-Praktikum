import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp


def fitfunktion(U, m, yabschnitt):
    return m*U+yabschnitt


def plotWiderstand(widerstand, spannung, V_N, dateiname):

    # plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
    # xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='kx', label='Messwerte')
    # amplitude = 0.2
    # spannung *= 10**(-3)  # in Volt
    # spannung /= amplitude**2  # auf amplitude normieren
    y = spannung / V_N**2
    if dateiname == "2" or dateiname == "2Korr":
        x = widerstand*10**3
    else:
        x = widerstand
    plt.plot(x, y, 'kx', label='Messwerte')
    #plt.xlabel(r'$R/\si{\ohm}$')



    # fitten:
    params, covariance = curve_fit(fitfunktion, unp.nominal_values(x),
                                   unp.nominal_values(y),
                                   p0=[0.1, 1])
    errors = np.sqrt(np.diag(covariance))
    print('m= ', params[0], '±', errors[0], ' yabschnitt= ', params[1], '±',
          errors[1])
    x_fit = np.linspace(0, max(x))
    plt.plot(x_fit, fitfunktion(x_fit, *params), label='Fit')

    # kBoltzmann
    if dateiname == "1" or dateiname == "2":
        int = np.genfromtxt('build/eichungeinfach.txt', unpack='True')
    else:
        int = np.genfromtxt('build/eichungKorrelator.txt', unpack='True')

    T = 293.15  # K
    k_B = params[0]/(4*int*T)
    print('k_B= ', k_B)

    #plt.ylabel(r'$U_\text{A} \:/\: a.u.$')
    plt.legend(loc='best')

    # in matplotlibrc leider (noch) nicht möglich
    plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
    plt.savefig('build/plotWiderstand'+dateiname+'.pdf')
    plt.close()


if __name__ == '__main__':
    widerstand, spannung, V_N = np.genfromtxt('daten/widerstand1.txt', unpack='True')
    plotWiderstand(widerstand, spannung * 10**(-3), V_N, "1")

    widerstand2, spannung2, V_N2 = np.genfromtxt('daten/widerstand2.txt', unpack='True')
    plotWiderstand(widerstand2, spannung2 * 10**(-3), V_N2, "2")

    widerstand1Korr, spannung1Korr, V_N1Korr = np.genfromtxt('daten/widerstand1Korr.txt', unpack='True')
    plotWiderstand(widerstand1Korr, spannung1Korr, V_N1Korr, "1Korr")

    widerstand2Korr, spannung2Korr, V_N2Korr = np.genfromtxt('daten/widerstand2Korr.txt', unpack='True')
    plotWiderstand(widerstand2Korr, spannung2Korr, V_N2Korr, "2Korr")
    # werteZuTabelle(kreisfrequenz, spannung,
    #               rundungen=[3, 1])
