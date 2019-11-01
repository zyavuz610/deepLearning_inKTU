########################################################
#   linear resgression (1-variable) with gradient descent
########################################################
import numpy as np
import matplotlib.pyplot as plt

m,c     = 0,0               # y = mx + n
L       = 0.01               # The learning Rate
epochs  = 1000              # The number of iterations to perform gradient descent

x0 = range(10)
y0 = [10,13,12,15,17,17,19,19,21,23]

x = np.array(x0)            # feature vektor
y = np.array(y0)            # response vector

plt.plot(x,y,"ro")

n = float(len(x))           # Number of elements in X
# Performing Gradient Descent 
for i in range(epochs): 
    y_pred = m*x + c                        # The current predicted value of Y
    D_m = (-2/n) * sum(x * (y - y_pred))    # Derivative wrt m
    D_c = (-2/n) * sum(y - y_pred)          # Derivative wrt c
    m = m - L * D_m                         # Update m
    c = c - L * D_c                         # Update c
    #print ("Params: ",m, c)

print ("Params: ",m, c)
x = 7.5
y_pred = m*x + c
plt.plot(x,y_pred,"bx")
'''
ind = 3
print(x[ind],y[ind])
print(x[ind],y_pred[ind])

'''