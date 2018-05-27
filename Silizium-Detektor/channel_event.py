import matplotlib.pyplot as plt
import numpy as np

cluster_event = np.genfromtxt('18_04_30_Graesser_Lammering/cluster_size.txt', unpack = 'True')

channel = np.zeros(128)
for i in range(0,128):
    channel[i] = i

cluster_event = cluster_event/np.sum(cluster_event)

plt.plot(channel[1:21], cluster_event[1:21], 'k.', markersize = 5)
plt.xlim(0,6.5)
plt.xlabel(r'\# Kanäle pro Cluster')
plt.ylabel(r'$h_{\#\text{Kanäle}}$')
plt.grid()
plt.savefig('build/channel_event.pdf')
