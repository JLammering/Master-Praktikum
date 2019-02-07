import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

T,I = np.genfromtxt('messung_2schritt.txt', unpack = 'True')

plt.plot(T,I,'k.', label = r'Messwerte(2)')

# für den Offset betrachtete Messwerte:

a = 5 # obere Grenze des ersten Arrays
b_1 = 26 # untere Grenze des zweiten Arrays
b_2 = 33 # obere Grenze des zweiten Arrays
T_beg = T[0:a]
I_beg = I[0:a]
T_mid = T[b_1:b_2]
I_mid = I[b_1:b_2]

plt.plot(T_beg, I_beg, 'r.', label = r'Messwerte(1)')
plt.plot(T_mid, I_mid, 'r.')

def offset(T,m,u):
    return np.exp(m*(T-u))

popt,pcov = curve_fit(offset,np.append(T_beg,T_mid),np.append(I_beg,I_mid))

x = np.linspace(-60,80)
plt.plot(x, offset(x,*popt), 'r-', linewidth = 1.0, label = r'Exponentielle Anpassung')

print('exp-Faktor:', popt[0],'+-', np.sqrt(pcov[0,0]))
print('Verschiebung:', popt[1],'+-', np.sqrt(pcov[1,1]))

plt.grid()
plt.xlabel(r'$T/\si{\celsius}$')
plt.ylabel(r'$I/\si{\pico\ampere}$')
plt.xlim(-55,63)
plt.ylim(0,57)
plt.legend(loc = 'best')
plt.tight_layout()
plt.savefig('build/stromtemp_2.pdf')
