import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

T,I = np.genfromtxt('messung_1_5schritt.txt', unpack = 'True')

def offset(x):
    m = 0.0381877479326 #+- 5.68311567582e-07
    u = -46.2165498447 #+- 1.35745291816
    return np.exp(m*(x-u))

I_log = I[9:19]
T_rez = T[9:19]

for i in range(0,10):
    I_log[i] = np.log(I_log[i] - offset(T_rez[i]))
    T_rez[i] = 1/(T_rez[i]+273.15)

#print(I_log)

def linfunc(x,m,b):
    return m*x+b

# Messwerte, die für den Fit einbezogen werden(alle betrachteten):
plt.plot(T_rez,I_log,'k.',label = r'Messwerte', markersize = 4.4)

popt,pcov = curve_fit(linfunc,T_rez,I_log)

m = ufloat(popt[0],np.sqrt(pcov[0,0]))
print('Steigung:', m)
print('Abzisse:', popt[1],'+-',np.sqrt(pcov[1,1]))

k_B = 1.38065*10**(-23)
e = 1.602177*10**(-19)
W = -m*k_B
print('berechnete Aktivierungsenergie (Joule, eV):', W, W/e)

W_2 = ufloat(1.82,0.07) # in 10**(-19)
W_mean = 1/2*(W+W_2*10**(-19))
W_std = ((W-W_mean)**2 +(W_2*10**(-19)-W_mean)**2)**(1/2)
W_mitt = ufloat(W_mean.nominal_value, W_std.nominal_value + W_std.std_dev) # Fehler des Fehlers einfach aufaddieren
print('Mittelwert Aktivierungsenergie (Joule, eV):', W_mitt, W_mitt/e)

d = np.linspace(0.003,0.005,10)
plt.plot(d,linfunc(d,*popt), 'r-', label = r'Fit', linewidth = 1.2)

plt.grid()
plt.xlabel(r'$\frac{1}{T}/\si{\kelvin}^{-1}$')
plt.ylabel(r'$\log \left( I/\si{\pico\ampere} \right)$')
plt.xlim(0.00395,0.00425)
plt.ylim(-2.8,3)

plt.legend(loc = 'best')
plt.tight_layout()
plt.savefig('build/stromtemp_1_5_off_W1.pdf')
