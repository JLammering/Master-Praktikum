import numpy as np
import matplotlib.pyplot as plt

T,I = np.genfromtxt('messung_2schritt', unpack = 'True')

plt.plot(T,I,'k.')

plt.grid()
plt.xlabel(r'$T/\si{\celsius}$')
plt.ylabel(r'$I/\si{\pico\ampere}$')

plt.savefig('build/stromtemp_1_5.pdf')
