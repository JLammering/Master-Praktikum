import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

ADC_0 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/0CCEL.txt', unpack = 'True')
ADC_10 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/10CCEL.txt', unpack = 'True')
ADC_20 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/20CCEL.txt', unpack = 'True')
ADC_30 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/30CCEL.txt', unpack = 'True')
ADC_40 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/40CCEL.txt', unpack = 'True')
ADC_50 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/50CCEL.txt', unpack = 'True')
ADC_60 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/60CCEL.txt', unpack = 'True')
ADC_70 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/70CCEL.txt', unpack = 'True')
ADC_80 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/80CCEL.txt', unpack = 'True')
ADC_90 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/90CCEL.txt', unpack = 'True')
ADC_100 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/100CCEL.txt', unpack = 'True')
ADC_110 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/110CCEL.txt', unpack = 'True')
ADC_120 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/120CCEL.txt', unpack = 'True')
ADC_130 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/130CCEL.txt', unpack = 'True')
ADC_140 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/140CCEL.txt', unpack = 'True')
ADC_150 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/150CCEL.txt', unpack = 'True')
ADC_160 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/160CCEL.txt', unpack = 'True')
ADC_170 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/170CCEL.txt', unpack = 'True')
ADC_180 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/180CCEL.txt', unpack = 'True')
ADC_190 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/190CCEL.txt', unpack = 'True')
ADC_200 = np.genfromtxt('18_04_30_Graesser_Lammering/CCEL/200CCEL.txt', unpack = 'True')

x = np.zeros(21)

for i in range(0,21):
    x[i] = i*10

channel_91 = np.zeros(21)

channel_91[0] = ADC_0[91]
channel_91[1] = ADC_10[91]
channel_91[3] = ADC_30[91]
channel_91[2] = ADC_20[91]
channel_91[4] = ADC_40[91]
channel_91[5] = ADC_50[91]
channel_91[6] = ADC_60[91]
channel_91[7] = ADC_70[91]
channel_91[8] = ADC_80[91]
channel_91[9] = ADC_90[91]
channel_91[10] = ADC_100[91]
channel_91[11] = ADC_110[91]
channel_91[12] = ADC_120[91]
channel_91[13] = ADC_130[91]
channel_91[14] = ADC_140[91]
channel_91[15] = ADC_150[91]
channel_91[16] = ADC_160[91]
channel_91[17] = ADC_170[91]
channel_91[18] = ADC_180[91]
channel_91[19] = ADC_190[91]
channel_91[20] = ADC_200[91]

# Normierung:
maximum_av = np.sum(channel_91[12:21])/9
channel_91 = channel_91/maximum_av

def CCE(U,a): # a in micrometer
    return (1-np.exp(-300/a * np.sqrt(U/110)))/(1-np.exp(-300/a))

popt, pcov = curve_fit(CCE, x[0:11], channel_91[0:11], bounds=(50,500))

print(popt)

y = np.linspace(0,110,1000)
plt.plot(y, (1-np.exp(-300/popt * np.sqrt(y/110)))/(1-np.exp(-300/popt)), 'r-', linewidth = 1.0)

plt.plot(x, channel_91, 'ko', markersize=2)
plt.grid()
plt.xlim(0,110)
plt.savefig('build/eindringtiefe.pdf')
