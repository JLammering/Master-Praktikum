import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

channel_values = np.genfromtxt('20180704/kalibration.txt', unpack = 'True')

channel_number = np.zeros(20)

a = 0
for i in range(0,len(channel_values)):
    if channel_values[i] != 0:
        channel_number[a] = i+1
        a = a+1

puls_diff = np.zeros(20)
for k in range(0,20):
    puls_diff[k] = (k+1)*0.5

puls_diff[19] = 9.9

#print(channel_number, puls_diff)

def t(c, a,b): #Zeit i.A. vom Kanal + Konstanten a,b
    return a*c + b

popt,pcov = curve_fit(t, channel_number, puls_diff)
np.savetxt('kalibration_data.txt', np.array([popt[0],0,np.sqrt(pcov[0,0]),0,0,popt[1],0,np.sqrt(pcov[1,1])]))

x = np.linspace(0,460)
plt.plot(x, popt[0]*x + popt[1], 'r-', linewidth = 1.1, label = r'Regressionsgerade')
plt.plot(channel_number,puls_diff,'k+',markersize = 8.0, label = r'Messwerte')
np.savetxt('kalibration_table.txt',np.array(((channel_number),(puls_diff))).T)

plt.xlabel(r'ch')
plt.ylabel(r'$\Delta t/\si{\nano\second}$')
plt.xlim(0,460)
plt.grid()
plt.legend(loc = 'best')
plt.savefig('build/kalibration.pdf')
