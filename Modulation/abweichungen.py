import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat


def abweichungen(theorie, gemessen):
    return (np.abs(theorie-gemessen)/theorie)*100


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
