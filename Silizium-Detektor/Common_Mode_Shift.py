import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

ADC = np.loadtxt('18_04_30_Graesser_Lammering/Pedestal.txt', delimiter = ';', unpack = 'True')

# Anzahl Kanäle(128)
u = ADC.shape

Pedestal = np.loadtxt('Berechneter_Pedestal.txt', unpack = 'True')

###CMS:

# Für jedes Event der CMS:
Common_Mode_Shift = np.zeros(1000)
for k in range(0,1000):
    for i in range(0,u[1]):
        Common_Mode_Shift[k] += (ADC[k,i] - Pedestal[i])/128

np.savetxt('Berechneter_Common_Mode_Shift.txt', Common_Mode_Shift)

anz = 50
CMS_Hist = np.histogram(Common_Mode_Shift, bins=anz, range=(-10,10))

CMS_Bin = np.zeros(anz+1)
for l in range(0,anz+1):
    CMS_Bin[l] = l*0.4 - 10

#plt.plot(CMS_Bin, CMS_Hist[0], 'k+', markersize = 5)
n,m,o = plt.hist(Common_Mode_Shift, bins = CMS_Bin, normed = True, label = r'Common Mode Shift')
def f(x,sigma):
    return 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-x**2/(2*sigma**2))

m_2 = np.zeros(50)
for i in range(0,50):
    m_2[i] = m[i] + 0.2

popt,pcov = curve_fit(f,m_2,n)

print('Gaußfit(sigma):',popt)

x = np.linspace(-10,10,1000)
plt.plot(x, 1/np.sqrt(2*np.pi*popt**2)*np.exp(-x**2/(2*popt**2)), 'r-', linewidth = 1.0, label = r'Gaußfit')

plt.xlim(-10,10)
plt.legend(loc='best')
plt.xlabel(r'CMS/ADC')
plt.ylabel(r'$p_k$')
plt.grid()
plt.savefig('build/Common_Mode_Shift.pdf')
