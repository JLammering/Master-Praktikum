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


def plot(axes, x, y, V_strich_theorie, label, filename, x_label, y_label, grenze, ylim=None, logy=None, uebergang=None, letzter_wert_kacke=False):
    #label = 'test'
    flanke_grenze = grenze
    flanke_grenze_oben = None
    if letzter_wert_kacke:
        flanke_grenze_oben = -1
        axes.errorbar(noms(x[-1:]), noms(y[-1:]),
                     xerr=stds(x[-1:]), yerr=stds(y[-1:]),
                     fmt='kx', label='Unberücksichtigt bei {}'.format(label))
    if uebergang is not None:
        flanke_grenze = grenze + 1
        axes.errorbar(noms(x[uebergang:uebergang+1]), noms(y[uebergang:uebergang+1]),
                     xerr=stds(x[uebergang:uebergang+1]), yerr=stds(y[uebergang:uebergang+1]),
                     fmt='gx', label='Messwerte Übergang bei {}'.format(label))

    axes.errorbar(noms(x[flanke_grenze:flanke_grenze_oben]), noms(y[flanke_grenze:flanke_grenze_oben]),
                 xerr=stds(x[flanke_grenze:flanke_grenze_oben]), yerr=stds(y[flanke_grenze:flanke_grenze_oben]),
                 fmt='rx', label='Messwerte Flanke bei {}'.format(label))
    axes.errorbar(noms(x[:grenze]), noms(y[:grenze]),
                 xerr=stds(x[:grenze]), yerr=stds(y[:grenze]),
                 fmt='bx', label='Messwerte Plateau bei {}'.format(label))
    plateau_mittel = ufloat(np.mean(np.exp(noms(y[:grenze]))), np.std(np.exp(noms(y[:grenze]))))
    plateau_mittel_halb = unp.log(plateau_mittel / unp.sqrt(2)) if plateau_mittel.n >= 1 else unp.log(plateau_mittel * unp.sqrt(2))
    label_v_halb = r"$V_\text{Plateau}' / \sqrt{2}$" if plateau_mittel.n >= 1 else r"$V_\text{Plateau}' \cdot \sqrt{2}$"
    #label_v_halb = 'test'
    axes.plot((min(noms(x)), max(noms(x))), (noms(plateau_mittel_halb), noms(plateau_mittel_halb)), '-', label=label_v_halb)
    grenzfrequenz = fitten(axes, x[flanke_grenze:flanke_grenze_oben], y[flanke_grenze:flanke_grenze_oben], linear, [-1, 5], ['m', 'b'], 'r', 'Flanke', schnittwert=plateau_mittel_halb)
    print('grenzfrequenz = ', grenzfrequenz)
    # fitten(x[:grenze], y[:grenze], linear, [0, 0], ['m', 'b'], 'g', 'Plateau')

    print('Mittelwert Plateau = ', plateau_mittel, 'Abweichung von ', abweichungen(V_strich_theorie, plateau_mittel))


    # plotting
    axes.legend(loc='best')
    axes.set_xlim(min(noms(x)) - max(noms(x)) * 0.06, (max(noms(x))) * 1.06)
    if ylim is not None:
        axes.set_ylim(ylim[0], ylim[1])
    #x_label, y_label = 'test', 'test'
    axes.set_xlabel(x_label)
    axes.set_ylabel(y_label)
    plt.close()

    return grenzfrequenz, plateau_mittel


def plotphase(nu_1, phi_1, nu_2, phi_2, nu_3, phi_3, nu_4, phi_4):
    # nu_1, nu_2, nu_3, nu_4 = unp.log(nu_1), unp.log(nu_2), unp.log(nu_3), unp.log(nu_4)
    # phi_1, phi_2, phi_3, phi_4 = unp.abs(phi_1), unp.abs(phi_2), unp.abs(phi_3), unp.abs(phi_4)
    plt.errorbar(noms(nu_1), np.abs(noms(phi_1)),
                  xerr=stds(nu_1), yerr=stds(phi_1), label='Messwerte bei 1. Widerstandskombination')
    plt.errorbar(noms(nu_2), np.abs(noms(phi_2)),
                  xerr=stds(nu_2), yerr=stds(phi_2), label='Messwerte bei 2. Widerstandskombination')
    plt.errorbar(noms(nu_3), np.abs(noms(phi_3)),
                  xerr=stds(nu_3), yerr=stds(phi_3), label='Messwerte bei 3. Widerstandskombination')
    plt.errorbar(noms(nu_4), np.abs(noms(phi_4)),
                  xerr=stds(nu_4), yerr=stds(phi_4), label='Messwerte bei 4. Widerstandskombination')

    xlabel = r'$\nu\:/\:\si{\kilo\hertz}$'
    ylabel = r'$\phi\:/\:\si{\degree}$'
    #xlabel = 'test'
    #ylabel = 'test'
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xscale('log')
    plt.legend(loc='best')

    plt.savefig('build/phasen.pdf')



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
    grenzfrequenz_1, plateau_mittel_1 = plot(axs[0][0], unp.log(nu_1), unp.log(V_strich_1), V_strich_theorie_1, '1. Widerstandskombination', 'gegen_1', r'$\ln(\nu\:/\:\si{\kilo\hertz})$', r"$\ln(V')$", 4, (-2, 0.25), uebergang=4)
    verst_bandbreite.append(grenzfrequenz_1 * plateau_mittel_1)
    V_1 = 1 / ((1 / plateau_mittel_1) - (R_1_1/R_N_1))
    print('V_1= ', V_1)

    # 2. Kombi
    nu_2, U_A_2, U_1_2, phi_2 = np.genfromtxt('daten/gegen_2.txt',
                                              unpack='True')
    sort_inds_2 = nu_2.argsort()
    nu_2 = unp.uarray(nu_2, nu_2 * 0.1)[sort_inds_2]
    U_A_2 = unp.uarray(U_A_2, 10)[sort_inds_2]
    U_1_2 = unp.uarray(U_1_2, 10)[sort_inds_2]
    V_strich_2 = U_A_2 / U_1_2
    werteZuTabelle(noms(nu_2), noms(U_1_2).astype(int), noms(U_A_2).astype(int), noms(V_strich_2), noms(phi_2).astype(int), rundungen=[1, 0, 0, 2, 0])
    R_N_2, R_1_2 = ufloat(1.002e3, 0.05e3), ufloat(9.96e3, 0.05e3)
    V_strich_theorie_2 = R_N_2 / R_1_2
    phi_2 = unp.uarray(phi_2, 5)[sort_inds_2]
    grenzfrequenz_2, plateau_mittel_2 = plot(axs[0][1], unp.log(nu_2), unp.log(V_strich_2), V_strich_theorie_2, '2. Widerstandskombination', 'gegen_2', r'$\ln(\nu\:/\:\si{\kilo\hertz})$', r"$\ln(V')$", 3, (-2.5, -1.5), letzter_wert_kacke=True)
    verst_bandbreite.append(grenzfrequenz_2 * plateau_mittel_2)
    V_2 = 1 / ((1 / plateau_mittel_2) - (R_1_2/R_N_2))
    print('V_2= ', V_2)

    # 3. Kombi
    nu_3, U_A_3, U_1_3, phi_3 = np.genfromtxt('daten/gegen_3.txt',
                                              unpack='True')
    sort_inds_3 = nu_3.argsort()
    nu_3 = unp.uarray(nu_3, nu_3 * 0.1)[sort_inds_3]
    U_A_3 = unp.uarray(U_A_3, 0.01)[sort_inds_3] * 1e3
    U_1_3 = unp.uarray(U_1_3, 10)[sort_inds_3]
    V_strich_3 = U_A_3 / U_1_3
    werteZuTabelle(noms(nu_3), noms(U_1_3).astype(int), noms(U_A_3).astype(int), noms(V_strich_3), noms(phi_3).astype(int), rundungen=[1, 0, 0, 1, 0])
    R_N_3, R_1_3 = ufloat(1.002e3, 0.05e3), ufloat(470, 5)
    V_strich_theorie_3 = R_N_3 / R_1_3
    phi_3 = unp.uarray(phi_3, 5)[sort_inds_3]
    grenzfrequenz_3, plateau_mittel_3 = plot(axs[1][0], unp.log(nu_3), unp.log(V_strich_3), V_strich_theorie_3, '3. Widerstandskombination', 'gegen_3', r'$\ln(\nu\:/\:\si{\kilo\hertz})$', r"$\ln(V')$", 6, (-1.5, 1), uebergang=6, letzter_wert_kacke=True)
    verst_bandbreite.append(grenzfrequenz_3 * plateau_mittel_3)
    V_3 = 1 / ((1 / plateau_mittel_3) - (R_1_3/R_N_3))
    print('V_3= ', V_3)

    # 4. Kombi
    nu_4, U_A_4, U_1_4, phi_4 = np.genfromtxt('daten/gegen_4.txt',
                                              unpack='True')
    sort_inds_4 = nu_4.argsort()
    nu_4 = unp.uarray(nu_4, nu_4 * 0.1)[sort_inds_4]
    U_A_4 = unp.uarray(U_A_4, 0.01)[sort_inds_4] * 1e3
    U_1_4 = unp.uarray(U_1_4, 10)[sort_inds_4]
    V_strich_4 = U_A_4 / U_1_4
    werteZuTabelle(noms(nu_4), noms(U_1_4).astype(int), noms(U_A_4).astype(int), noms(V_strich_4), noms(phi_4).astype(int), rundungen=[1, 0, 0, 1, 0])
    R_N_4, R_1_4 = ufloat(9.96e3, 0.05e3), ufloat(1.002e3, 0.05e3)
    V_strich_theorie_4 = R_N_4 / R_1_4
    phi_4 = unp.uarray(phi_4, 5)[sort_inds_4]
    grenzfrequenz_4, plateau_mittel_4 = plot(axs[1][1], unp.log(nu_4), unp.log(V_strich_4), V_strich_theorie_4, '4. Widerstandskombination', 'gegen_4', r'$\ln(\nu\:/\:\si{\kilo\hertz})$', r"$\ln(V')$", 4, (-3, 3))
    verst_bandbreite.append(grenzfrequenz_4 * plateau_mittel_4)
    V_4 = 1 / ((1 / plateau_mittel_4) - (R_1_4/R_N_4))
    print('V_4= ', V_4)

    print(verst_bandbreite)
    sum = []
    for i, verst in enumerate(noms(verst_bandbreite)):
        if i == 1:
            continue
        sum.append(verst)
    print('verst_bandbreite_const = ', np.mean(sum), np.std(sum), sum)

    print('V_ges = ', np.mean([V_1.n, V_3.n, V_4.n]), np.std([V_1.n, V_3.n, V_4.n]))

    plotphase(nu_1, phi_1, nu_2, phi_2, nu_3, phi_3, nu_4, phi_4)


    fig.savefig('build/gegen.pdf')
    plt.close()
