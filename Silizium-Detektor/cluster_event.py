import numpy as np
import matplotlib.pyplot as plt

cluster_event = np.genfromtxt('18_04_30_Graesser_Lammering/number_of_clusters.txt', unpack = 'True')

channel = np.zeros(128)
for i in range(0,128):
    channel[i] = i

print(np.sum(cluster_event))
# Normierung:
cluster_event = cluster_event/np.sum(cluster_event)
plt.plot(channel[0:20], cluster_event[0:20], 'k.', markersize = 5)
#plt.legend(loc = 'best')
plt.xlim(-0.5,4.5)
plt.xlabel(r'$i$')
plt.ylabel(r'$h_{\#\text{Cluster}}$')
plt.grid()
plt.savefig('build/cluster_event.pdf')
