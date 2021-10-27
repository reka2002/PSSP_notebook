import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import fsolve

# data:
A=20;
B=0.1;
C0=0.05;
V0=500;
process_time=5;

Cout=C0+A*B*process_time/V0


print("The steady state concentration is", Cout, "[kg/l]")
