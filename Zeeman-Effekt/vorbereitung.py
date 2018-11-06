import numpy as np
from scipy import constants
from uncertainties import ufloat


def landeFaktor(J, L, S):
    return (3*J*(J+1) + S*(S+1) - L*(L+1))/(2*J*(J+1))


def energieDiffZeemanNormal(m, B):
    return m*bohrMagneton*B


def energieDiffZeemanAnomal(m, J, L, S, B):
    pass


def dispersionsGebiet(lamda, d, n):
    return lamda**2/(2*d)*(1/(n**2-1))**(1/2)


def aufloesung(L, lamda, n):
    return L/lamda*(n**2-1)


if __name__ == '__main__':
    bohrMagneton = ufloat(constants.physical_constants["Bohr magneton"][0],
                          constants.physical_constants["Bohr magneton"][2])
    L = 120e-3
    d = 4e-3
    #  rote Linie--normaler Effekt
    B_normal = 0
    lamda_rot = 643.8e-9
    n_rot = 1.4567
    print('rot mit L=J=2: g= ', landeFaktor(2, 2, 0))
    print('rot mit L=J=1: g= ', landeFaktor(1, 1, 0))
    print('Delta E(m=-1) = ', energieDiffZeemanNormal(-1, B_normal))
    print('Delta E(m=0) = ', energieDiffZeemanNormal(0, B_normal))
    print('Delta E(m=+1) = ', energieDiffZeemanNormal(+1, B_normal))
    print('dispersionsGebiet= ', dispersionsGebiet(lamda_rot, d, n_rot))
    print('aufloesung= ', aufloesung(L, lamda_rot, n_rot))

    #  blaue Linie--anormaler Effekt
    lamda_blau = 480e-9
    n_blau = 1.4567
    print('blau mit L=0,J=1,S=1: g=', landeFaktor(1, 0, 1))
    print('blau mit L=1,J=1,S=1: g=', landeFaktor(1, 1, 1))

    print('dispersionsGebiet= ', dispersionsGebiet(lamda_blau, d, n_blau))
    print('aufloesung= ', aufloesung(L, lamda_blau, n_blau))
