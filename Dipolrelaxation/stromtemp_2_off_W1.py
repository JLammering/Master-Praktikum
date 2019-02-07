import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

T,I = np.genfromtxt('messung_2schritt.txt', unpack = 'True')

def offset(x):
    m = 0.0381877479326 #+- 5.68311567582e-07
    u = -46.2165498447 #+- 1.35745291816
    return np.exp(m*(x-u))

a = 18
I_log = np.zeros(a)
T_rez = np.zeros(a)

for i in range(0,a):
    k = I[i] - offset(T[i])
    if k > 0:
        I_log[i] = np.log(I[i] - offset(T[i]))
        T_rez[i] = 1/(T[i]+273.15)

#plt.plot(T_rez[0:a],I_log[0:a],'k.', label = r'Messwerte', markersize = 4)

def linfunc(x,m,b):
    return m*x+b

# Messwerte, die für den Fit einbezogen werden:
T_rez_used = T_rez[5:13]
I_log_used = I_log[5:13]
plt.plot(T_rez_used,I_log_used,'k.',label = r'Anpassungs-Messwerte', markersize = 4.4)

popt,pcov = curve_fit(linfunc,T_rez_used,I_log_used)

m = ufloat(popt[0],np.sqrt(pcov[0,0]))
print('Steigung:', m)
print('Abzisse:', popt[1],'+-',np.sqrt(pcov[1,1]))

k_B = 1.38065*10**(-23)
e = 1.602177*10**(-19)
W = -m*k_B
print('berechnete Aktivierungsenergie (Joule, eV):', W, W/e)

d = np.linspace(0,1,10)
plt.plot(d,linfunc(d,*popt), 'r-', label = r'Anpassung', linewidth = 1.2)

plt.grid()
plt.xlabel(r'$\frac{1}{T}/\si{\kelvin}^{-1}$')
plt.ylabel(r'$\log \left( I/\si{\pico\ampere} \right)$')
plt.xlim(0.0039,0.00425)
plt.ylim(-2,3)

plt.legend(loc = 'best')
plt.tight_layout()
plt.savefig('build/stromtemp_2_off_W1.pdf')
