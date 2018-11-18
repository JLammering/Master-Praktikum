import numpy as np
from scipy import constants
from uncertainties import ufloat


def landeFaktor(J, L, S):
    return (3*J*(J+1) + S*(S+1) - L*(L+1))/(2*J*(J+1))


def energieDiffZeeman(deltamg, B):
    return deltamg*bohrMagneton*B


def BfeldOpti(lamda, deltamg, disper):
    return (c*h)/(4*lamda**2*deltamg*bohrMagneton)*disper


def dispersionsGebiet(lamda, d, n):
    return lamda**2/(2*d)*(1/(n**2-1))**(1/2)


def aufloesung(L, lamda, n):
    return L/lamda*(n**2-1)


if __name__ == '__main__':
    bohrMagneton = ufloat(constants.physical_constants["Bohr magneton"][0],
                          constants.physical_constants["Bohr magneton"][2])
    c = constants.physical_constants["speed of light in vacuum"][0]
    h = ufloat(constants.physical_constants["Planck constant"][0],
               constants.physical_constants["Planck constant"][2])
    L = 120e-3
    d = 4e-3
    #  rote Linie--normaler Effekt
    lamda_rot = 643.8e-9
    n_rot = 1.4567
    print("rot: ")
    print('rot mit L=J=2: g= ', landeFaktor(2, 2, 0))
    print('rot mit L=J=1: g= ', landeFaktor(1, 1, 0))
    disper_rot = dispersionsGebiet(lamda_rot, d, n_rot)
    print('dispersionsGebiet= ', dispersionsGebiet(lamda_rot, d, n_rot))

    B_normal = BfeldOpti(lamda_rot, 1, disper_rot)
    print('B_normal = ', B_normal)
    print('Delta E(m=-1) = ', energieDiffZeeman(-1, B_normal)/(1.602e-19), "eV")
    print('Delta E(m=0) = ', energieDiffZeeman(0, B_normal)/(1.602e-19), "eV")
    print('Delta E(m=+1) = ', energieDiffZeeman(+1, B_normal)/(1.602e-19), "eV")
    print('aufloesung= ', aufloesung(L, lamda_rot, n_rot), "\n\n")

    #  blaue Linie--anormaler Effekt
    print("blau: ")
    lamda_blau = 480e-9
    n_blau = 1.4567
    print('blau mit L=0,J=1,S=1: g=', landeFaktor(1, 0, 1))
    print('blau mit L=1,J=1,S=1: g=', landeFaktor(1, 1, 1))
    disper_blau = dispersionsGebiet(lamda_blau, d, n_blau)
    print('dispersionsGebiet= ', dispersionsGebiet(lamda_blau, d, n_blau))

    B_anomalpi = BfeldOpti(lamda_blau, 0.5, disper_blau)
    B_anomalsigma = BfeldOpti(lamda_blau, 1.75, disper_blau)

    print('B_anomalpi = ', B_anomalpi)
    print('B_anomalsigma = ', B_anomalsigma)

    print('Delta E(mg=-2) = ', energieDiffZeeman(-2, B_anomalsigma)/(1.602e-19), "eV")
    print('Delta E(mg=-1.5) = ', energieDiffZeeman(-1.5, B_anomalsigma)/(1.602e-19), "eV")
    print('Delta E(mg=-0.5) = ', energieDiffZeeman(-0.5, B_anomalpi)/(1.602e-19), "eV")
    print('Delta E(m=0) = ', energieDiffZeeman(0, B_normal)/(1.602e-19), "eV")
    print('Delta E(m=+0.5) = ', energieDiffZeeman(+0.5, B_anomalpi)/(1.602e-19), "eV")
    print('Delta E(mg=+1.5) = ', energieDiffZeeman(+1.5, B_anomalsigma)/(1.602e-19), "eV")
    print('Delta E(mg=+2) = ', energieDiffZeeman(+2, B_anomalsigma)/(1.602e-19), "eV")

    print('dispersionsGebiet= ', dispersionsGebiet(lamda_blau, d, n_blau))
    print('aufloesung= ', aufloesung(L, lamda_blau, n_blau))
