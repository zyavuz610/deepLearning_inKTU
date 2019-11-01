import numpy as np 
import matplotlib.pyplot as plt 

# th0,th1 = 4,3
X = 2 * np.random.rand(100,1)
y = 14 +3 * X+np.random.randn(100,1)

plt.plot(X,y,'bo')


plt.xlabel("$x$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=18)
_ =plt.axis([0,2,10,35])

X_b = np.c_[np.ones((100,1)),X]  # concationation, X dizisinin başına 1 ekliyor.

theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y) # normal equation

print(theta_best)
y_pred = theta_best[0] + theta_best[1]*X
plt.plot(X,y_pred,'r-')