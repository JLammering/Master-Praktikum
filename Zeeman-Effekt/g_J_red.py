import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat

values_delta_s = np.genfromtxt('Spektrallinienwerte/red_delta_s.txt', unpack = 'True')
values_var_s = np.genfromtxt('Spektrallinienwerte/red_var_s.txt', unpack = 'True')

sh = np.shape(values_delta_s)[1]

delta_s = unp.uarray(np.zeros([sh]),np.zeros([sh]))
var_s = unp.uarray(np.zeros([sh]),np.zeros([sh])) # beide matrizen gleichgroß
s_quot = unp.uarray(np.zeros([sh]),np.zeros([sh]))
count = np.zeros([sh])

for i in range(0, sh):
    delta_s[i] = ufloat(values_delta_s[1,i],10) - ufloat(values_delta_s[0,i],10)
    var_s[i] = ufloat(values_var_s[1,i],10) - ufloat(values_var_s[0,i],10)
    s_quot[i] = var_s[i]/delta_s[i]
    count[i] = i

#print(delta_s) #für Tabelle
#print(var_s) #für Tabelle
#print(s_quot) #für Tabelle

# Mittelwert:
s_quot_av = np.mean(s_quot)
print('Mittelwert des Quotienten der Deltas für rot:',s_quot_av)

# Berechnung vom Lande-Faktor:
lamda_rot = 643.8e-9 # rote Wellenlänge in m
n_rot = 1.4567 # roter Brechungsindex
d = 4e-3 # Dicke der Platte in m

lamda_rot_D = lamda_rot**2/(2*d) * np.sqrt(1/(n_rot**2-1))
print('Dispersionsgebiet für rot:', lamda_rot_D)

c = 299792258 # Lichtgeschwindigkeit in m/s
h = 6.626e-34 # Planck konstante in Js
u_B = 9.274e-24 # Bohr magneton in J/T
B = ufloat(0.634,0.028) # Magnetfeld in T

g_J = c*h/(2*u_B) * lamda_rot_D/lamda_rot**2 * 1/B * s_quot_av

print('Lande-Faktor g_J für rot (soll=1):', g_J)

# Plot der Differenzen Delta_s und var_s:
#plt.errorbar(count, unp.nominal_values(delta_s), xerr = 0, yerr = unp.std_devs(delta_s), fmt = 'rx', label = r'$\Delta s$')
#plt.errorbar(count, unp.nominal_values(var_s), xerr = 0, yerr = unp.std_devs(var_s), fmt ='kx', label = r'$\delta s$')
#plt.ylim(0,330)
#plt.xlabel(r'$n-n_0$')
#plt.ylabel(r'$d/\text{LE}$')
#plt.legend(loc = 'best')
#plt.grid()
#plt.tight_layout()
#plt.savefig('build/red_ds.pdf')

# Plot der Quotienten:
plt.errorbar(count, unp.nominal_values(s_quot), xerr = 0, yerr = unp.std_devs(s_quot), fmt = 'rx', label = r'Berechnete Quotienten')
t = np.linspace(-0.5,11.5,10)
plt.plot(t, 0*t + s_quot_av.nominal_value, 'r-', label = r'Mittelwert')
plt.xlim(-0.5,11.5)
plt.ylim(0.3,0.7)
plt.xlabel(r'$n-n_0$')
plt.ylabel(r'$\delta s/ \Delta s$')
plt.legend(loc = 'best')
plt.grid()
plt.tight_layout()
plt.savefig('build/red_quot.pdf')
