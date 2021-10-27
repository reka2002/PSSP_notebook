import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import fsolve

# Parameters:
N = 500 #number of points
time = np.linspace(0, 30, N)

A=20;  #m^2
B=0.1;
C0=0.05;
V0=500;

C_specific = 0.2

#Operating Equation
C = C0*np.exp(B*A/V0/C0*time)
V = V0*np.exp(-B*A/V0/C0*time)

#Plotting
figure=plt.figure()
axes = figure.add_axes([0.1,0.1,0.8,0.8])
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
axes.plot(time,C, marker=' ' , color='r')

plt.title('Solute concentration', fontsize=18);
axes.set_xlabel('time [h]', fontsize=14);
axes.set_ylabel('concentration [kg/m$^3$]',fontsize=14);

figure=plt.figure()
axes = figure.add_axes([0.1,0.1,0.8,0.8])
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
axes.plot(time,V, marker=' ' , color='b')

plt.title('Suspension Volume', fontsize=18);
axes.set_xlabel('time [h]', fontsize=14);
axes.set_ylabel('V [m$^3$]',fontsize=14);


def equation(proc_time):
    eq1 = C0*np.exp(B*A/V0/C0*proc_time) - C_specific
    return eq1

process_time = fsolve(equation,[1])

#To see the figures
plt.show()

print("The process time necessary to obtain a solid residue concentration of", C_specific, "[kg/l] is:", process_time, "[h]")
