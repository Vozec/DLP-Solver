#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# _authors_: Vozec
# _date_ : 31/10/2022

from utils.logger import found_x
from sympy.ntheory.residue_ntheory import discrete_log


def run(stop,name,g,h,p,all_factor):
	try:
		return found_x(stop,name,discrete_log(p, h, g))
	except Exception as ex:
		stop.cancel()