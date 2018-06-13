import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)


def plotSpektrum(nu_M, spannung, V_N, delta_nu, dateiname):

    # plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
    # xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='kx', label='Messwerte')
    spannung /= V_N**2
    x = nu_M
    y = spannung/delta_nu
    plt.errorbar(noms(x), noms(y),
                 xerr=stds(x), yerr=stds(y), fmt='kx', label='Messwerte')
    plt.xlabel(r'$\nu_\text{M}\:/\: \si{\kilo\hertz}$')
    plt.ylabel(r'$W \:/\: a.u.$')
    plt.legend(loc='best')
    plt.yscale('log')
    # plt.ylim(10**(-9), 10**(-6))
    plt.xscale('log')

    # in matplotlibrc leider (noch) nicht möglich
    plt.tight_layout(pad=0.5, h_pad=1.2, w_pad=1.08)
    plt.savefig('build/plotRauschspektrum'+dateiname+'.pdf')
    plt.close()


def commuteDeltaNu(nu_M, kathodenart):
    delta_nu = unp.uarray(np.ones(len(nu_M)), np.ones(len(nu_M)))

    for i, elem in enumerate(nu_M):
        if elem.n >= 0.01 and elem.n < 0.1:
            delta_nu[i] = 0.15*elem - 0.003 + 0.0000001
        elif elem.n >= 0.1 and elem.n < 10:
            delta_nu[i] = 0.140*elem + 0.007
        elif elem.n >= 10 and elem.n < 50:
            delta_nu[i] = 0.135*elem + 0.05
        elif elem.n >= 50 and elem.n <= 100 and kathodenart == "oxyd":  # R=2200ohm
            delta_nu[i] = 0.115*elem + 1.05
        elif elem.n >= 50 and elem.n <= 100 and kathodenart == "rein":  # R=4680ohm
            delta_nu[i] = 0.109*elem + 1.2

    return delta_nu


if __name__ == '__main__':
    # oxyd:
    nu_MBand, delta_nuBand, sigma_delta_nuBand, spannungBand, V_NBand = np.genfromtxt('daten/oxidkurveband.txt',
                                                                                      unpack='True')

    nu_MBand = unp.uarray(nu_MBand, 5)
    delta_nuBand = unp.uarray(delta_nuBand, sigma_delta_nuBand)
    spannungBand = unp.uarray(spannungBand, 0.05)
    nu_Msel, spannungsel, V_Nsel = np.genfromtxt('daten/oxidkurvesel.txt',
                                                 unpack='True')
    nu_Msel = unp.uarray(nu_Msel, 0.1*nu_Msel)
    spannungsel = unp.uarray(spannungsel, 0.005)
    delta_nusel = commuteDeltaNu(nu_Msel, "oxyd")
    plotSpektrum(np.append(nu_MBand, nu_Msel), np.append(spannungBand, spannungsel), np.append(V_NBand, V_Nsel), np.append(delta_nuBand*10**3, delta_nusel*10**3), "Oxid")

    # rein:
    nu_MBand2, delta_nuBand2, sigma_delta_nuBand2, spannungBand2, V_NBand2 = np.genfromtxt('daten/reinkurveband.txt', unpack='True')
    nu_MBand2 = unp.uarray(nu_MBand2, 5)
    delta_nuBand2 = unp.uarray(delta_nuBand2, sigma_delta_nuBand2)
    spannungBand2 = unp.uarray(spannungBand2, 0.05)
    nu_Msel2, spannungsel2, V_Nsel2 = np.genfromtxt('daten/reinkurvesel.txt',
                                                    unpack='True')
    nu_Msel2 = unp.uarray(nu_Msel2, 0.1*nu_Msel2)
    spannungsel2 = unp.uarray(spannungsel2, 0.005)
    delta_nusel2 = commuteDeltaNu(nu_Msel2, "rein")
    print('delta_nusel=', delta_nusel2)
    plotSpektrum(np.append(nu_MBand2, nu_Msel2), np.append(spannungBand2, spannungsel2), np.append(V_NBand2, V_Nsel2), np.append(delta_nuBand2*10**3, delta_nusel2*10**3), "Rein")

    # werteZuTabelle(kreisfrequenz, spannung,
    #                rundungen=[3, 1])
