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

plt.plot(Verzögerung, Rate, 'k.', markersize = 2.0)
plt.xlabel(r'$\Delta t/\si{\nano\second}$')
plt.ylabel(r'I/\si{\per\second}')
plt.grid()
plt.savefig('build/justage_koinzidenz.pdf')
