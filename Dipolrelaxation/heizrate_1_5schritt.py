import numpy as np
import matplotlib.pyplot as plt

T, I = np.genfromtxt('messung_2schritt.txt', unpack = 'True')

t = np.zeros(len(T))

for i in range(0,len(T)):
    t[i] = i+1

plt.plot(t,T,'k.')

plt.grid()
plt.savefig('build/heizrate_1_5schritt.pdf')
