import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import fsolve

# data:
A=20;
B=0.1;
C0=0.05;
V0=500;
process_time=5;


# The number of elements of this array corresponds to the number of stages.
# The value in each element is the number of modules per stage.
# n=np.array([5, 4, 3, 2]);
n = np.array([17]);

CIN=np.append(C0,np.zeros(np.size(n)-1))
FIN=np.append(V0/process_time, np.zeros(np.size(n)-1));

# Input to the intermediate stages
for i in range(1,np.size(n)):
    CIN[i]=CIN[i-1]+n[i-1]*A*B/FIN[i-1];
    FIN[i]=CIN[i-1]*FIN[i-1]/CIN[i];

# Output concentration
Cout=CIN[np.size(n)-1]+n[np.size(n)-1]*A*B/FIN[np.size(n)-1];

print("The steady state concentration is", Cout, "[kg/l]")
