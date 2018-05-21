import matplotlib.pyplot as plt
import numpy as np

Hits_per_channel = np.genfromtxt('18_04_30_Graesser_Lammering/hitmap.txt', unpack = 'True')

x = np.zeros(128)

for i in range(0,128):
    x[i] = i+1

plt.plot(x,Hits_per_channel,'kx',markersize=2)
#, bins = x)
# range=(x.min(),x.max()))

plt.savefig('build/hitmap.pdf')
