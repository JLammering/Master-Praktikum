import numpy as np
import matplotlib.pyplot as plt

ADC = np.loadtxt('18_04_30_Graesser_Lammering/Pedestal.txt', delimiter = ';', unpack = 'True')
Pedestal = np.loadtxt('Berechneter_Pedestal.txt', unpack = 'True')
Common_Mode_Shift = np.loadtxt('Berechneter_Common_Mode_Shift.txt', unpack = 'True')
u = ADC.shape # Anzahl Kanäle

###Noise:

Noise = np.zeros(u[1])

for i in range(0,u[1]):
    summe = 0
    for k in range(0,1000):
        summe += (ADC[k,i] - Pedestal[i] - Common_Mode_Shift[k])**2
    Noise[i] = np.sqrt(1/999 * summe)

# Kanalnummerierung
channel = np.zeros(u[1])
for i in range(0,u[1]):
    channel[i] = i+1

# Average Noise
Noise_aver = np.sum(Noise)/128
#Standardabweichung:
Noise_sigma = np.sqrt(1/(len(Noise)-1)*np.sum((Noise-Noise_aver)**2))
print('Mittelwert Noise:', Noise_aver, '+-', Noise_sigma)

x = np.linspace(0,129,100)
plt.plot(x, 0*x + Noise_aver, 'b-', linewidth = 1.0, label = r'Mittelwert')
plt.plot(channel, Noise, 'ko', markersize = 2.0, label = r'Noise pro Kanal')
plt.ylim(1.2,3.2)
plt.xlim(0,129)

plt.legend(loc='best')
plt.xlabel(r'$i$')
plt.ylabel(r'Noise/ADC')
plt.grid()
plt.savefig('build/Noise.pdf')
