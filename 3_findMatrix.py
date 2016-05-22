import numpy as np
import os
import cv2 as cv
import math;


X = np.array([[0, 50, 0, 50, 0, 50,  100, 100], [0, 0, 50,0,100,50,50,100], [100,100,50,50,50,0,0,0], [1,1,1,1,1,1,1,1]])     
x = np.array([[229, 297, 159, 288, 79, 222, 283, 212],[155, 188, 259, 268, 295, 370, 425, 480] , [1,1,1,1,1,1,1,1]])   



def calibrate(x, X):
    n = x.shape[1]
    A = np.zeros([2*n,12])
    for i, ind in enumerate(range(1, 16, 2),):
        ind -=1
        A[ind,:] = np.hstack([X[:3,i].T, 1,0,0,0,0, -x[0, i].T*X[:3,i], -x[0,i]])
        A[ind+1,:] = np.hstack([0,0,0,0,X[:3,i].T, 1,-x[1, i].T*X[:3,i], -x[1,i]])
    U, S, V = np.linalg.svd(A)
    V = np.linalg.inv(V)
    M = V[:,11].reshape([3,4])/V[11,11]
    #print M
    return M
        

M = calibrate(x, X)
M1 = np.linalg.pinv(M);
p =[[514],[143],[1]];
t = M1.dot(p);
xc =' cm';
xcord = str(math.fabs(t[0]*0.1));
print('X in World Frame:  '+xcord+xc);
xcord = str(math.fabs(t[1]*0.1));
print('Y in World Frame:  '+xcord+xc);
xcord = str(math.fabs(t[2]*0.1));
print('Z in World Frame:  '+xcord+xc);

