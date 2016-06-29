# Matrix Algebra

import numpy

A = [[1,2,3],[2,7,4]]
B = [[1,-1],[0,1]]
C = [[5,-1],[9,1],[6,0]]
D = [[3,-2,-1],[1,2,3]]
u = [[6,2,-3,5]]
v = [[3,5,-1,4]]
w = [[1],[8],[0],[5]]

## 1.1 dimension of A
print "A:",len(A),"x",len(A[0])

## 1.2 dimension of B
print "B:",len(B),"x",len(B[0])

## 1.3 dimension of C
print "C:",len(C),"x",len(C[0])

## 1.4 dimension of D
print "D:",len(D),"x",len(D[0])

## 1.5 dimension of u
print "u:",len(u),"x",len(u[0])

## 1.6 dimension of w
print "w:",len(w),"x",len(w[0])

## 2.1
print map(lambda i: map(lambda x,y:x+y, u[i],v[i]), range(len(u)))

## 2.2
print map(lambda i: map(lambda x,y:x-y, u[i],v[i]), range(len(u)))

## 2.3
alpha = 6
print map(lambda i: map(lambda x:alpha*x, u[i]), range(len(u)))

## 2.4
print map(lambda i: map(lambda x,y:x*y, u[i],v[i]), range(len(u)))

## 2.5
import math
j=0
for i in range(len(u[0])):
    j += u[0][i]**2
print math.sqrt(j)

## 3.1 - not defined

## 3.2 
C_T = zip(*C)
print map(lambda i: map(lambda x,y:x-y, A[i],C_T[i]), range(len(A)))

## 3.3
print map(lambda i: map(lambda x,y:x+3*y, C_T[i],D[i]), range(len(A)))

## 3.4
import numpy as np

mB = np.matrix(B)
mA = np.matrix(A)

print mB*mA

## 3.5 - not defined

## 3.6 - not defined

## 3.7 
mC = np.matrix(C)
print mC*mB

## 3.8
print mB**4

## 3.9
A_T = zip(*A)
mA_T = np.matrix(A_T)
print mA*mA_T

## 3.10
D_T = zip(*D)

mD = np.matrix(D)
mD_T = np.matrix(D_T)
print mD_T*mD