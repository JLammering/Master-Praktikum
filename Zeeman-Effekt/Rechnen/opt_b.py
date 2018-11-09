import numpy as np
from scipy import constants

c = 299792458 # in meter per second
h = 6.626e-34 # in Joule per second
mu = constants.physical_constants["Bohr magneton"][0]

lambda_rot = 643.8e-9
lambda_blau = 480e-9
D_lambda_rot = 0.04891e-9
D_lambda_blau = 0.02695e-9

g_J_1 = 1
g_J_2 = 1.75

B_rot = c*h/(4 * g_J_1 * lambda_rot**2 * mu) * D_lambda_rot
B_blau = c*h/(4 * g_J_2 * lambda_blau**2 * mu) * D_lambda_blau

print('B_rot:',B_rot)
print('B_blau:',B_blau)
