import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat

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
popt,pcov = np.polyfit(charge_20, ADC_aver, 4, cov = True)
#rint(pcov)

a = popt[0]
b = popt[1]
c = popt[2]
d = popt[3]
e = popt[4]

a_with_err = ufloat(popt[0],np.sqrt(pcov[0,0]))
b_with_err = ufloat(popt[1],np.sqrt(pcov[1,1]))
c_with_err = ufloat(popt[2],np.sqrt(pcov[2,2]))
d_with_err = ufloat(popt[3],np.sqrt(pcov[3,3]))
e_with_err = ufloat(popt[4],np.sqrt(pcov[4,4]))

values_with_err = np.array((a_with_err, b_with_err, c_with_err, d_with_err, e_with_err))

print('Kalibrationskoeffizienten:', values_with_err)
maxwert = 250000 # in charge
print('maximal umrechenbarer Wert(charge,ADC,keV)', maxwert, a*maxwert**4 + b*maxwert**3 + c*maxwert**2 + d*maxwert + e, 0.0036*maxwert)
np.savetxt('Kalibration_Koeffizienten.txt', popt)

x = np.linspace(0,270000,10000)
plt.plot(charge_20, ADC_20, 'bo', markersize = 0.8, label = r'Kalibrationskurve Kanal 20/40/60/80/100')
plt.plot(charge_20, ADC_40, 'bo', markersize = 0.8)
plt.plot(charge_20, ADC_60, 'bo', markersize = 0.8)
plt.plot(charge_20, ADC_80, 'bo', markersize = 0.8)
plt.plot(charge_20, ADC_100, 'bo', markersize = 0.8)
plt.plot(charge_20, ADC_aver, 'ko', markersize = 0.8, label = r'Kalibrationskurve gemittelt')
plt.plot(x, a*x**4 + b*x**3 + c*x**2 + d*x + e, 'r-', linewidth = 0.9, label = r'Ausgleichspolynom')

plt.xlim(0,260000)
plt.ylim(0,275)
plt.legend(loc='best')
plt.xlabel(r'charge/$e$')
plt.ylabel(r'$K$/ADC')
plt.grid()
plt.savefig('build/kalibration.pdf')
