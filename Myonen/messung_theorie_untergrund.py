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

kalibration_data = np.genfromtxt('kalibration_data.txt', unpack = 'True')

def kalib(c): # channel -> time
    return kalibration_data[0]*c + kalibration_data[5]

time = np.zeros(len(channel_values))

for i in range(0,len(time)):
    time[i] = kalib(i+1)

channel_errors = np.sqrt(channel_values)

# U_theo:
t_mess = 85721 #in s
N_start = ufloat(1456661, np.sqrt(1456661))
I_mess = N_start/t_mess
T_s = 10.3*10**(-6) #in s
mu = I_mess*T_s
p_1 = mu * unp.exp(-mu)
channel_a = -kalibration_data[5]/kalibration_data[0]
channel_b = (10.3 - kalibration_data[5])/kalibration_data[0]
channel_anz = 461
U_ges = p_1*N_start

U_theo = U_ges/channel_anz
print('I_mess', I_mess)
print('U_ges', U_ges)
print('channel_int:', channel_a, channel_b)
print('Untergrund-Theoriewert:', U_theo)

plt.errorbar(time[0:4],channel_values[0:4],xerr = 0, yerr = channel_errors[0:4], fmt = 'b.',markersize = 1.3, elinewidth = 0.42, label = r'abgeschnittene Messwerte')
plt.errorbar(time[4:464],channel_values[4:464]-unp.nominal_values(U_theo),xerr = 0, yerr = channel_errors[4:464], fmt = 'k.',markersize = 1.3, elinewidth = 0.42, label = r'relevante Messwerte (mit $U_\text{t}$)')
plt.errorbar(time[464:],channel_values[464:],xerr = 0, yerr = channel_errors[464:], fmt = 'b.',markersize = 1.3, elinewidth = 0.42)

def N(t, N_0, l): #N(t) + Fitparameter
    return N_0*np.exp(-l*t)

popt,pcov = curve_fit(N,time[4:464],channel_values[4:464]-unp.nominal_values(U_theo))
print('popt,pcov(N,l)',popt,np.diag(pcov))

t = np.linspace(-0.05,11.5)
plt.plot(t, N(t, popt[0],popt[1]), 'r-', linewidth = 1.25, label = r'Fitfunktion')

tau_lit = 2.196 * 10**(-6)
l_mess = ufloat(popt[1], np.sqrt(pcov[1,1]))
tau_mess = 1/l_mess * 10**(-6)

#print(np.sum(channel_values))
print('Literaturwert,Messwert:', tau_lit, tau_mess)

plt.xlim(-0.05,11.5)
plt.ylim(-2.5, 70)
plt.grid()
plt.legend(loc = 'best')
plt.xlabel(r't/\si{\micro\second}')
plt.ylabel(r'$N$/counts')
plt.savefig('build/messung_t_u.pdf')
