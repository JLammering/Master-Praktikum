import matplotlib.pyplot as plt
import numpy as np

U,I = np.genfromtxt('stromspannungskennlinie.txt', unpack='True')

a, b, c, d, e = np.polyfit(U,I,4)

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

x = np.linspace(0,200,1000)
plt.plot(U,I,'kx')
plt.plot(x, a*x**4 + b*x**3 + c*x**2 + d*x + e, 'r-')

print(-b/(4*a))

plt.savefig('build/stromspannungskennlinie.pdf')
