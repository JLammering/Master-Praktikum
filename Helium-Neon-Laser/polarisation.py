import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy import constants
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)


def fitfunktion_pol(phi, I_0, phi_verschieb, m):
    return I_0*(np.cos(m*phi + phi_verschieb)**2)


def fitfunktion_grundmode(x, I_0, r_verschieb, omega):
    return I_0*np.exp((-2*(x+r_verschieb)**2)/(omega**2))


# def fitfunktion_transmode(x, I_01, r_verschieb1, omega1,
#                           I_02, r_verschieb2, omega2):
#     return (I_01*np.exp((-2*(x+r_verschieb1)**2)/(omega1**2)) +
#             I_02*np.exp((-2*(x+r_verschieb2)**2)/(omega2**2)))
def fitfunktion_transmode(x, I_0, x_0, omega):
    return I_0*(x-x_0)**2*np.exp(-2*(x-x_0)**2/(omega**2))


def plot(x, y, label, filename, x_label, y_label,
         fitfunktion, p_list, pname_list):
    plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
                 xerr=unp.std_devs(x), yerr=unp.std_devs(y),
                 fmt='kx', label='Messwerte '+label)

    werte_start = 0
    werte_ende = len(x)-1
    params, covariance = curve_fit(fitfunktion, unp.nominal_values(x[werte_start:werte_ende]),
                                   unp.nominal_values(y[werte_start:werte_ende]),
                                   p0=p_list)
    errors = np.sqrt(np.diag(covariance))
    for i, name in enumerate(pname_list):
        print('{0} = {1} ± {2}'.format(name, round(params[i], 5), round(errors[i], 5)))
    # print('I_0= ', params[0], '±', errors[0])
    # print('phi_verschieb= ', params[1], '±', errors[1])
    # print('m = ', params[2], '±', errors[2])
    # m = ufloat(params[0], errors[0])
    x_fit = np.linspace(noms(x[0])-(noms(x[-1]))*0.1, (noms(x[-1]))*1.1, 1000)
    plt.plot(x_fit, fitfunktion(x_fit, *params), label='Fit ' + label)

    # plotting
    plt.legend(loc='best')
    plt.xlim(noms(x[0])-(noms(x[-1]))*0.06, (noms(x[-1]))*1.06)

    # y_label, x_label= 'test', 'x_label'
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig('build/{}.pdf'.format(filename))
    plt.close()


def wellenlaenge(d_array, mitte, L):
    d_links = unp.uarray(np.zeros(mitte), np.zeros(mitte))
    d_rechts = unp.uarray(np.zeros(12-mitte), np.zeros(12-mitte))
    for i in range(0, mitte, 1):
        d_links[i] = np.sum(d_array[mitte-(i+1):mitte])
    for i in range(0, 12-mitte, 1):
        d_rechts[i] = np.sum(d_array[mitte:mitte+(i+1)])
    g = (10**-3)/80
    print('g = ', g*10**6, 'micro meter')
    d_links = d_links*10**-2
    d_rechts = d_rechts*10**-2
    d_all = np.concatenate((noms(d_links), noms(d_rechts)))
    n_links = np.linspace(1, 6, 6)
    lamda_links = g * unp.sin(unp.arctan(d_links/L))/n_links
    n_rechts = range(1, len(d_rechts)+1, 1)
    n_all = np.concatenate((n_links, n_rechts))
    lamda_rechts = g * unp.sin(unp.arctan(d_rechts/L))/n_rechts
    lamda_all = np.concatenate((lamda_links, lamda_rechts))
    werteZuTabelle(d_all*100, n_all.astype(int), (noms(lamda_all)*10**9).astype(int), (stds(lamda_all)*10**9).astype(int), rundungen=[3, 0, 0, 0])
    print('lambda = ', (np.sum(lamda_all))/12)
    print('Abweichung = ', abweichungen(632.8*10**-9, (np.sum(lamda_all))/12))
    print('Mittelwert = ', np.mean(noms(lamda_all)), '±', np.std(noms(lamda_all)))


def longitudinaleModen(f_array, L_vergleich):
    c = ufloat(constants.physical_constants["speed of light in vacuum"][0], 0)
    differenz = unp.uarray(np.zeros(4), np.zeros(4))
    for i in range(len(f_array)):
        if i == 0:
            differenz[i] = f_array[i]
        else:
            differenz[i] = f_array[i] - f_array[i-1]
    print(differenz)
    differenz *= 10**6
    L = c/((np.sum(differenz)/4)*2)
    print('L = ', L)
    print('Abweichung = ', abweichungen(L_vergleich, L))


if __name__ == '__main__':
    # polarisation
    I = np.genfromtxt('daten/polarisation.txt',
                      unpack='True')
    phi = np.linspace(0, 180, 19)
    phi = unp.uarray(phi, 1)
    phi_rad = (phi/360)*2*np.pi
    I = unp.uarray(I, 0.005)
    werteZuTabelle(noms(phi).astype(int), noms(I), rundungen=[0, 2])
    plot(phi_rad, I, "Polarisation", "polarisation", r'$\phi/\si{\radian}$', r'$I/\si{\micro\ampere}$', fitfunktion_pol,
         [0.8, 2, 0], ["I_0", "phi_verschieb", "m"])



    # moden
    x, I = np.genfromtxt('daten/tem00.txt',
                         unpack='True')
    x = unp.uarray(x, 0.5)
    I = unp.uarray(I, 0.01)
    werteZuTabelle(noms(x).astype(int), noms(I), rundungen=[0, 3])
    plot(x, I, r'TEM$_{00}$', 'grundmode', r'$x/\si{\milli\meter}$',
         r'$I/\si{\micro\ampere}$', fitfunktion_grundmode, [2.97, 13, 50],
         ["I_0", "x_0", "omega"])

    x, I = np.genfromtxt('daten/tem01.txt',
                         unpack='True')
    x = unp.uarray(x, 0.5)
    I = unp.uarray(I, 0.01)
    werteZuTabelle(noms(x).astype(int), noms(I), rundungen=[0, 3])
    plot(x, I, r'TEM$_{01}$', 'transmode', r'$x/\si{\milli\meter}$',
         r'$I/\si{\micro\ampere}$', fitfunktion_transmode,
         [0.12, 20, 1],
         ["I_0_trans", "x_0", "omega"])

    # wellenlänge
    nummer, d = np.genfromtxt('daten/wellenlaenge.txt',
                              unpack='True')
    d = unp.uarray(d, 0.2)
    L = ufloat(0.798, 0.005)
    wellenlaenge(d, 6, L)

    # longi Moden
    f = np.genfromtxt('daten/longiModen.txt',
                      unpack='True')
    f = unp.uarray(f, 5)
    longitudinaleModen(f[0:4], ufloat(0.535, 0.005))
    longitudinaleModen(f[4:8], ufloat(0.605, 0.005))
    longitudinaleModen(f[8:12], ufloat(0.756, 0.005))
    werteZuTabelle(noms(f).astype(int), rundungen=[0] )

    c = constants.physical_constants["speed of light in vacuum"][0]
    v_neon = 601.957 #m/s
    v_neon /= np.sqrt(3)
    f_neon = c/632.816e-9
    f_beobacht = f_neon * c/(c-v_neon)
    delta_f = 2* (f_beobacht-f_neon)/1e6
    print('f_neon = ', f_neon/1e12, 'freq beobachtet = ', f_beobacht/1e12, 'delta f = ', delta_f)
