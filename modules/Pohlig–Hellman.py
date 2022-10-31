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

def modInv(a, m):
	g, x, y = egcd(a, m)
	return x % m
		
def crt(Ni, Mi):
	M = 1
	for m in Mi:
		M *= m
	X = 0	
	for m, n in zip(Mi, Ni):
		temp_mi = M//m
		X += (temp_mi) * n * modInv(temp_mi, m)	
	X %= M	
	return X

def run(stop,name,g,h,p,all_factor):
	x = []

	for factor in all_factor:
		if(stop.is_cancelled):	return None	 

		res = {}
		for _ in range(factor[0]):
			if(stop.is_cancelled):	return None	 
			res[ pow(g, ((p-1)//factor[0])*_, p) ] = _
	   
		c_i,h_ = [],h
		for _ in range(factor[1]):
			if(stop.is_cancelled):	return None	 
			tp = pow( h_, (p-1) // (factor[0] ** (_+1)) , p )						
			c_i.append(res[tp])			
			a = pow(g, (res[tp] * (factor[0] ** (_))), p)
			a = modInv(a, p)
			h_ *= a
			h_ %= p
 
		x.append( sum([ (factor[0] ** _) * c_i[_] for _ in range(factor[1])]) )

	factors = [ x[0] ** x[1] for x in all_factor]
	return found_x(stop,name,crt(x,  factors))