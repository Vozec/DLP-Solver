#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# _authors_: Vozec
# _date_ : 31/10/2022

from utils.logger import found_x
from sympy import ceiling,isprime,sqrt

def run(stop,name,g,h,p,factors):	
	if(not isprime(p)):
		return None

	n 	= int(ceiling(sqrt(p - 1)))
	
	for _ in range(n):
		if(stop.is_cancelled):
			return None
		ref = {pow(g, _, p): _}

	c 	= pow(g, n * (p - 2), p)

	for j in range(n):
		if(stop.is_cancelled):return None

		_ = (pow(c, j, p) * h) % p
		if _ in ref:
			x = ref[_] + n * j
			return found_x(stop,name,x)

	return None

