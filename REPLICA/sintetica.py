#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import csv

outp1="sin.txt"

def sintetica(outp):
	f_outp = open(outp, "w")
	sin = []
	for i in  range(300):
		s = np.random.choice(5)
		for j in range(4):
			a = np.random.rand(3000)
			b = np.random.choice(100,3000)
			v = [i,s,(a+b).tolist()]
			#print v
			sin.append(v)
	#print sin
	for item in sin:
		f_outp.write("%s\n" % item)
	#np.savetxt('test.txt', sin, fmt="%d") 

sintetica(outp1)