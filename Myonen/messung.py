import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy import constants
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

#1456661
#4077

channel_values = np.genfromtxt('20180704/messung.txt', unpack = 'True')
#print(len(channel_values))

kalibration_data = np.genfromtxt('kalibration_data.txt', unpack = 'True')

def kalib(c): # channel -> time
    return kalibration_data[0]*c + kalibration_data[5]

time = np.zeros(len(channel_values))

for i in range(0,len(time)):
    time[i] = kalib(i+1)

channel_errors = np.sqrt(channel_values)
plt.errorbar(time[0:4],channel_values[0:4],xerr = 0, yerr = channel_errors[0:4], fmt = 'b.',markersize = 1.3, elinewidth = 0.42, label = r'abgeschnittene Messwerte')
plt.errorbar(time[4:464],channel_values[4:464],xerr = 0, yerr = channel_errors[4:464], fmt = 'k.',markersize = 1.3, elinewidth = 0.42, label = r'relevante Messwerte')
plt.errorbar(time[464:],channel_values[464:],xerr = 0, yerr = channel_errors[464:], fmt = 'b.',markersize = 1.3, elinewidth = 0.42)

def N(t, N_0, l, U): #N(t) + Fitparameter
    return N_0*np.exp(-l*t) +U

popt,pcov = curve_fit(N,time[4:464],channel_values[4:464])
print('popt,pcov(N,l,U):',popt,np.diag(pcov))

t = np.linspace(-0.05,11.5)
plt.plot(t, N(t, popt[0],popt[1],popt[2]), 'r-', linewidth = 1.25, label = r'Fitfunktion (mit $U_\text{n}$)')

tau_lit = 2.196 * 10**(-6)
l_mess = ufloat(popt[1], np.sqrt(pcov[1,1]))
tau_mess = 1/l_mess * 10**(-6)

#print(np.sum(channel_values))
print('tau Literaturwert,Messwert:', tau_lit, tau_mess)

plt.xlim(-0.05,11.5)
plt.ylim(-2.5, 70)
plt.grid()
plt.legend(loc = 'best')
plt.xlabel(r't/\si{\micro\second}')
plt.ylabel(r'$N$/counts')
plt.savefig('build/messung.pdf')
