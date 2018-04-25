import numpy as np
from uncertainties import ufloat


def werteZuTabelle(*werteArray, rundungen):
    ''' Funktion um Werte in Tabelle auszugeben'''

    if len(werteArray) != len(rundungen):  # Fehleruntersuchung
        print('Dimension werteArray= ', len(werteArray), ' != ',
              'Dimension rundungen= ', len(rundungen))
        return

    for i in range(len(werteArray[0])):  # geht durch die Zeilen
        for k in range(len(werteArray)):  # geht durch die Spalten
            if k == len(werteArray)-1:  # am Ende Backslashes
                print(round(werteArray[k][i], rundungen[k]), end='\\\\\n')
            else:  # vorher mit Undzeichen
                print(round(werteArray[k][i], rundungen[k]), end=' & ')


def abweichungen(theorie, gemessen):
    '''Funktion um Abweichungen zwischen berechnetem und erwarteten Wert
       anzugeben'''
    return (np.abs(theorie-gemessen)/theorie)*100


def mittelwert(sigma):
    '''calculate mean of values with errors'''
    laenge = len(sigma)
    sum = ufloat(0, 0)
    for i in range(0, laenge):
        sum += sigma[i]
    return (1/laenge)*sum
