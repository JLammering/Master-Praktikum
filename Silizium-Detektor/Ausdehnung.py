import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

Datenmatrix = np.loadtxt('18_04_30_Graesser_Lammering/Laserscan.txt', unpack = 'True')

#Kanäle:
channel_90 = Datenmatrix[89,:]
channel_91 = Datenmatrix[90,:]
channel_92 = Datenmatrix[91,:]
channel_93 = Datenmatrix[92,:]

channel_sum = channel_90 + channel_91 + channel_92 + channel_93

u = Datenmatrix.shape
x = np.zeros(u[1])

for i in range(0,u[1]):
    x[i] = i*10

plt.plot(x, channel_sum,'k.')

plt.grid()
plt.xlabel(r'$x/\si{\micro\meter}$')
plt.ylabel(r'$P_\text{Laser}$')
plt.legend(loc='best')
plt.savefig('build/Ausdehnung.pdf')



#laser_160 = Datenmatrix[87:95,16]
#laser_170 = Datenmatrix[87:95,17]
#laser_180 = Datenmatrix[87:95,18]
#laser_190 = Datenmatrix[87:95,19]
#
##Kanäle:
#channel = np.zeros(8)
#for i in range(87,95):
#    channel[i-87] = i+1
#
## Normierung vor dem Fit:
#laser_160 = laser_160/np.sum(laser_160)
#laser_170 = laser_170/np.sum(laser_170)
#laser_180 = laser_180/np.sum(laser_180)
#laser_190 = laser_190/np.sum(laser_190)
#
##Gaußfit für die Streifen 88-95(einschließlich) //8 werte//:
#def f(x,sigma,mu): # Gauß
#    return 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-(x-mu)**2/(2*sigma**2))
#
#popt_160,pcov_160 = curve_fit(f,channel,laser_160, bounds = ([0,2],[90,93]))
#popt_170,pcov_170 = curve_fit(f,channel,laser_170, bounds = ([0,2],[90,93]))
#popt_180,pcov_180 = curve_fit(f,channel,laser_180, bounds = ([0,2],[90,93]))
#popt_190,pcov_190 = curve_fit(f,channel,laser_190, bounds = ([0,2],[90,93]))
#
#x = np.linspace(87.5,95.5,1000)
#plt.plot(x, 1/np.sqrt(2*np.pi*popt_160[0]**2)*np.exp(-(x-popt_160[1])**2/(2*popt_160[0]**2)), 'b-', linewidth = 1, label = r'Gaußfit $\SI{160}{\micro\meter}$')
#plt.plot(x, 1/np.sqrt(2*np.pi*popt_170[0]**2)*np.exp(-(x-popt_170[1])**2/(2*popt_170[0]**2)), 'r-', linewidth = 1, label = r'Gaußfit $\SI{170}{\micro\meter}$')
#plt.plot(x, 1/np.sqrt(2*np.pi*popt_180[0]**2)*np.exp(-(x-popt_180[1])**2/(2*popt_180[0]**2)), 'k-', linewidth = 1, label = r'Gaußfit $\SI{180}{\micro\meter}$')
#plt.plot(x, 1/np.sqrt(2*np.pi*popt_190[0]**2)*np.exp(-(x-popt_190[1])**2/(2*popt_190[0]**2)), 'g-', linewidth = 1, label = r'Gaußfit $\SI{190}{\micro\meter}$')
#
#plt.plot(channel,laser_160,'b.', label = r'Signal bei $\SI{160}{\micro\meter}$ gemittelt')
#plt.plot(channel,laser_170,'r.', label = r'Signal bei $\SI{170}{\micro\meter}$ gemittelt')
#plt.plot(channel,laser_180,'k.', label = r'Signal bei $\SI{180}{\micro\meter}$ gemittelt')
#plt.plot(channel,laser_190,'g.', label = r'Signal bei $\SI{190}{\micro\meter}$ gemittelt')
#
#print('alle vier Mittelwerte:',popt_160[1],popt_170[1],popt_180[1],popt_190[1] )
#print('Differenz der Mittelwerte(180-170 approx 10):', popt_180[1]-popt_170[1])
#print('arithmetisches Mittel der Standardabweichungen:', 0.5*(popt_170[0]+ popt_180[0] + popt_160[0]+ popt_190[0]))
#plt.xlim(87.5,95.5)

##Gaußfit für die Streifen 85-98(einschließlich) //14 werte//:
#streif = np.zeros(8)
#for i in range(87,95):
#    streif[i-87] = np.sum(Datenmatrix[i,:])/35
#
## davor erst normieren! (hier easy, da bins 1 breit sind (1 Streifen))
#streif_norm = streif/np.sum(streif)
#
#def f(x,sigma,mu): # Gauß
#    return 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-(x-mu)**2/(2*sigma**2))
#
#popt,pcov = curve_fit(f,channel,streif_norm, bounds = ([0,90],[2,93]))
#
#plt.plot(channel, streif_norm, 'k.', markersize=3, label = r'Signal gemittelt')
#x = np.linspace(84.5,98.5,1000)
#plt.plot(x, 1/np.sqrt(2*np.pi*popt[0]**2)*np.exp(-(x-popt[1])**2/(2*popt[0]**2)), 'r-', linewidth = 1, label = r'Gaußfit')
#print('Gaußfit(mu, sigma)', popt[1], popt[0])
#pitch = 161.68536371
#Ausdehnung = 4*popt[0]*pitch - 35 # in micrometern
#print('Ausdehnung des Lasers(in um):', Ausdehnung)
#
#t = np.linspace(popt[1]-2*popt[0], popt[1]+2*popt[0], 100)
#plt.plot(t, 0*t + f(popt[1]-2*popt[0],popt[0],popt[1]), 'b-', label = r'$2\sigma$-Umgebung', linewidth = 0.8)
