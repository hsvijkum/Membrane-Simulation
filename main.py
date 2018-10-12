import sys,os,math,random,subprocess
import numpy as np
import matplotlib

lipids=["DOPC", "DPPC", "DOPE", "DPPE", "DOPS", "DPPS"]
chol=[10, 20, 30, 40]
asym=[10, 20, 30, 40]

for l in lipids:
	for c in chol:
		for a in asym:
			subprocess.call(["./simulate.txt", l, str(c), str(a)])

sys.exit(0)
