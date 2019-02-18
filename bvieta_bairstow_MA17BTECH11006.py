from mpmath import *
from sympy import degree
from sympy import *
from sympy.abc import x
import numpy as np
import cmath




print("Entere the polynomial whose roots you want to find\n")
print("if you want to find roots of a(x^2) + b(x) + c then enter ' a*(x**2) + b*x + c '\n\n")

fun= raw_input("polynomial--> ").strip()	
fun=sympify(fun)

fun=Poly(fun,x)

deg=degree(fun)
co=fun.all_coeffs()

co_r=[]
for i in co:
	co_r.append(i)
co_r.reverse()


def bergie_vieta(p,tol):
	p0=p
	while(np.abs(fun.subs(x,p0))>tol):
		b=co[0]
		c=co[0]
		for i in range(1,deg):
			b=co[i]+ (p0*b)
			c=b + (p0*c)
		b= co[deg] + (p0*b)
		p0=p0-(b/c)
	return p0

	


def bairstow(a,r,s,g,roots,tolerance):
	if(g<1):
		return None
	if((g==1) and (a[1]<>0)):
		roots.append(float(-a[0])/float(a[1]))
		return None
	if(g==2):
		D = (a[1]**2.0)-(4.0)*(a[2])*(a[0])
		X1 = (-a[1] - cmath.sqrt(D))/(2.0*a[2])
		X2 = (-a[1] + cmath.sqrt(D))/(2.0*a[2])
		roots.append(X1)
		roots.append(X2)
		return None
	n = len(a)
	b = [0]*len(a)
	c = [0]*len(a)
	b[n-1] = a[n-1]
	b[n-2] = a[n-2] + r*b[n-1]
	i = n - 3
	while(i>=0):
		b[i] = a[i] + r*b[i+1] + s*b[i+2]
		i = i - 1
	c[n-1] = b[n-1]
	c[n-2] = b[n-2] + r*c[n-1]
	i = n - 3
	while(i>=0):
		c[i] = b[i] + r*c[i+1] + s*c[i+2]
		i = i - 1
	Din = ((c[2]*c[2])-(c[3]*c[1]))**(-1.0)
	r = r + (Din)*((c[2])*(-b[1])+(-c[3])*(-b[0]))
	s = s + (Din)*((-c[1])*(-b[1])+(c[2])*(-b[0]))
	if(abs(b[0])>tolerance or abs(b[1])>tolerance):
		return bairstow(a,r,s,g,roots)
	if (g>=3):
		Dis = ((-r)**(2.0))-((4.0)*(1.0)*(-s))
		X1 = (r - (cmath.sqrt(Dis)))/(2.0)
		X2 = (r + (cmath.sqrt(Dis)))/(2.0)
		roots.append(X1)
		roots.append(X2)
		return bairstow(b[2:],r,s,g-2,roots) 	

k=0
roots=[]


print("for bergie vieta method enter 1 \n for bairstow method enter 2\n\n")
number=int(raw_input("choice--> "))

if  number==1:
	p=float(raw_input("enter the initial guess-->"))
	tole=float(raw_input("enter the tolerance(eg:0.0000001)-->"))
	print("root is " +str(float(bergie_vieta(p,tole))))

if number==2:
	p=raw_input("enter the initial p-->")
	q=raw_input("enter the initial q-->")
	tol=raw_input("enter the tolerance(eg:0.0000001)-->")
	bairstow(co_r,p,q,deg,roots,tol)
	print "\nROOTS ARE: \n"
	for r in roots:
		print "R" + str(k) + " = " + str(r)
		k += 1

