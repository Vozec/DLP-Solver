#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# _authors_: Vozec
# _date_ : 31/10/2022

from utils.logger import found_x
from sympy import ceiling,isprime,sqrt

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def Xab(x, a, b, G, H, P, Q):   
	sub = x % 3
	if sub == 0:
		return x*G % P,(a+1) % Q,b
	elif sub == 1:
		return x * H % P,a,(b + 1) % Q
	elif sub == 2:
		return x*x % P,a*2 % Q,b*2 % Q
	return x, a, b


def run(stop,name,g,h,p,factors):	
	if(not isprime(p)):
		return None

	q	  = (p - 1) / 2
	x,a,b = g*h,1,1
	X,A,B = x,a,b

	for i in range(1, p):
		if(stop.is_cancelled):return None
		x, a, b = Xab(x, a, b, g, h, p, q)
		X, A, B = Xab(X, A, B, g, h, p, q)
		X, A, B = Xab(X, A, B, g, h, p, q)
		if x == X:break

	x = (egcd(B-b, q)[1] * (a-A)) % q
	if pow(g, int(x), p) == h:
		return found_x(stop,name,int(x))   
	return found_x(stop,name,int(x + q))