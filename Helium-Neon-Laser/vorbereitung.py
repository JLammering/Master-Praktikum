import matplotlib.pyplot as plt
import numpy as np


def plotStabi(r_1, r_2, label):
    L = np.linspace(0, 3, 1000)
    func = L**2*(1/(r_1*r_2))-L*(1/r_1+1/r_2)+1
    # max_length = 0
    for i, value in enumerate(func):
        if value>1 or value < 0:
            print("maximale Länge = ", L[i])
            break

    # ind_value = func.index(threshold)
    # max_length = L[ind_value]
    plt.plot(L, func, label=label)#+" max L = "+str(max_length)+ " m")
    plt.xlabel('L')
    plt.ylabel(r'$g_1 \cdot g_2$')


if __name__ == '__main__':
    # plotStabi(1000e-3, 1000e-3, '2 mit 2')
    # plotStabi(1000e-3, 1400e-3, '2 mit 3')
    plotStabi(1400e-3, 1400e-3, r'$r_1=r_2=\SI{1400}{\milli\meter}$')
    plotStabi(1400e-3, 10000000000, r'$r_1=\SI{1400}{\milli\meter}; r_2=\infty')

    plt.plot([0, 3], [1, 1], label='Grenze', color='k', linestyle='--')
    plt.plot([0, 3], [0, 0], color='k', linestyle='--')

    plt.legend(loc='best')

    plt.savefig('build/stabil.pdf')
