import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

Datenmatrix = np.loadtxt('18_04_30_Graesser_Lammering/Laserscan.txt', unpack = 'True')

#Kanäle:
channel = np.zeros(8)
for i in range(87,95):
    channel[i-87] = i+1

#Gaußfit für die Streifen 85-98(einschließlich) //14 werte//:
streif = np.zeros(8)
for i in range(87,95):
    streif[i-87] = np.sum(Datenmatrix[i,:])/35

# davor erst normieren! (hier easy, da bins 1 breit sind (1 Streifen))
streif_norm = streif/np.sum(streif)

def f(x,sigma,mu): # Gauß
    return 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-(x-mu)**2/(2*sigma**2))

popt,pcov = curve_fit(f,channel,streif_norm, bounds = ([0,90],[2,93]))

plt.plot(channel, streif_norm, 'k.', markersize=3, label = r'Signal gemittelt')
x = np.linspace(84.5,98.5,1000)
plt.plot(x, 1/np.sqrt(2*np.pi*popt[0]**2)*np.exp(-(x-popt[1])**2/(2*popt[0]**2)), 'r-', linewidth = 1, label = r'Gaußfit')
print('Gaußfit(mu, sigma)', popt[1], popt[0])
pitch = 161.68536371
Ausdehnung = 4*popt[0]*pitch - 35 # in micrometern
print('Ausdehnung des Lasers(in um):', Ausdehnung)

t = np.linspace(popt[1]-2*popt[0], popt[1]+2*popt[0], 100)
plt.plot(t, 0*t + f(popt[1]-2*popt[0],popt[0],popt[1]), 'b-', label = r'$2\sigma$-Umgebung', linewidth = 0.8)

plt.grid()
plt.xlim(87.5,95.5)
plt.xlabel(r'$i$')
plt.ylabel(r'$P_\text{Laser}$')
plt.legend(loc='best')
plt.savefig('build/Ausdehnung.pdf')
