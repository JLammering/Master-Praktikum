import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat

#pi:
values_delta_s = np.genfromtxt('Spektrallinienwerte/blue_delta_s.txt', unpack = 'True')
values_var_s_1 = np.genfromtxt('Spektrallinienwerte/blue_1_var_s.txt', unpack = 'True')

sh = np.shape(values_delta_s)[1]

delta_s = unp.uarray(np.zeros([sh]),np.zeros([sh]))
var_s_1 = unp.uarray(np.zeros([sh]),np.zeros([sh])) # beide matrizen gleichgroß
s_quot_1 = unp.uarray(np.zeros([sh]),np.zeros([sh]))
count = np.zeros([sh])

for i in range(0, sh):
    delta_s[i] = ufloat(values_delta_s[1,i],10) - ufloat(values_delta_s[0,i],10)
    var_s_1[i] = ufloat(values_var_s_1[1,i],10) - ufloat(values_var_s_1[0,i],10)
    s_quot_1[i] = var_s_1[i]/delta_s[i]
    count[i] = i

#sigma:
values_var_s_2 = np.genfromtxt('Spektrallinienwerte/blue_2_var_s.txt', unpack = 'True')

var_s_2 = unp.uarray(np.zeros([sh]),np.zeros([sh])) # beide matrizen gleichgroß
s_quot_2 = unp.uarray(np.zeros([sh]),np.zeros([sh]))

for i in range(0, sh):
    var_s_2[i] = ufloat(values_var_s_2[1,i],10) - ufloat(values_var_s_2[0,i],10)
    s_quot_2[i] = var_s_2[i]/delta_s[i]

#print(delta_s) #für Tabelle
#print(var_s_1) #für Tabelle
#print(var_s_2) #für Tabelle
#print(s_quot_1) #für Tabelle
#print(s_quot_2) #für Tabelle

# Mittelwert:
s_quot_av_1 = np.mean(s_quot_1)
s_quot_av_2 = np.mean(s_quot_2)
print('Mittelwert des Quotienten der Deltas für blau (1):',s_quot_av_1)
print('Mittelwert des Quotienten der Deltas für blau (2):',s_quot_av_2)

# Berechnung vom Lande-Faktor:
lamda_blau = 480e-9 # blaue Wellenlänge in m
n_blau = 1.4635 # blauer Brechungsindex
d = 4e-3 # Dicke der Platte in m

lamda_blau_D = lamda_blau**2/(2*d) * np.sqrt(1/(n_blau**2-1))
print('Dispersionsgebiet für blau:', lamda_blau_D)

c = 299792258 # Lichtgeschwindigkeit in m/s
h = 6.626e-34 # Planck konstante in Js
u_B = 9.274e-24 # Bohr magneton in J/T
B_1 = ufloat(1.07,0.04) # Magnetfeld in T für pi
B_2 = ufloat(0.360,0.024) # Magnetfeld in T für sigma

g_J_1 = c*h/(2*u_B) * lamda_blau_D/lamda_blau**2 * 1/B_1 * s_quot_av_1
g_J_2 = c*h/(2*u_B) * lamda_blau_D/lamda_blau**2 * 1/B_2 * s_quot_av_2

print('Lande-Faktor g_J für blau (1, soll=0.5):', g_J_1)
print('Lande-Faktor g_J für blau (1, soll=1.75):', g_J_2)

# Plot der Differenzen Delta_s und var_s:
#plt.errorbar(count, unp.nominal_values(delta_s), xerr = 0, yerr = unp.std_devs(delta_s), fmt = 'rx', label = r'$\Delta s$')
#plt.errorbar(count, unp.nominal_values(var_s_1), xerr = 0, yerr = unp.std_devs(var_s_1), fmt ='kx', label = r'$\delta s_\pi$')
#plt.errorbar(count, unp.nominal_values(var_s_2), xerr = 0, yerr = unp.std_devs(var_s_2), fmt ='bx', label = r'$\delta s_\sigma$')
#plt.ylim(0,330)
#plt.xlabel(r'$n-n_0$')
#plt.ylabel(r'$d/\text{LE}$')
#plt.legend(loc = 'best')
#plt.grid()
#plt.tight_layout()
#plt.savefig('build/blue_ds.pdf')

# Plot der Quotienten:
count = count -0.01
plt.errorbar(count, unp.nominal_values(s_quot_1), xerr = 0, yerr = unp.std_devs(s_quot_1), fmt = 'bx', label = r'Berechnete Quotienten der $\pi$-Linie')
count = count +0.02
plt.errorbar(count, unp.nominal_values(s_quot_2), xerr = 0, yerr = unp.std_devs(s_quot_2), fmt = 'cx', label = r'Berechnete Quotienten der $\sigma$-Linie')
t = np.linspace(-0.5,10.5,10)
plt.plot(t, 0*t + s_quot_av_1.nominal_value, 'b-', label = r'Mittelwert für die $\pi$-Linie')
plt.plot(t, 0*t + s_quot_av_2.nominal_value, 'c-', label = r'Mittelwert für die $\sigma$-Linie')
plt.xlim(-0.5,10.5)
plt.ylim(0.3,0.7)
plt.xlabel(r'$n-n_0$')
plt.ylabel(r'$\delta s/ \Delta s$')
plt.legend(loc = 'best')
plt.grid()
plt.tight_layout()
plt.savefig('build/blue_quot.pdf')
