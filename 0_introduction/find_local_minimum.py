import numpy as np
import sys
# f(x)=4-(1-(0.5*x+3)^2)
Xleft,Xright = -30,30

x=np.arange(Xleft,Xright,0.1)
ymin = sys.float_info.max
xmin = -30
for xi in x:
    y = 4-(1-(0.5*xi+3)**2)
    if y<ymin:
        xmin,ymin = xi,y

print(format(xmin,".2f"),format(ymin,".2f"))
