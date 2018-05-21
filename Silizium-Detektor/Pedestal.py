import numpy as np
import matplotlib.pyplot as plt

ADC = np.loadtxt('18_04_30_Graesser_Lammering/Pedestal.txt', delimiter = ';', unpack = 'True')

# Anzahl Kanäle(128)
u = ADC.shape
#print(u)

###Pedestal:

# Kanalnummerierung
channel = np.zeros(u[1])
for i in range(0,u[1]):
    channel[i] = i+1

Pedestal = np.zeros(u[1])

# Mittelung über alle 1000 Events
for i in range(0,u[1]):
    Pedestal[i] = np.sum(ADC[:,i])/1000

np.savetxt('Berechneter_Pedestal.txt', Pedestal)

Pedestal_aver = np.sum(Pedestal)/u[1]
#Standardabweichung:
Pedestal_sigma = np.sqrt(1/(len(Pedestal)-1)*np.sum((Pedestal-Pedestal_aver)**2))

print('Mittelwert Pedestal:',Pedestal_aver,'+-',Pedestal_sigma)
x = np.linspace(0,130,1000)
plt.plot(x, 0*x + Pedestal_aver,'r-', linewidth = 1.0, label = r'Mittelwert')
plt.plot(channel,Pedestal,'ko', markersize = 2.0, label = r'Pedestal pro Kanal')
plt.xlim(0,130)
plt.ylim(500,525)
plt.xlabel(r'$i$')
plt.ylabel(r'Pedestal/ADC')

plt.grid()
plt.legend(loc = 'best')
plt.savefig('build/Pedestal.pdf')
