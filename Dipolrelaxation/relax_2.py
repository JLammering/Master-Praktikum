import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

T,I = np.genfromtxt('messung_2schritt.txt', unpack = 'True')

# betrachtete Werte (erster Peak, letzter Wert ca. 0):
T = T[0:25] + 273.15
I = I[0:25]

def offset(x):
    m = 0.0381877479326 #+- 5.68311567582e-07
    u = -46.2165498447 #+- 1.35745291816
    return np.exp(m*(x-u))

for i in range(0,len(T)):
    I[i] = I[i] - offset(T[i] - 273.15)

# Zunächst wird eine Art Trapezregel implementiert, um das auftretende Integral numerisch zu bestimmen:

balken = np.zeros(24) # Flächeninhalt der Balken

for n in range(0,24):
    balken[n] = 0.5 * (T[n+1]-T[n])*(I[n+1]+I[n])

# Integral für jeden Stromwert:
I_int = np.zeros(24)

for n in range(0,24):
    I_int[n] = np.sum(balken[n:24])

# Tau(T) für jeden Stromwert:
I_end = np.zeros(24)

for n in range(2,23):# Der letzte Wert und die ersten beiden werden herausgenommen
    I_end[n] = 30* I_int[n]/I[n]

plt.plot(T[2:23], I_end[2:23], 'k.')

def fit(x,tau_0):
    a = 1.78 * 10**4
    return tau_0 * np.exp(a/x)

print(I_end[10:22])
popt,pcov = curve_fit(fit,T[6:23],I_end[6:23])
plt.plot(T[2:5],I_end[2:5],'r.')
#plt.plot(T[2],I_end[2],'r.')

print(popt)

d = np.linspace(230,275,500)
plt.plot(d, fit(d,*popt),'r-')

plt.grid()
plt.xlabel(r'$T/\si{\kelvin}$')
plt.ylabel(r'$\tau(T)/\si{\second}$')
plt.xlim(230,275)
#plt.ylim(0,1000)

plt.legend(loc = 'best')
plt.tight_layout()
plt.savefig('build/relax_2.pdf')
