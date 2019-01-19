import numpy as np
import matplotlib.pyplot as plt

T,I = np.genfromtxt('messung_2schritt.txt', unpack = 'True')

def offset(x):
    m = 0.0381877479326 #+- 5.68311567582e-07
    u = -46.2165498447 #+- 1.35745291816
    return np.exp(m*(x-u))

for i in range(0,len(T)):
    I[i] = I[i] - offset(T[i])

plt.plot(T[0:25],I[0:25],'k.',label=r'Messwerte', markersize = 6)
plt.plot(T[5:13],I[5:13],'r.',label=r'W-Messwerte(1)', markersize = 6.4)

plt.grid()
plt.xlabel(r'$T/\si{\celsius}$')
plt.ylabel(r'$I/\si{\pico\ampere}$')
plt.xlim(-55,3)
plt.ylim(-3,18)

plt.legend(loc = 'best')
plt.tight_layout()
plt.savefig('build/stromtemp_2_off.pdf')
