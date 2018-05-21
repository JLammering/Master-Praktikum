import numpy as np
import matplotlib.pyplot as plt

def linregress(x, y):
    assert len(x) == len(y)

    x, y = np.array(x), np.array(y)

    N = len(y)
    Delta = N * np.sum(x**2) - (np.sum(x))**2

    A = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / Delta
    B = (np.sum(x**2) * np.sum(y) - np.sum(x) * np.sum(x * y)) / Delta

    sigma_y = np.sqrt(np.sum((y - A * x - B)**2) / (N - 2))

    A_error = sigma_y * np.sqrt(N / Delta)
    B_error = sigma_y * np.sqrt(np.sum(x**2) / Delta)

    return A, A_error, B, B_error

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

plateau_90 = channel_91[9:21]
plateau_100 = channel_91[10:21]
plateau_110 =  channel_91[11:21]

plateau_90_av = np.sum(plateau_90)/12
plateau_100_av = np.sum(plateau_100)/11
plateau_110_av = np.sum(plateau_110)/10

m_90, m_err_90, b_90, b_err_90 = linregress(x[9:21],plateau_90)
m_100, m_err_100, b_100, b_err_100 = linregress(x[10:21],plateau_100)
m_110, m_err_110, b_110, b_err_110 = linregress(x[11:21],plateau_110)

print(m_90, m_100, m_110)

t = np.linspace(0,205)
#plt.plot(t, m_90*t + b_90, 'r-', linewidth = 0.6)
#plt.plot(t, m_100*t + b_100, 'g-', linewidth = 0.6)
plt.plot(t, m_110*t + b_110, 'b-', linewidth = 0.8)

plt.plot(x, channel_91, 'ko', markersize=2)
plt.grid()
plt.xlim(0,205)
plt.savefig('build/ccel.pdf')
