import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from tqdm import tqdm

daten = pd.read_csv('18_04_30_Graesser_Lammering/Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
daten = daten.fillna(0).as_matrix()

length = daten.shape[0]
daten_av = np.sum(daten, axis = 1)

# Ab hier Umrechnung in keV:
Coeff = np.genfromtxt('Kalibration_Koeffizienten.txt', unpack = 'True')

def f(x,a,b,c,d,e):
    return a*x**4 + b*x**3 + c*x**2 + d*x + e

# Erzeuge Wertepaararray:

anz_bins = 10001

adc_bins = np.zeros(anz_bins)
charge_values = np.zeros(anz_bins) # von 0 bis 260 000
for i in range(0,anz_bins): # Das ADC array beinhaltet bins, wenn ein Wert zwischen zwei einträgen liegt, wird er diesem bin zugeordnet
    charge_values[i] = 260000/(anz_bins-1)*(i)
    adc_bins[i] = f(charge_values[i],Coeff[0], Coeff[1], Coeff[2], Coeff[3], Coeff[4])
    charge_values[i] = 260000/(anz_bins-1)*(i+0.5)

print(charge_values)
print(adc_bins)
print(daten_av)
def adc_to_charge(adc_b, adc, a_bins):
    if adc > adc_b[a_bins-1]:
        return 0; # nicht schlimm, da hier eh keine Daten erwartet, wegen noise
    else:
        i = 0
        while adc > adc_b[i]:
            i = i+1
        return i-1; # in keV übersetzte Daten

daten_av_keV = np.zeros(length)

k = 0
with tqdm(total=length) as pbar:
    while k < length:
        daten_av_keV[k] = charge_values[adc_to_charge(adc_bins,daten_av[k],anz_bins)] * 0.0036 # in keV
        k = k+1
        pbar.update(1)

keV_av = 0 # Mittelwert:
anz_daten = 0 # Anzahl in keV übersetzte Werte

for k in range(0,len(daten_av_keV)):
    if daten_av_keV[k] != 260000/(anz_bins-1)*0.5/0.0036: # Alle Daten, die übersetzt werden konnten, werden gemittelt
        keV_av += daten_av_keV[k]
        anz_daten += 1

keV_av = keV_av/anz_daten

print('Mittelwert deponierte Energie:', keV_av)

anz = 400
daten_hist = np.histogram(daten_av_keV, bins = anz, range=(1,1000))
n,m,o = plt.hist(daten_av_keV, bins = daten_hist[1], normed = 'True')

# Bestimmung des MPV's: Fitfunktion: Gauß plus x
def peak_fit(x,C,mu,sigma,a):
    return C*np.exp(-(x-mu)**2/(2*sigma**2)) + a*(x-mu)

popt,pcov = curve_fit(peak_fit, daten_hist[1][15:40], n[15:40], bounds = ([0,70,10,0],[1,100,1000,3]))

x = np.linspace(0,200,500)
plt.plot(x, popt[0]*np.exp(-(x-popt[1])**2/(2*popt[2]**2)) + popt[3]*x, 'r-',)

plt.xlim(0,600)
plt.savefig('build/energiespektrum_keV.pdf')
