import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
from scipy.optimize import curve_fit
from functions import abweichungen, werteZuTabelle


def linear(x, m, b):
    return m * x + b


def fitten(axes, x, y, fitfunktion, p_list, pname_list, color, label, schnittwert=None):
    params, covariance = curve_fit(fitfunktion, noms(x),
                                   noms(y),
                                   p0=p_list)
    errors = np.sqrt(np.diag(covariance))
    print('Werte ' + label)
    for i, name in enumerate(pname_list):
        print('{0} = {1} ± {2}'.format(name, round(params[i], 5), round(errors[i], 5)))
    x_fit = np.linspace(noms(x[0]) - (noms(x[-1])) * 1, (noms(x[-1])) * 1.1, 10000)
    axes.plot(x_fit, fitfunktion(x_fit, *params), color, label='Fit ' + label)

    if schnittwert is not None:
        for x_loop in x_fit:
            if fitfunktion(x_loop, *params) < noms(schnittwert) and params[0] < 0:
                return unp.exp(x_loop)
                break
            elif fitfunktion(x_loop, *params) > noms(schnittwert) and params[0] > 0:
                return unp.exp(x_loop)
                break


def plot(axes, x, y, V_strich_theorie, label, filename, x_label, y_label, grenze, ylim=None, logy=None):
    axes.errorbar(noms(x[grenze:]), noms(y[grenze:]),
                 xerr=stds(x[grenze:]), yerr=stds(y[grenze:]),
                 fmt='rx', label=f'Messwerte Flanke bei {label}')
    axes.errorbar(noms(x[:grenze]), noms(y[:grenze]),
                 xerr=stds(x[:grenze]), yerr=stds(y[:grenze]),
                 fmt='bx', label=f'Messwerte Plateau bei {label}')
    print(V_strich_theorie.n)
    V_strich_theorie_halb = unp.log(V_strich_theorie / unp.sqrt(2)) if V_strich_theorie.n >= 1 else unp.log(V_strich_theorie * unp.sqrt(2))
    label_v_halb = r"$V_\text{theorie}' / \sqrt{2}$" if V_strich_theorie.n >= 1 else r"$V_\text{theorie}' \cdot \sqrt{2}$"
    # label_v_halb = 'hallo'
    axes.plot((min(noms(x)), max(noms(x))), (noms(V_strich_theorie_halb), noms(V_strich_theorie_halb)), '-', label=label_v_halb)
    grenzfrequenz = fitten(axes, x[grenze:], y[grenze:], linear, [-1, 5], ['m', 'b'], 'r', 'Flanke', schnittwert=V_strich_theorie_halb)
    print('grenzfrequenz = ', grenzfrequenz)
    # fitten(x[:grenze], y[:grenze], linear, [0, 0], ['m', 'b'], 'g', 'Plateau')
    plateau_mittel = ufloat(np.mean(noms(y[:grenze])), np.std(noms(y[:grenze])))
    print('Mittelwert Plateau = ', plateau_mittel, 'Abweichung von ', abweichungen(V_strich_theorie, unp.exp(plateau_mittel)))


    # plotting
    axes.legend(loc='best')
    axes.set_xlim(min(noms(x)) - max(noms(x)) * 0.06, (max(noms(x))) * 1.06)
    if ylim is not None:
        axes.set_ylim(ylim[0], ylim[1])
    # x_label, y_label = 'test', 'test'
    axes.set_xlabel(x_label)
    axes.set_ylabel(y_label)

    return grenzfrequenz


if __name__ == '__main__':
    verst_bandbreite = []
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    print(axs)

    # 1. Kombi
    nu_1, U_A_1, U_1_1, phi_1 = np.genfromtxt('daten/gegen_1.txt',
                                              unpack='True')
    sort_inds_1 = nu_1.argsort()
    nu_1 = unp.uarray(nu_1, nu_1 * 0.1)[sort_inds_1]
    U_A_1 = unp.uarray(U_A_1, 10)[sort_inds_1]
    U_1_1 = unp.uarray(U_1_1, 10)[sort_inds_1]
    V_strich_1 = U_A_1 / U_1_1
    werteZuTabelle(noms(nu_1), noms(U_1_1).astype(int), noms(U_A_1).astype(int), noms(V_strich_1), noms(phi_1).astype(int), rundungen=[1, 0, 0, 1, 0])
    R_N_1, R_1_1 = ufloat(9.96e3, 0.05e3), ufloat(9.96e3, 0.05e3)
    V_strich_theorie_1 = R_N_1 / R_1_1
    phi_1 = unp.uarray(phi_1, 5)[sort_inds_1]
    grenzfrequenz_1 = plot(axs[0][0], unp.log(nu_1), unp.log(V_strich_1), V_strich_theorie_1, '1. Widerstandskombination', 'gegen_1', r'$\ln(\nu\:/\:\si{\kilo\hertz})$', r"$\ln(V')$", 4, (-2, 0.25))
    verst_bandbreite.append(grenzfrequenz_1 * V_strich_theorie_1)

    # 2. Kombi
    nu_2, U_A_2, U_1_2, phi_2 = np.genfromtxt('daten/gegen_2.txt',
                                              unpack='True')
    sort_inds_2 = nu_2.argsort()
    nu_2 = unp.uarray(nu_2, nu_2 * 0.1)[sort_inds_2]
    U_A_2 = unp.uarray(U_A_2, 10)[sort_inds_2]
    U_1_2 = unp.uarray(U_1_2, 10)[sort_inds_2]
    V_strich_2 = U_A_2 / U_1_2
    R_N_2, R_1_2 = ufloat(1.002e3, 0.05e3), ufloat(9.96e3, 0.05e3)
    V_strich_theorie_2 = R_N_2 / R_1_2
    phi_2 = unp.uarray(phi_2, 5)[sort_inds_2]
    grenzfrequenz_2 = plot(axs[0][1], unp.log(nu_2), unp.log(V_strich_2), V_strich_theorie_2, '2. Widerstandskombination', 'gegen_2', r'$\ln(\nu\:/\:\si{\kilo\hertz})$', r"$\ln(V')$", 3, (-2.5, -1.5))
    verst_bandbreite.append(grenzfrequenz_2 * V_strich_theorie_2)

    # 3. Kombi
    nu_3, U_A_3, U_1_3, phi_3 = np.genfromtxt('daten/gegen_3.txt',
                                              unpack='True')
    sort_inds_3 = nu_3.argsort()
    nu_3 = unp.uarray(nu_3, nu_3 * 0.1)[sort_inds_3]
    U_A_3 = unp.uarray(U_A_3, 0.01)[sort_inds_3] * 1e3
    U_1_3 = unp.uarray(U_1_3, 10)[sort_inds_3]
    V_strich_3 = U_A_3 / U_1_3
    R_N_3, R_1_3 = ufloat(1.002e3, 0.05e3), ufloat(470, 5)
    V_strich_theorie_3 = R_N_3 / R_1_3
    phi_3 = unp.uarray(phi_3, 5)[sort_inds_3]
    grenzfrequenz_3 = plot(axs[1][0], unp.log(nu_3), unp.log(V_strich_3), V_strich_theorie_3, '3. Widerstandskombination', 'gegen_3', r'$\ln(\nu\:/\:\si{\kilo\hertz})$', r"$\ln(V')$", 6, (-1.5, 1))
    verst_bandbreite.append(grenzfrequenz_3 * V_strich_theorie_3)

    # 4. Kombi
    nu_4, U_A_4, U_1_4, phi_4 = np.genfromtxt('daten/gegen_4.txt',
                                              unpack='True')
    sort_inds_4 = nu_4.argsort()
    nu_4 = unp.uarray(nu_4, nu_4 * 0.1)[sort_inds_4]
    U_A_4 = unp.uarray(U_A_4, 0.01)[sort_inds_4] * 1e3
    U_1_4 = unp.uarray(U_1_4, 10)[sort_inds_4]
    V_strich_4 = U_A_4 / U_1_4
    R_N_4, R_1_4 = ufloat(9.96e3, 0.05e3), ufloat(1.002e3, 0.05e3)
    V_strich_theorie_4 = R_N_4 / R_1_4
    phi_4 = unp.uarray(phi_4, 5)[sort_inds_4]
    grenzfrequenz_4 = plot(axs[1][1], unp.log(nu_4), unp.log(V_strich_4), V_strich_theorie_4, '4. Widerstandskombination', 'gegen_4', r'$\ln(\nu\:/\:\si{\kilo\hertz})$', r"$\ln(V')$", 4, (-3, 3))
    verst_bandbreite.append(grenzfrequenz_4 * V_strich_theorie_4)

    print(verst_bandbreite)

    fig.savefig('build/gegen.pdf')
    plt.close()
