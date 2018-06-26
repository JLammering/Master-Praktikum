import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
from uncertainties import ufloat
from scipy import constants


def funkelFunk(nu, const, alpha):
    return (const/(nu**alpha))


def plotSpektrum(nu_M, strom, V_N, delta_nu, dateiname):

    strom /= (V_N**2 * 1000**2 * 10)
    x = nu_M
    y = strom/delta_nu
    if dateiname == 'Oxid':
        how_many = 10
        x_funkel = x[len(x)-how_many:len(x)]
        x_schrot = x[0:len(x)-how_many]
        y_funkel = y[len(x)-how_many:len(x)]
        y_schrot = y[0:len(x)-how_many]
        print('nu_funkel <= ', x_funkel[0])
        plt.errorbar(noms(x_schrot), noms(y_schrot),
                     xerr=stds(x_schrot), yerr=stds(y_schrot), fmt='kx', label='Messwerte Schrotrauschen')
        plt.errorbar(noms(x_funkel), noms(y_funkel),
                     xerr=stds(x_funkel), yerr=stds(y_funkel), fmt='rx', label='Messwerte Schrotrauschen+Funkeleffekt')
        # fitten:
        params, covariance = curve_fit(funkelFunk, unp.nominal_values(x_funkel),
                                       unp.nominal_values(y_funkel),
                                       p0=[10**(-22), 1], sigma=stds(y_funkel))
        errors = np.sqrt(np.diag(covariance))
        print('const= ', params[0], '±', errors[0], ' alpha= ', params[1], '±',
              errors[1])
        alpha = ufloat(params[1], errors[1])
        print('Abweichung von alpha= ', abweichungen(1, alpha), '%')
        x_fit = np.linspace(0.02, 100)
        plt.plot(x_fit, funkelFunk(x_fit, *params), label='Fit')
        plt.xlim(0.03, 500)
        plt.ylim(10**(-22), 10**(-19))
    else:
        plt.errorbar(noms(x), noms(y),
                     xerr=stds(x), yerr=stds(y), fmt='kx', label='Messwerte')
    e0theorie = ufloat(constants.physical_constants["elementary charge"][0],
                       constants.physical_constants["elementary charge"][2])
    # xv = [0.02, 10**3]
    # yv = [2*e0theorie.n*0.9*10**(-3), 2*e0theorie.n*0.9*10**(-3)]
    # plt.plot(xv, yv, 'b-', label='Schrotrauschen Theorie')
    plt.xlabel(r'$\nu_\text{M}\:/\: \si{\kilo\hertz}$')
    plt.ylabel(r'$W \:/\: \si{\ampere\per\hertz}$')
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
    R_oxid = 2200
    nu_MBand = unp.uarray(nu_MBand, 5)
    delta_nuBand = unp.uarray(delta_nuBand, sigma_delta_nuBand)
    spannungBand = unp.uarray(spannungBand, 0.05)
    stromband = spannungBand/(R_oxid**2)
    nu_Msel, spannungsel, V_Nsel = np.genfromtxt('daten/oxidkurvesel.txt',
                                                 unpack='True')
    nu_Msel = unp.uarray(nu_Msel, 0.1*nu_Msel)
    spannungsel = unp.uarray(spannungsel, 0.005)
    stromsel = spannungsel/(R_oxid**2)
    delta_nusel = commuteDeltaNu(nu_Msel, "oxyd")
    werteZuTabelle(noms(np.append(nu_MBand, nu_Msel)), stds(np.append(nu_MBand, nu_Msel)), noms(np.append(delta_nuBand, delta_nusel)), stds(np.append(delta_nuBand, delta_nusel)), noms(np.append(spannungBand, spannungsel)), stds(np.append(spannungBand, spannungsel)), np.append(V_NBand, V_Nsel).astype('int'), rundungen=[2, 4, 3, 4, 3, 3, 0])
    plotSpektrum(np.append(nu_MBand, nu_Msel), np.append(stromband, stromsel), np.append(V_NBand, V_Nsel), np.append(delta_nuBand*10**3, delta_nusel*10**3), "Oxid")

    # rein:
    nu_MBand2, delta_nuBand2, sigma_delta_nuBand2, spannungBand2, V_NBand2 = np.genfromtxt('daten/reinkurveband.txt', unpack='True')
    R_rein = 4680
    nu_MBand2 = unp.uarray(nu_MBand2, 5)
    delta_nuBand2 = unp.uarray(delta_nuBand2, sigma_delta_nuBand2)
    spannungBand2 = unp.uarray(spannungBand2, 0.05)
    stromband2 = spannungBand2/(R_rein**2)
    nu_Msel2, spannungsel2, V_Nsel2 = np.genfromtxt('daten/reinkurvesel.txt',
                                                    unpack='True')
    nu_Msel2 = unp.uarray(nu_Msel2, 0.1*nu_Msel2)
    spannungsel2 = unp.uarray(spannungsel2, 0.005)
    stromsel2 = spannungsel2/(R_rein**2)
    delta_nusel2 = commuteDeltaNu(nu_Msel2, "rein")
    werteZuTabelle(noms(np.append(nu_MBand2, nu_Msel2)), stds(np.append(nu_MBand2, nu_Msel2)), noms(np.append(delta_nuBand2, delta_nusel2)), stds(np.append(delta_nuBand2, delta_nusel2)), noms(np.append(spannungBand2, spannungsel2)), stds(np.append(spannungBand2, spannungsel2)), np.append(V_NBand2, V_Nsel2).astype('int'), rundungen=[2, 4, 3, 4, 3, 3, 0])
    plotSpektrum(np.append(nu_MBand2, nu_Msel2), np.append(stromband2, stromsel2), np.append(V_NBand2, V_Nsel2), np.append(delta_nuBand2*10**3, delta_nusel2*10**3), "Rein")

    # werteZuTabelle(kreisfrequenz, spannung,
    #                rundungen=[3, 1])
