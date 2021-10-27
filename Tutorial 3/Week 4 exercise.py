import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import fsolve
import math

# data:
A=5; # [m2]
Qin_i=200; # [m3/day]
Cin_i=0.5 #[kg/m3]
Cin_i_plus_one=20 #[kg/m3]
J=3.8*0.1* math.log(145/Cin_i_plus_one) * 24  # convert to days from hours

#  C(in, i+1)= C(in, i) + (n * A * J) / Q(in, i)
n=((Cin_i_plus_one-Cin_i)*Qin_i)/ (J*A)

print("The number of membrane modules necessary for the operation of this process in a single-stage "
      "feed-and-bleed configuration is", n)
