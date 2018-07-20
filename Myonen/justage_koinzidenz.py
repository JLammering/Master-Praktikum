import matplotlib.pyplot as plt
import numpy as np
from functions import werteZuTabelle, abweichungen, mittelwert
from scipy.optimize import curve_fit, fmin
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy import constants
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

Verzögerung, Counts = np.genfromtxt('justage_koinzidenz.txt', unpack = 'True')
Rate = Counts/10 # da 10 Sekunden Messzeit
Rate_err = np.sqrt(Counts)/10
#print(Rate_err)

# Arrays für den Plateaufit erstellen:
Verzögerung_Plateau = np.zeros(27)
Rate_Plateau = np.zeros(27)
a = 0
for i in range(0,len(Verzögerung)):
    if Verzögerung[i] > -7.49:
        if Verzögerung[i] < 13.01:
            Verzögerung_Plateau[a] = Verzögerung[i]
            Rate_Plateau[a] = Rate[i]
            a = a+1

# arithmetisches Mittel:
Med_val = np.mean(Rate_Plateau)
Med_std = np.std(Rate_Plateau)
Med = ufloat(Med_val,Med_std)
print('Plateaumittelwert',Med)

x = np.linspace(-15,25, 100)
plt.plot(x, 0*x + Med_val, 'r-', linewidth = 1.1, label = r'Plateaumittelwert')
plt.plot(x, 0*x + Med_val/2, 'r--', linewidth = 1.1, label = r'Plateaumittelwert/2')

# Arrays für die Anstiegsfits erstellen:
Verzögerung_links = np.zeros(11)
Rate_links = np.zeros(11)
a = 0
for i in range(0,len(Verzögerung)):
    if Verzögerung[i] < -7.49:
        Verzögerung_links[a] = Verzögerung[i]
        Rate_links[a] = Rate[i]
        a = a+1

Verzögerung_rechts = np.zeros(12)
Rate_rechts = np.zeros(12)
a = 0
for i in range(0,len(Verzögerung)):
    if Verzögerung[i] > 13.01:
        Verzögerung_rechts[a] = Verzögerung[i]
        Rate_rechts[a] = Rate[i]
        a = a+1

def f(x,m,b):#Gerade
    return m*x + b

popt_links,pcov_links = curve_fit(f, Verzögerung_links, Rate_links)
popt_rechts,pcov_rechts = curve_fit(f, Verzögerung_rechts, Rate_rechts)

m_uf_links = ufloat(popt_links[0], np.sqrt(pcov_links[0,0]))
b_uf_links = ufloat(popt_links[1], np.sqrt(pcov_links[1,1]))

m_uf_rechts = ufloat(popt_rechts[0], np.sqrt(pcov_rechts[0,0]))
b_uf_rechts = ufloat(popt_rechts[1], np.sqrt(pcov_rechts[1,1]))

print('Steigung links:',m_uf_links,'Abzisse links',b_uf_links)
print('Steigung rechts:',m_uf_rechts,'Abzisse rechts',b_uf_rechts)
print('dt_links:',(Med/2-b_uf_links)/m_uf_links,' dt_rechts:',(Med/2-b_uf_rechts)/m_uf_rechts)
print('Halbwertsbreite:', (Med/2-b_uf_rechts)/m_uf_rechts - (Med/2-b_uf_links)/m_uf_links)

plt.plot(x,popt_links[0]*x + popt_links[1],'k-' ,linewidth = 1.1, label = r'Linksfit')
plt.plot(x,popt_rechts[0]*x + popt_rechts[1],'b-' ,linewidth = 1.1, label = r'Rechtsfit')

Rate_Plateau_err = np.zeros(len(Rate_Plateau))
for k in range(0,len(Rate_Plateau)):
    Rate_Plateau_err[k] = 1/10*np.sqrt(10*Rate_Plateau[k])
#print(Rate_Plateau,Rate_Plateau_err)
Rate_Plateau = unp.uarray(Rate_Plateau, Rate_Plateau_err)

Rate_links_err = np.zeros(len(Rate_links))
for k in range(0,len(Rate_links)):
    Rate_links_err[k] = 1/10*np.sqrt(10*Rate_links[k])
Rate_links = unp.uarray(Rate_links, Rate_links_err)

Rate_rechts_err = np.zeros(len(Rate_rechts))
for k in range(0,len(Rate_rechts)):
    Rate_rechts_err[k] = 1/10*np.sqrt(10*Rate_rechts[k])
Rate_rechts = unp.uarray(Rate_rechts, Rate_rechts_err)

plt.errorbar(Verzögerung_Plateau, unp.nominal_values(Rate_Plateau),xerr=0, yerr=unp.std_devs(Rate_Plateau), fmt='r.', markersize = 5.5, label = r'Plateaufit Messwerte')
plt.errorbar(Verzögerung_links, unp.nominal_values(Rate_links),xerr=0, yerr=unp.std_devs(Rate_links), fmt='kx', markersize = 4.5, label = r'Linksfit Messwerte')
plt.errorbar(Verzögerung_rechts, unp.nominal_values(Rate_rechts),xerr=0, yerr=unp.std_devs(Rate_rechts), fmt='b+', markersize = 5.5, label = r'Rechtsfit Messwerte')

plt.xlabel(r'$\Delta t/\si{\nano\second}$')
plt.ylabel(r'I/\si{\per\second}')
plt.legend(loc = 'best')
plt.xlim(-14.3,21.8)
plt.ylim(4,24)
plt.grid()
plt.savefig('build/justage_koinzidenz.pdf')
