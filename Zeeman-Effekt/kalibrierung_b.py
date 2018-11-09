import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat

I,B = np.genfromtxt('kalibrierung_b.txt', unpack = 'True') # I in A und B in mT

plt.errorbar(I,B, xerr = 0.5, yerr = 50, fmt = 'kx', label = r'Messwerte')

def f(x,m,b):
    return m*x + b

popt,pcov = curve_fit(f,I,B)
print('Steigung:', popt[0],'+-', np.sqrt(pcov[0,0]))
print('Abzissenabschnitt:', popt[1], '+-', np.sqrt(pcov[1,1]))

i = np.linspace(-0.3,22, 100)
plt.plot(i, popt[0]*i + popt[1], 'r-', label = r'linearer Fit')

#print('Eingabe (B in mT):')
#I_eingabe = float(input())
#print('Ausgabe (I in A):', (I_eingabe-popt[1])/popt[0])

slope = ufloat(popt[0],np.sqrt(pcov[0,0]))
intercept = ufloat(popt[1], np.sqrt(pcov[1,1]))

I_rot = ufloat(11,0.2)
I_blau_pi = ufloat(19,0.2)
I_blau_sigma = ufloat(5.9,0.2)

B_rot = f(I_rot, slope, intercept)
B_blau_pi = f(I_blau_pi, slope, intercept)
B_blau_sigma = f(I_blau_sigma, slope, intercept)
print('B für rot:', B_rot)
print('B für blau,pi:', B_blau_pi)
print('B für blau,sigma:', B_blau_sigma)

plt.xlim(-0.3,22)
plt.xlabel(r'$I/\si{\ampere}$')
plt.ylabel(r'$B/\si{\milli\tesla}$')
plt.legend(loc = 'best')
plt.grid()
plt.tight_layout()
plt.savefig('build/kalibrierung_b.pdf')
