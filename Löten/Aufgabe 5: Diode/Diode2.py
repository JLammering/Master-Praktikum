import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

I,U = np.genfromtxt('MesswerteDiode2.txt', unpack = 'True')

def lin(x,m,b):
    return m*x + b

#popt,pcov = curve_fit(lin,I,U)

#x = np.linspace(0,5)
#plt.plot(x, lin(x,*popt), 'r-', label = r'linearer Fit')
plt.plot(U,I,'kx', label = r'Messwerte')

plt.xlabel('I/mA')
plt.ylabel('U/V')
plt.grid()
plt.legend(loc = 'best')
plt.savefig('Diode2.pdf')
