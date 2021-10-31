import numpy as np

tr=np.array([7,10,15]); 
tw=np.array([1,2,1.5]); 
L=10 #cm

N=(16*(tr/tw)**2)

H=L/N

R=np.zeros((np.size(tr),np.size(tr)));

for i in range(0,np.size(tr)):
    for j in range(0,np.size(tr)):
        R[i,j]=abs((tr[i]-tr[j])/(2*(tw[i]+tw[j])))


print('\nHeight of a theoretical plates ',H,' [-]')
print('Number of theoretical plates ',H,' cm')
print('Resolution i,j\n',R)
