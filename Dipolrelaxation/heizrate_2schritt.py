import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import curve_fit

T, I = np.genfromtxt('messung_2schritt.txt', unpack = 'True')

t = np.zeros(len(T))

for i in range(0,len(T)):
    t[i] = i+1

plt.plot(t,T,'k.', markersize = 4, label = r'Messwerte(1)')
plt.plot(t[0:5], T[0:5], 'r.', markersize = 4.3, label = r'Messwerte(2)') # Messwerte, die aus dem Fit genommen werden

def linfunc(x,m,b):
    return m*x+b

popt,pcov = curve_fit(linfunc, t[5:], T[5:])

d = np.linspace(0,60,10)
plt.plot(d,linfunc(d,*popt), label = r'linearer Fit')

plt.grid()
plt.savefig('build/heizrate_2schritt.pdf')
