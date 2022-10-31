#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# _authors_: Vozec
# _date_ : 31/10/2022

import os,re,sys,argparse,math
from factordb.factordb import FactorDB


from utils.logger import *

def header():
	logger(r"""
    ____  __    ____     _____       __               
   / __ \/ /   / __ \   / ___/____  / /   _____  _____
  / / / / /   / /_/ /   \__ \/ __ \/ / | / / _ \/ ___/
 / /_/ / /___/ ____/   ___/ / /_/ / /| |/ /  __/ /    
/_____/_____/_/       /____/\____/_/ |___/\___/_/
""",'log',0,0)

def parse_args():
	parser = argparse.ArgumentParser(add_help=False, description='This tool automates the resolution of the discrete logarithm problem: h=(g^x)\%p')
	parser.add_argument("-g",dest="g",type=int,required=True, help="g")
	parser.add_argument("-h",dest="h",type=int,required=True, help="h")
	parser.add_argument("-p",dest="p",type=int,required=True, help="p")
	return parser.parse_args()

def Load_modules(path, env):
	def get_module_names_in_dir(path):
		result = set()
		for entry in os.listdir(path):
			if os.path.isfile(os.path.join(path, entry)):
				regexp_result = re.search("(.+)\.py(c?)$", entry)
				if regexp_result: # is a module file name
					result.add(regexp_result.groups()[0])
		return result
	sys.path.append(path)
	modules = {}
	for module_name in sorted(get_module_names_in_dir(path)):
		env[module_name] = __import__(module_name)
		modules[module_name]=env[module_name]
	return modules

def Format_Factors(factors):
	fct = {}
	for f in factors:
		if f not in fct.keys():
			fct[f]  = 1
		else:
			fct[f] += 1
	return list(fct.items())

def Get_all_factors(m):
	f = FactorDB(m)
	f.connect()

	factors = f.get_factor_list()
	if math.prod(factors) == m:
		return Format_Factors(factors)

	factors = []
	for x,y in f.get_factor_from_api():
		for _ in range(y):
			factors.append(int(x))
	if math.prod(factors) == m:
		return Format_Factors(factors)

	return [m,1]