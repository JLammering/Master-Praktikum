import numpy as np
from uncertainties import ufloat
from functions import abweichungen

if __name__ == '__main__':
    # schalter
    R_1 = ufloat(1.00e3, 0.05e3)  #kohm
    R_p = ufloat(99.7e3, 0.5e3)  #kohm
    U_B = ufloat(14.13, 0.05)  #volt
    U_A = ufloat(26.3, 0.5)  #volt

    umkipp_1 = ufloat(151.25e-3, 5e-3)  #mV
    umkipp_2 = ufloat(167.75e-3, 5e-3)  #mV
    print(umkipp_1, U_B*R_1/R_p, 'Abweichung = ', abweichungen(U_B*R_1/R_p, umkipp_1))
    print(umkipp_2, U_B*R_1/R_p, 'Abweichung = ', abweichungen(U_B*R_1/R_p, umkipp_2))
    print('U_A', U_A, abweichungen(2*U_B, U_A))

    #signalgen
    R_1 = ufloat(1.002e3, 0.05e3)  #kohm
    R_p = ufloat(99.7e3, 0.5e3)  #kohm
    R = ufloat(100e3, 0.5e3)  #kohm
    C = ufloat(970e-9, 10e-9)
    U_B = ufloat(14.125, 0.05)  #volt
    U_A_recht = ufloat(26.3, 0.5)  #volt
    U_A_drei = ufloat(345e-3, 5e-3)
    nu = ufloat(216, 1)
    U_A_drei_theo = 2*R_1/R_p *U_B
    U_A_recht_theo = 2*U_B
    omega_drei_theo = (np.pi*R_p)/(R*C*R_1)
    print('U_A_drei', U_A_drei, U_A_drei_theo, abweichungen(U_A_drei_theo, U_A_drei))
    print('U_A_recht', U_A_recht, U_A_recht_theo, abweichungen(U_A_recht_theo, U_A_recht))
    print('omega_drei', 2*np.pi*nu, omega_drei_theo, abweichungen(omega_drei_theo, 2*np.pi*nu))

    #entdämpft
    R = ufloat(9.96e3, 0.05e3)  #kOhm
    C = ufloat(np.mean([20.65e-9, 22.8e-9]), np.std([20.65e-9, 22.8e-9]))
    nu_mess = ufloat(674, 5)  #hertz
    nu_erw = 1/(2*np.pi*R*C)
    print('C ', C)
    print('freq: ', nu_mess, nu_erw, abweichungen(nu_erw, nu_mess))
