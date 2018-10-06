import sys,os,math,random,subprocess
import numpy as np

lipids=["DBPC", "DLPC", "DOPC", "DPPC", "DTPC", "DVPC", "DXPC", "DYPC"]
chol=[5, 10, 15, 20, 25, 30]
asym=[10, 20, 30]

for l in lipids:
	for c in chol:
		for a in asym:
			subprocess.call(["./simulate.txt", l, str(c), str(a)])
			f = open("ener-area-out.xvg")
			ls = f.readlines()
			f.close()


sys.exit(0)
