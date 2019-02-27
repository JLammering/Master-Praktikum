import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy import constants
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)


def fitfunktion_daempf(t, tau, U_0):
    return U_0 * np.exp(-t / tau)


def plot(x, y, file, fitfunktion, tau_erw, abklingzeit_erw, x_fit=None, xlim=None, ylim=None):
    plt.errorbar(unp.nominal_values(x), unp.nominal_values(y),
                 xerr=unp.std_devs(x), yerr=unp.std_devs(y), fmt='-', label='Messwerte')

    # maxima finden
    x_nom = noms(x)
    y_nom = noms(y)
    left_right = 1
    ende = 30
    start = 30
    maxima_x = []
    maxima_y = []
    for i in range(start, len(x_nom)-ende):
        if y_nom[i-left_right]<y_nom[i] and y_nom[i+left_right]<=y_nom[i] and y_nom[i-3]<y_nom[i] and y_nom[i+3]<y_nom[i]:
            maxima_x.append(x_nom[i])
            maxima_y.append(y_nom[i])
            #i += 500
    maxima_x, maxima_y = maxima_x[:14], maxima_y[:14]
    plt.plot(maxima_x, maxima_y, 'x', label='Maxima')
    maxima_x = np.asarray(maxima_x)
    U_0 = 0.000007
    # fitten:
    if x_fit is not None:
        params, covariance = curve_fit(fitfunktion, maxima_x,
                                        maxima_y,
                                        p0=[tau_erw.n, U_0])
        errors = np.sqrt(np.diag(covariance))
        print('tau= ', params[0] * 1e3, '±', errors[0] * 1e3)
        k = ufloat(params[0], errors[0])
        print('U_0= ', params[1], '±', errors[1])
        U_0 = ufloat(params[1], errors[1])

        print('Abweichung von tau_erw = ', abweichungen(tau_erw, k), '%')
        x_fit = np.linspace(x_fit[0], x_fit[1], 10000)
        plt.plot(x_fit, fitfunktion(x_fit, *params), label='Fit')
        label=r'Maximum$\:/\:e$'
        #label='test'
        plt.plot((xlim[0], xlim[1]), (maxima_y[0]/np.e, maxima_y[0]/np.e), label=label)

        for x_loop in x_fit:
            if fitfunktion(x_loop, *params) < maxima_y[0]/np.e:
                print('Abklingzeit =', x_loop - maxima_x[0], abklingzeit_erw, abweichungen(abklingzeit_erw, x_loop - maxima_x[0]))
                break

    if xlim is not None:
        plt.xlim(xlim[0], xlim[1])
    if ylim is not None:
        plt.ylim(ylim[0], ylim[1])
    xlabel = r'$t\:/\:\si{\second}$'
    ylabel = r"$U_\text{A}\:/\:\si{\volt}$"
    #xlabel, ylabel = 'test', 'test'
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc='best')

    # in matplotlibrc leider (noch) nicht möglich
    plt.tight_layout(pad=0.2, h_pad=1.08, w_pad=1.08)
    plt.savefig('build/'+file+'.pdf')
    plt.close()


if __name__ == '__main__':
    t, U_recht, U_daempf = np.genfromtxt('daten/daempf.txt', unpack='True', delimiter=',')

    print(t, U_recht, U_daempf)
    R = ufloat(9.96e3, 0.5e3)
    C = ufloat(22e-9, 1e-9)
    tau_erw = 20 * R * C
    print('kerw = ', tau_erw)
    plot(t, U_daempf, 'gedaempft', fitfunktion_daempf, tau_erw, 20*R*C, (-0.05, -0.03), xlim=(-0.05, -0.03))#(-0.05, -0.03)
