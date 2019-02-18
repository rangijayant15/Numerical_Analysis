
# coding: utf-8

# In[ ]:


from sympy import *
from mpmath import *
import numpy as np
x=symbols("x")
function = raw_input().strip()
function=function.sympify()
def secant(l,r,tolerance):
    x1=l
    x2=r
    if function.subs(x,x1)*function.subs(x,x2)==0:
        if(function.subs(x,x1)==0):
            print(x1)
        else:
            print(x2)
    else:
        slope=(function.subs(x,x1)-function.subs(x,x2))/(x1-x2)
        x3=x1-(function.subs(x,x1)/slope)
        while (np.abs(function.subs(x,x3))>=tolerance):
            x1=x2
            x2=x3
            slope=(function.subs(x,x1)-function.subs(x,x2))/(x1-x2)
            x3=x1-(function.subs(x,x1)/slope)
            
        print(float(x3))       
    
        
secant(-400,10,0.00000000001)

