import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

daten = pd.read_csv('18_04_30_Graesser_Lammering/Cluster_adc_entries.txt', skiprows = 1, dtype = float, delimiter = '\t', header=None,names = range(1,21))
daten = daten.fillna(0).as_matrix()

length = daten.shape[0]
daten_av = np.sum(daten, axis = 1)

# print(np.max(daten_av))
# bei etwa 1000 ist noch ein Wert


anz = 500
daten_hist = np.histogram(daten_av, bins = anz, range=(0,500))
plt.hist(daten_av, bins = daten_hist[1], normed = 'True', label = r'ADC Daten')
plt.axvline(x=269.070094488, color = 'r', linewidth = 1, label = r'maximaler Umrechnungswert') # maximaler Wert, der noch umgerechnet werden kann mit dem Kalibrationspolynom

plt.xlim(0,350)
plt.ylim(0,0.017)
plt.xlabel(r'$\text{Signal}_\text{Event}/\si{\text{ADC}}$')
plt.ylabel(r'$P_\text{ADC}$')
plt.grid()
plt.tight_layout()
plt.legend(loc = 'best')
plt.savefig('build/energiespektrum_adc.pdf')
