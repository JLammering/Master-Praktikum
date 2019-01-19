import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

W = 1.7 * 10**(-19) # Aktivierungsenergie
tau_0 = 1 * 10**(-18) # char. Relax.
k_B = 1.38065*10**(-23) # Boltzmannkonstante

x = np.linspace(-35,10,500)
plt.plot(x, tau_0*np.exp(W/(k_B*(x+273.15))), 'b-', label=r'Relaxationszeit $\tau(T)$', linewidth = 1.3)

plt.xlim(-35,10)
plt.ylim(-100,30000)
plt.xlabel(r'$T/ \si{\celsius}$')
plt.ylabel(r'$\tau/ \si{\second}$')
plt.legend(loc = 'best')
plt.grid()
plt.tight_layout()
plt.savefig('build/relax.pdf')
