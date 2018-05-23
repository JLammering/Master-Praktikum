import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tqdm import tqdm

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


#Daten:
ADC_0   = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/0_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_10  = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/10_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_20  = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/20_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_30  = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/30_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_40  = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/40_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_50  = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/50_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_60  = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/60_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_70  = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/70_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_80  = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/80_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_90  = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/90_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_100 = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/100_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_110 = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/110_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_120 = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/120_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_130 = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/130_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_140 = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/140_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_150 = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/150_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_160 = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/160_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_170 = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/170_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_180 = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/180_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_190 = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/190_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
ADC_200 = pd.read_csv('18_04_30_Graesser_Lammering/CCEQ/200_Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))

ADC_0   = ADC_0.fillna(0).as_matrix()
ADC_10  = ADC_10.fillna(0).as_matrix()
ADC_20  = ADC_20.fillna(0).as_matrix()
ADC_30  = ADC_30.fillna(0).as_matrix()
ADC_40  = ADC_40.fillna(0).as_matrix()
ADC_50  = ADC_50.fillna(0).as_matrix()
ADC_60  = ADC_60.fillna(0).as_matrix()
ADC_70  = ADC_70.fillna(0).as_matrix()
ADC_80  = ADC_80.fillna(0).as_matrix()
ADC_90  = ADC_90.fillna(0).as_matrix()
ADC_100 = ADC_100.fillna(0).as_matrix()
ADC_110 = ADC_110.fillna(0).as_matrix()
ADC_120 = ADC_120.fillna(0).as_matrix()
ADC_130 = ADC_130.fillna(0).as_matrix()
ADC_140 = ADC_140.fillna(0).as_matrix()
ADC_150 = ADC_150.fillna(0).as_matrix()
ADC_160 = ADC_160.fillna(0).as_matrix()
ADC_170 = ADC_170.fillna(0).as_matrix()
ADC_180 = ADC_180.fillna(0).as_matrix()
ADC_190 = ADC_190.fillna(0).as_matrix()
ADC_200 = ADC_200.fillna(0).as_matrix()

# Ab hier Mitteln und Umrechnung in keV:
Coeff = np.genfromtxt('Kalibration_Koeffizienten.txt', unpack = 'True')

def f(x,a,b,c,d,e):
    return a*x**4 + b*x**3 + c*x**2 + d*x + e

# Erzeuge Wertepaararray:
anz_bins = 10001 # insgesamt 10000 bins

adc_bins = np.zeros(anz_bins)
charge_values = np.zeros(anz_bins) # von 0 bis 260 000
for i in range(0,anz_bins): # Das ADC array beinhaltet bins; wenn ein Wert zwischen zwei einträgen liegt, wird er diesem bin zugeordnet
    charge_values[i] = 260000/(anz_bins-1)*(i)
    adc_bins[i] = f(charge_values[i],Coeff[0], Coeff[1], Coeff[2], Coeff[3], Coeff[4])
    charge_values[i] = 260000/(anz_bins-1)*(i+0.5)

def adc_to_charge(adc_b, adc):
    if adc > adc_b[10000]:
        return 0; # nicht schlimm, da hier eh keine Daten erwartet, wegen noise
    else:
        i = 0
        while adc > adc_b[i]:
            i = i+1
        return i-1; # in keV übersetzte Daten

def average_keV(daten, adc_bins):
    #print(daten)
    length = daten.shape[0]
    daten_keV = np.zeros([length,20])
    k = 0
    i = 0
    p = 0
    s = length*20
    with tqdm(total=length) as pbar:
        while k < length:
            while i < 20:
                if daten[k][i] == 0:
                    daten_keV[k][i] = 0
                    p = p+1
                else:
                    daten_keV[k,i] = charge_values[adc_to_charge(adc_bins,daten[k,i])] * 0.0036 # in keV
                i = i+1
            k = k+1
            i = 0
            pbar.update(1)
    daten_av_keV = np.sum(daten_keV, axis = 1)
    print(daten_av_keV)
    return np.sum(daten_av_keV)/len(daten_av_keV)

    keV_av = 0 # Mittelwerte der deponierten Ladung
    anz_daten = 0 # Anzahl in keV übersetzte Werte

    for k in range(0,len(daten_av_keV)):
        if daten_av_keV[k] != 260000/(10000)*0.5/0.0036: # Alle Daten, die übersetzt werden konnten, werden gemittelt
            keV_av += daten_av_keV[k]
            anz_daten += 1

    return keV_av/anz_daten # Gibt den Mittelwert der deponierten Energie zurück

# Mittelwertearray:
keV_av_U = np.zeros(21)

keV_av_U[0 ] = average_keV(ADC_0  , adc_bins)
keV_av_U[1 ] = average_keV(ADC_10 , adc_bins)
keV_av_U[2 ] = average_keV(ADC_20 , adc_bins)
keV_av_U[3 ] = average_keV(ADC_30 , adc_bins)
keV_av_U[4 ] = average_keV(ADC_40 , adc_bins)
keV_av_U[5 ] = average_keV(ADC_50 , adc_bins)
keV_av_U[6 ] = average_keV(ADC_60 , adc_bins)
keV_av_U[7 ] = average_keV(ADC_70 , adc_bins)
keV_av_U[8 ] = average_keV(ADC_80 , adc_bins)
keV_av_U[9 ] = average_keV(ADC_90 , adc_bins)
keV_av_U[10] = average_keV(ADC_100, adc_bins)
keV_av_U[11] = average_keV(ADC_110, adc_bins)
keV_av_U[12] = average_keV(ADC_120, adc_bins)
keV_av_U[13] = average_keV(ADC_130, adc_bins)
keV_av_U[14] = average_keV(ADC_140, adc_bins)
keV_av_U[15] = average_keV(ADC_150, adc_bins)
keV_av_U[16] = average_keV(ADC_160, adc_bins)
keV_av_U[17] = average_keV(ADC_170, adc_bins)
keV_av_U[18] = average_keV(ADC_180, adc_bins)
keV_av_U[19] = average_keV(ADC_190, adc_bins)
keV_av_U[20] = average_keV(ADC_200, adc_bins)

#print(keV_av_U)

# Spannungswertearray:
U = np.zeros(21)

for i in range(0,21):
    U[i] = i*10

plateau_140 = keV_av_U[14:21]
plateau_130 =  keV_av_U[13:21]
plateau_120 = keV_av_U[12:21]

plateau_140_av = np.sum(plateau_140)/7
plateau_130_av = np.sum(plateau_130)/8
plateau_120_av = np.sum(plateau_120)/9


m_140, m_err_140, b_140, b_err_140 = linregress(U[14:21],plateau_140)
m_130, m_err_130, b_130, b_err_130 = linregress(U[13:21],plateau_130)
m_120, m_err_120, b_120, b_err_120 = linregress(U[12:21],plateau_120)

print('Steigung,Abzissenabschnitt(Plateau140):',m_140,'+-',m_err_140,b_140,'+-',b_err_140)
print('Steigung,Abzissenabschnitt(Plateau130):',m_130,'+-',m_err_130,b_130,'+-',b_err_130)
print('Steigung,Abzissenabschnitt(Plateau120):',m_120,'+-',m_err_120,b_120,'+-',b_err_120)

plt.plot(U, keV_av_U, 'k.', markersize = 2, label = r'Messwerte gemittelt')
t = np.linspace(0,205,15)
plt.plot(t, m_120*t + b_120, 'b-', linewidth = 0.8, label = r'Ausgleichsgerade Plateau 120')

plt.xlim(-0.9,205)
plt.grid()
plt.xlabel(r'$U/\si{\volt}$')
plt.ylabel(r'$\text{E}_\text{average}/\si{\kilo\electronvolt}$')
plt.legend(loc = 'best')
plt.savefig('build/cceq.pdf')
