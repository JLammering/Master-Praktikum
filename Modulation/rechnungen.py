import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat


def abweichungen(theorie, gemessen):
    return (np.abs(theorie-gemessen)/theorie)*100


def dBmTomW(wert):
    '''rechnet Werte von dBm in mW um'''
    return (10**(wert/10))

if __name__ == '__main__':
    #  a
    modfreq = ufloat(43.8, 0.5)
    trägfreq = ufloat(970, 1)
    print("abweichungen(trägfreq-modfreq, 929.3)",
          abweichungen(trägfreq-modfreq, 929.3))
    print("abweichungen(trägfreq, 973.1)",
          abweichungen(trägfreq, 973.1))
    print("abweichungen(trägfreq+modfreq, 1016.6)",
          abweichungen(trägfreq+modfreq, 1016.6))

    # c
    # aus Oszi_Pic
    U_diff = ufloat(19.75, 0.02)
    U_Tmax = ufloat(43.25, 0.02)

    U_Tdach = U_Tmax - U_diff/2
    m_oszi = U_Tmax/U_Tdach - 1
    print('Aufgabe c\n')
    print('m aus Oszi_Pic = ', m_oszi)
    # aus Frequenzspektrum
    ampl_links = ufloat(-36.1, 0.02)  # in dBm
    ampl_mitte = ufloat(-20.55, 0.02)
    ampl_rechts = ufloat(-35.88, 0.02)
    # print('Umrechnung von ampl_links=', dBmTomW(ampl_links))
    # print('Umrechnung von ampl_mitte=', dBmTomW(ampl_mitte))
    ampl_links = dBmTomW(ampl_links)
    ampl_rechts = dBmTomW(ampl_rechts)
    ampl_mitte = dBmTomW(ampl_mitte)
    ampl_lr = (ampl_links+ampl_rechts)/2
    print('amplituden=', ampl_links*1000, ampl_rechts*1000, ampl_lr*1000,  ampl_mitte*1000, 'in mW')
    m_freq = (2*ampl_lr)/ampl_mitte
    print('m aus Frequenzspektrum = ', m_freq)
