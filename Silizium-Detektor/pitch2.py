import numpy as np
import matplotlib.pyplot as plt

Datenmatrix = np.loadtxt('18_04_30_Graesser_Lammering/Laserscan.txt', unpack = 'True')

#interessante Streifen:
channel_90 = Datenmatrix[89,:]
channel_91 = Datenmatrix[90,:]
channel_92 = Datenmatrix[91,:]
channel_93 = Datenmatrix[92,:]

u = Datenmatrix.shape
x = np.zeros(u[1])

for i in range(0,u[1]):
    x[i] = i*10

# Bestimmung der Minima mit Parabelfits:

# Messwert 8-13 bei channel 91:
channel_91_parab = channel_91[7:13]
x_91_parab = x[7:13]

# Messwert 24-29 bei channel 92
channel_92_parab = channel_92[23:29]
x_92_parab = x[23:29]

def f(x,a,b,c):
    return a*x**2 + b*x + c
#2 a x + b = 0
#x = -b/(2a)

a_91, b_91, c_91 = np.polyfit(x_91_parab,channel_91_parab,2)
a_92, b_92, c_92 = np.polyfit(x_92_parab,channel_92_parab,2)

y = np.linspace(0,350,1000)
plt.plot(y, f(y, a_91, b_91, c_91), 'b-', linewidth = 1.0)
plt.plot(y, f(y, a_92, b_92, c_92), 'r-', linewidth = 1.0)

minima_91 = -b_91/(2*a_91)
minima_92 = -b_92/(2*a_92)
pitch = minima_92 - minima_91

print('erster Streifen, zweiter Streifen, dritter Streifen:', minima_91, minima_92, pitch)

#plt.plot(x, channel_90, 'go', markersize=2)
plt.plot(x[0:7], channel_91[0:7], 'bo', markersize=2.2)
plt.plot(x[7:13], channel_91[7:13], 'b+', markersize=4.5)
plt.plot(x[13:35], channel_91[13:35], 'bo', markersize=2.2)

plt.plot(x[0:23], channel_92[0:23], 'ro', markersize=2.2)
plt.plot(x[23:29], channel_92[23:29], 'r+', markersize=4.5)
plt.plot(x[29:35], channel_92[29:35], 'ro', markersize=2.2)
#plt.plot(x, channel_93, 'co', markersize=2)

plt.ylim(0,180)
plt.grid()
plt.savefig('build/pitch2.pdf')

#Polynomfits mit polyfit (Grad 10):

#def f(x, i,j,k,a,b,c,d,e,f,g,h):
#    return i*x**10 + j*x**9 + k*10**8 + a*x**7 + b*x**6 + c*x**5 + d*x**4 + e*x**3 + f*x**2 + g*x + h

#a_90, b_90, c_90, d_90, e_90, f_90, g_90, h_90 = np.polyfit(x, channel_90, 7)
#a_91, b_91, c_91, d_91, e_91, f_91, g_91, h_91, i_91, j_91, k_91 = np.polyfit(x, channel_91, 10)
#a_92, b_92, c_92, d_92, e_92, f_92, g_92, h_92, i_92, j_92, k_92 = np.polyfit(x, channel_92, 10)
#a_93, b_93, c_93, d_93, e_93, f_93, g_93, h_93 = np.polyfit(x, channel_93, 7)

#y = np.linspace(0,350,1000)
#plt.plot(y, f(y,a_90, b_90, c_90, d_90, e_90, f_90, g_90, h_90),'g-')
#plt.plot(y, f(y,a_91, b_91, c_91, d_91, e_91, f_91, g_91, h_91, i_91, j_91, k_91),'b-')
#plt.plot(y, f(y,a_92, b_92, c_92, d_92, e_92, f_92, g_92, h_92, i_92, j_92, k_92),'r-')
#plt.plot(y, f(y,a_93, b_93, c_93, d_93, e_93, f_93, g_93, h_93),'c-')
