import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

T,I = np.genfromtxt('messung_1_5schritt.txt', unpack = 'True')

# betrachtete Werte (erster Peak, letzter Wert ca. 0):
T = T[0:35]
I = I[0:35]

def offset(x):
    m = 0.034020771068 #+- 0.00156440403239
    u = -44.9731489791 #+- 2.46942161367
    return np.exp(m*(x-u))

for i in range(0,len(T)):
    I[i] = I[i] - offset(T[i])

# Zunächst wird eine Art Trapezregel implementiert, um das auftretende Integral numerisch zu bestimmen:

balken = np.zeros(34) # Flächeninhalt der Balken

for n in range(0,34):
    balken[n] = 0.5 * (T[n+1]-T[n])*(I[n+1]+I[n])

# Integral für jeden Stromwert:
I_int = np.zeros(34)

for n in range(0,34):
    I_int[n] = np.sum(balken[n:34])

# "rechte Seite" für jeden Stromwert:
I_log = np.zeros(34)

for n in range(9,34):# Der letzte Wert und die ersten neun werden herausgenommen
    I_log[n] = np.log(I_int[n]/I[n])

# "linke Seite" für jeden Temperaturwert:
T_rez = np.zeros(34)

for n in range(0,34):
    T_rez[n] = 1/(T[n]+273.15)

plt.plot(T_rez[9:34], I_log[9:34], 'k.', label = r'Messwerte')

def linfunc(x,m,b):
    return m*x+b

popt,pcov = curve_fit(linfunc,T_rez[9:34],I_log[9:34])

m = ufloat(popt[0],np.sqrt(pcov[0,0]))
print('Steigung:', m)
print('Abzisse:', popt[1],'+-',np.sqrt(pcov[1,1]))

k_B = 1.38065*10**(-23)
e = 1.602177*10**(-19)
W = m*k_B
print('berechnete Aktivierungsenergie (joule, eV):', W, W/e)
m_2 = ufloat(1.29,0.04)*10**4
W_mean = k_B* 1/2*(m+m_2)
W_std = ((k_B*m-W_mean)**2 +(k_B*m_2-W_mean)**2)**(1/2)
W_mitt = ufloat(W_mean.nominal_value, W_std.nominal_value + W_std.std_dev)
print('gemittelte Aktivierungsenergie (joule, eV):',W_mitt, W_mitt/e)

d = np.linspace(0,1,10)
plt.plot(d,linfunc(d,*popt), 'r-', label = r'Anpassung')

plt.grid()
plt.xlabel(r'$\frac{1}{T}/\si{\kelvin}^{-1}$')
plt.ylabel(r'$f\left(I \right)$')
plt.xlim(0.0036,0.00425)
plt.ylim(-2,8)

plt.legend(loc = 'best')
plt.tight_layout()
plt.savefig('build/stromtemp_1_5_off_W2')
