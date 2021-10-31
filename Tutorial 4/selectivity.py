import numpy as np

tr=np.array([7,10,15]); 
t0=1
SEL=np.zeros((np.size(tr),np.size(tr)));

for i in range(0,np.size(tr)):
    for j in range(0,np.size(tr)):
        SEL[i,j]=(tr[i]-t0)/(tr[j]-t0)

print('Selectivity i,j\n',SEL)
