import numpy as np
from uncertainties import ufloat

U = ufloat(3.42, 0.05)
R = ufloat(100, 1)
print("I_s = ", U/R, " A")

U = ufloat(5.33, 0.05)
print("I_f = ", U/R, " A")
