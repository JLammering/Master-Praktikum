import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

T,I = np.genfromtxt('messung_2schritt.txt', unpack = 'True')

# betrachtete Werte (erster Peak, letzter Wert ca. 0):
T = T[0:25]
I = I[0:25]

def offset(x):
    m = 0.0381877479326 #+- 5.68311567582e-07
    u = -46.2165498447 #+- 1.35745291816
    return np.exp(m*(x-u))

for i in range(0,len(T)):
    I[i] = I[i] - offset(T[i])

# Zunächst wird eine Art Trapezregel implementiert, um das auftretende Integral numerisch zu bestimmen:

balken = np.zeros(24) # Flächeninhalt der Balken

for n in range(0,24):
    balken[n] = 0.5 * (T[n+1]-T[n])*(I[n+1]+I[n])

# Integral für jeden Stromwert:
I_int = np.zeros(24)

for n in range(0,24):
    I_int[n] = np.sum(balken[n:24])

# "rechte Seite" für jeden Stromwert:
I_log = np.zeros(24)

for n in range(2,23):# Der letzte Wert und die ersten beiden werden herausgenommen
    I_log[n] = np.log(I_int[n]/I[n])

# "linke Seite" für jeden Temperaturwert:
T_rez = np.zeros(24)

for n in range(0,24):
    T_rez[n] = 1/(T[n]+273.15)

plt.plot(T_rez[2:23], I_log[2:23], 'k.', label = r'Messwerte')

def linfunc(x,m,b):
    return m*x+b

popt,pcov = curve_fit(linfunc,T_rez[2:23],I_log[2:23])

m = ufloat(popt[0],np.sqrt(pcov[0,0]))
print('Steigung:', m)
print('Abzisse:', popt[1],'+-',np.sqrt(pcov[1,1]))

k_B = 1.38065*10**(-23)
e = 1.602177*10**(-19)
W = m*k_B
print('berechnete Aktivierungsenergie (Joule, eV):', W, W/e)

d = np.linspace(0,1,10)
plt.plot(d,linfunc(d,*popt), 'r-', label = r'Anpassung')

plt.grid()
plt.xlabel(r'$\frac{1}{T}/\si{\kelvin}^{-1}$')
plt.ylabel(r'$f\left(I \right)$')
plt.xlim(0.0036,0.00435)
plt.ylim(-1,9)

plt.legend(loc = 'best')
plt.tight_layout()
plt.savefig('build/stromtemp_2_off_W2')
