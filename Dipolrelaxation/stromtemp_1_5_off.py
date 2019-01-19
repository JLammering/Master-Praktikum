import numpy as np
import matplotlib.pyplot as plt

T,I = np.genfromtxt('messung_1_5schritt.txt', unpack = 'True')

def offset(x):
    m = 0.034020771068 #+- 0.00156440403239
    u = -44.9731489791 #+- 2.46942161367
    return np.exp(m*(x-u))

for i in range(0,len(T)):
    I[i] = I[i] - offset(T[i])

plt.plot(T[0:35],I[0:35],'k.',label=r'Messwerte', markersize = 5)
plt.plot(T[9:19],I[9:19],'r.',label=r'W-Messwerte(1)', markersize = 5.4)

plt.grid()
plt.xlabel(r'$T/\si{\celsius}$')
plt.ylabel(r'$I/\si{\pico\ampere}$')
plt.xlim(-50,3)
plt.ylim(-3,15)

plt.legend(loc = 'best')
plt.tight_layout()
plt.savefig('build/stromtemp_1_5_off.pdf')
