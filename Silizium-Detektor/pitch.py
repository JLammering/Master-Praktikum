import numpy as np
import matplotlib.pyplot as plt

Datenmatrix = np.loadtxt('18_04_30_Graesser_Lammering/Laserscan.txt', unpack = 'True')

#Kanäle:
channel = np.zeros(128)
for i in range(0,128):
    channel[i] = i+1

streif = np.zeros(128)
for i in range(0,128):
    streif[i] = np.sum(Datenmatrix[i,:])/35

plt.plot(channel[0:90], streif[0:90], 'ko', markersize=1.5, label = r'Messwerte')
plt.plot(channel[90:92], streif[90:92], 'r+', markersize=3, label = r'Messwerte zur Bestimmung der pitch')
plt.plot(channel[92:128], streif[92:128], 'ko', markersize=1.5)

plt.xlim(0,129)
plt.ylim(-2,75)
plt.grid()
plt.xlabel(r'$i$')
plt.ylabel(r'$\text{Signal}_\text{average}/\text{ADC}$')
plt.legend(loc='best')
plt.savefig('build/pitch.pdf')
