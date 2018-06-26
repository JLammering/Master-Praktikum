import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat

U,I = np.genfromtxt('stromspannungskennlinie.txt', unpack='True')

params, cov = np.polyfit(U,I,4, full= False, cov = True)
#print(cov)

a = params[0]
b = params[1]
c = params[2]
d = params[3]
e = params[4]

a_with_err = ufloat(a,np.sqrt(cov[0,0]))
b_with_err = ufloat(b,np.sqrt(cov[1,1]))
c_with_err = ufloat(c,np.sqrt(cov[2,2]))
d_with_err = ufloat(d,np.sqrt(cov[3,3]))
e_with_err = ufloat(e,np.sqrt(cov[4,4]))

#U_1 = np.zeros(len(U)-1)
#I_1 = np.zeros(len(U)-1)
#
#for i in range(0,len(U_1)):
#    I_1[i] = (I[i+1]-I[i])/(U[i+1]-U[i])
#    U_1[i] = (U[i+1]+U[i])/2
#
#U_2 = np.zeros(len(U_1)-1)
#I_2 = np.zeros(len(U_1)-1)
#
#for i in range(0,len(U_2)):
#    I_2[i] = (I_1[i+1]-I_1[i])/(U_1[i+1]-U_1[i])
#    U_2[i] = (U_1[i+1]+U_1[i])/2
#
#plt.plot(U_2,I_2,'rx')

x = np.linspace(0,205,1000)
plt.plot(U,I,'k.', markersize = 2, label = r'Messwerte')
plt.plot(x, a*x**4 + b*x**3 + c*x**2 + d*x + e, 'r-', linewidth = 1, label = r'Ausgleichspolynom')

print('Fit-Parameter:', a_with_err, b_with_err, c_with_err, d_with_err, e_with_err)
print('Knick im Ausgleichspolynom (stärkste Veränderung der Steigung):',-b_with_err/(4*a_with_err))

plt.xlim(0,205)
plt.legend(loc = 'best')
plt.xlabel(r'$U/\si{\volt}$')
plt.ylabel(r'$I/\si{\micro\ampere}$')
plt.grid()
plt.savefig('build/stromspannungskennlinie.pdf')
