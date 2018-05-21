import numpy as np
import matplotlib.pyplot as plt

charge_50_v0, ADC_50_v0 = np.genfromtxt('18_04_30_Graesser_Lammering/Calib/0Vbeikanal50.txt', unpack = 'True')
charge_20, ADC_20 = np.genfromtxt('18_04_30_Graesser_Lammering/Calib/kanal20.txt', unpack = 'True')
charge_40, ADC_40 = np.genfromtxt('18_04_30_Graesser_Lammering/Calib/kanal40.txt', unpack = 'True')
charge_60, ADC_60 = np.genfromtxt('18_04_30_Graesser_Lammering/Calib/kanal60.txt', unpack = 'True')
charge_80, ADC_80 = np.genfromtxt('18_04_30_Graesser_Lammering/Calib/kanal40.txt', unpack = 'True')
charge_100, ADC_100 = np.genfromtxt('18_04_30_Graesser_Lammering/Calib/kanal40.txt', unpack = 'True')

#plt.plot(charge_20, ADC_20, 'kx')
#plt.plot(charge_40, ADC_40, 'kx')
#plt.plot(charge_60, ADC_60, 'kx')
#plt.plot(charge_80, ADC_80, 'kx')
#plt.plot(charge_100, ADC_100, 'kx')

ADC_aver = np.zeros(len(ADC_20))

# Berechnung der Mittelwerte:
for i in range(0,len(ADC_20)):
    ADC_aver[i] = 1/5 * (ADC_20[i] + ADC_40[i] + ADC_60[i] + ADC_80[i] + ADC_100[i])

# Berechnung des Ausgleichspolynoms mittels polyfit:
a,b,c,d,e = np.polyfit(charge_20, ADC_aver, 4)

x = np.linspace(0,270000,10000)
plt.plot(charge_20, ADC_aver, 'ko', markersize = 0.5, label = r'Kalibrationskurven oberhalb von $U_\text{dep}$')
plt.plot(charge_50_v0, ADC_50_v0, 'bo', markersize = 0.5, label = r'Kalibrationskurve bei $U = \SI{0}{\volt}$')

plt.xlim(30000,170000)
plt.ylim(100,270)
#plt.xlim(0,262000)
plt.legend(loc='best')
plt.xlabel(r'charge/$e$')
plt.ylabel(r'$K$/ADC')
plt.grid()
plt.savefig('build/kalibration2.pdf')
