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
    U_diff = ufloat(20, 1)
    U_max = ufloat(43, 1)

    m_oszi = U_max/(U_max - U_diff/2) - 1
    print('Aufgabe c\n')
    print('m aus Oszi_Pic = ', m_oszi)
    # aus Frequenzspektrum
    ampl_links = ufloat(-36.1, 0.1)  # in dBm
    ampl_mitte = ufloat(-20.55, 0.1)
    ampl_rechts = ufloat(-35.88, 0.1)

    P_links = dBmTomW(ampl_links)
    P_rechts = dBmTomW(ampl_rechts)
    P_mitte = dBmTomW(ampl_mitte)

    R = 1
    U_links = unp.sqrt(P_links*R)
    U_rechts = unp.sqrt(P_rechts*R)
    U_mitte = unp.sqrt(P_mitte*R)
    U_lr = (U_links+U_rechts)/2

    print('amplituden=', P_links*1000, P_mitte*1000,
          P_rechts*1000, 'in microW')
    m_freq = (2*U_lr)/U_mitte
    print('m aus Frequenzspektrum = ', m_freq)

    # d
    print('Aufgabe d\n')

    zeitdiff = ufloat(288, 5) * 10**(-9)  # s
    omega_M = ufloat(211.5, 0.4) * 10**3  # Hz
    delta = zeitdiff*omega_M*2*np.pi
    # delta = np.pi/8

    m = delta/(2*(1+np.pi)+unp.cos(delta))
    print('m_oszi aus frequenzmodulierter=', m)
    # print(delta, unp.cos(np.pi))

    # aus Frequenzspektrum
    f_T = ufloat(973, 2)  # kHz
    f_M = ufloat(211.5, 0.4)  # kHz

    ampl_links = ufloat(-22.0, 0.1)  # in dBm
    ampl_mitte = ufloat(-9.9, 0.1)
    ampl_rechts = ufloat(-22.2, 0.1)

    P_links = dBmTomW(ampl_links)
    P_rechts = dBmTomW(ampl_rechts)
    P_mitte = dBmTomW(ampl_mitte)

    R = 1
    U_links = unp.sqrt(P_links*R)
    U_rechts = unp.sqrt(P_rechts*R)
    U_mitte = unp.sqrt(P_mitte*R)
    U_lr = (U_links+U_rechts)/2

    print('amplituden=', P_links*1000, P_mitte*1000,
          P_rechts*1000, 'in microW')

    # U_links = 1/2 m f_T/f_M *U_mitte
    m_freq = (2*U_lr)/U_mitte * (f_M/f_T)
    print('m aus Frequenzspektrum = ', m_freq)
    print('m*f_T/f_M = ', m_freq*f_T/f_M)
