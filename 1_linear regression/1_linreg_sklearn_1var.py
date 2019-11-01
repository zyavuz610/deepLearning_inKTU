###############################################
#   linear regression (1-variable)
#   using "sklearn" library models
#       sklearn.linear_model -> LinearRegression
###############################################
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x0 = range(10)
y0 = [10,13,12,15,17,17,19,19,21,23]

x = np.array(x0)            # feature vektor
y = np.array(y0)            # response vector
plt.plot(x,y,"rx")

reg = LinearRegression()    # model

x = x.reshape((x.size,1))   # reshape, data must be in matrix (2D)
y = y.reshape((y.size,1))

reg.fit(x,y)                # learn the parameters

y_pred = reg.predict(x)     # prediction

print("Coefficients: ",reg.coef_)


# regression score -> "y_pred" is ideal, so score must be 1.
print(reg.score(x,y),reg.score(x,y_pred))
plt.plot(x,y_pred,"b-")

ind = 3
print(x[ind],y[ind])
print(x[ind],y_pred[ind])