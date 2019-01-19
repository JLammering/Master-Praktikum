import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

T, I = np.genfromtxt('messung_1_5schritt.txt', unpack = 'True')

t = np.zeros(len(T))

for i in range(0,len(T)):
    t[i] = i+1

plt.plot(t,T,'k.', markersize = 4, label = r'Messwerte')

def linfunc(x,m,b):
    return m*x+b

popt,pcov = curve_fit(linfunc, t[5:], T[5:])

heizrate = ufloat(popt[0]/60, np.sqrt(pcov[0,0])/60) # Grad pro Sekunde
b = ufloat(popt[1], np.sqrt(pcov[1,1]))

print('heizrate:', heizrate)
print('Abzisse:', b)

d = np.linspace(0,78,10)
plt.plot(d,linfunc(d,*popt), label = r'linearer Fit', linewidth = 0.9)

plt.legend(loc = 'best')
plt.xlabel(r'$t/\si{\minute}$')
plt.ylabel(r'$T/\si{\celsius}$')
plt.xlim(0,78)
plt.grid()
plt.tight_layout()
plt.savefig('build/heizrate_1_5schritt.pdf')