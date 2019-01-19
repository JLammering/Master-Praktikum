import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

T,I = np.genfromtxt('messung_1_5schritt.txt', unpack = 'True')

def offset(x):
    m = 0.034020771068 #+- 0.00156440403239
    u = -44.9731489791 #+- 2.46942161367
    return np.exp(m*(x-u))

for i in range(0,len(T)):
    I[i] = I[i] - offset(T[i])

plt.plot(T[0:35],I[0:35],'k.',label=r'Messwerte', markersize = 5)
plt.plot(T[9:19],I[9:19],'r.',label=r'W-Messwerte(1)', markersize = 5.4)

# Parabelfit zur Bestimmung des Maximums
I_parabfit = I[20:28]
T_parabfit = T[20:28]
plt.plot(T_parabfit,I_parabfit,'c.',label=r'Fit-Messwerte', markersize = 5.4)

def parab(x,a,b,c):
    return a*x**2 +b*x +c

popt,pcov = curve_fit(parab,T_parabfit, I_parabfit)

a = ufloat(popt[0], np.sqrt(pcov[0,0]))
b = ufloat(popt[1], np.sqrt(pcov[1,1]))
c = ufloat(popt[2], np.sqrt(pcov[2,2]))
T_max = -b/(2*a)

print('Fitparameter(a,b,c):', a, b, c)
print('T_max:', T_max)

T_max = T_max + 273.15 # kelvin
heizrate = ufloat(0.02411,0.00003)
W = ufloat(1.7,0.2) # Potenzen mit k_B verrechnet
k_B = 1.38065*10**(-4)

tau_0 = k_B * T_max**2/(heizrate*W) *unp.exp(- W/(k_B * T_max))
print('char.Relaxationszeit:', tau_0)

d = np.linspace(-30,0,500)
plt.plot(d, parab(d,*popt), 'b-', label = r'Parabelfit', linewidth = 1.0)

plt.grid()
plt.xlabel(r'$T/\si{\celsius}$')
plt.ylabel(r'$I/\si{\pico\ampere}$')
plt.xlim(-50,3)
plt.ylim(-3,15)

plt.legend(loc = 'best')
plt.tight_layout()
plt.savefig('build/stromtemp_1_5_off.pdf')
