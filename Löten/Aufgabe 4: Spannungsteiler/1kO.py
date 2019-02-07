import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

I,U = np.genfromtxt('Messwerte1kO.txt', unpack = 'True')

def lin(x,m,b):
    return m*x + b

popt,pcov = curve_fit(lin,I,U)

x = np.linspace(0,5)
plt.plot(x, lin(x,*popt), 'r-', label = r'linearer Fit')
plt.plot(I,U,'kx', label = r'Messwerte')

print('Lastwiderstand(Steigung) in KiloOhm:', popt[0], '+-', np.sqrt(pcov[0,0]))
plt.xlabel('I/mA')
plt.ylabel('U/V')
plt.grid()
plt.legend(loc = 'best')
plt.savefig('1kO.pdf')
