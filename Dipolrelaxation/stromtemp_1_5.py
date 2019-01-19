import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

T,I = np.genfromtxt('messung_1_5schritt.txt', unpack = 'True')

plt.plot(T,I,'k.', label = r'Messwerte(2)')

# für den Offset betrachtete Messwerte:
a_1 = 4 # untere Grenze des ersten Arrays
a_2 = 6 # obere Grenze des ersten Arrays
b_1 = 33 # untere Grenze des zweiten Arrays
b_2 = 45 # obere Grenze des zweiten Arrays
T_beg = T[a_1:a_2]
I_beg = I[a_1:a_2]
T_mid = T[b_1:b_2]
I_mid = I[b_1:b_2]

plt.plot(T_beg, I_beg, 'r.', label = r'Messwerte(1)')
plt.plot(T_mid, I_mid, 'r.')

def offset(T,m,u):
    return np.exp(m*(T-u))

popt,pcov = curve_fit(offset,np.append(T_beg,T_mid),np.append(I_beg,I_mid))

x = np.linspace(-50,63,500)
plt.plot(x, offset(x,*popt), 'r-', linewidth = 1.0, label = r'Exponential-Fit')

print('exp-Faktor:', popt[0],'+-', np.sqrt(pcov[0,0]))
print('Verschiebung:', popt[1],'+-', np.sqrt(pcov[1,1]))

plt.grid()
plt.xlabel(r'$T/\si{\celsius}$')
plt.ylabel(r'$I/\si{\pico\ampere}$')
plt.xlim(-50,63)
plt.ylim(0,40)
plt.legend(loc = 'best')
plt.tight_layout()
plt.savefig('build/stromtemp_1_5.pdf')
