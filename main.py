import sys,os,math,random,subprocess
import numpy as np

lipids=["DOPC", "DPPC", "DTPC"]
chol=[30]
asym=[30, 40]

M = []

for l in lipids:
	for c in chol:
		for a in asym:
			subprocess.call(["./simulate.txt", l, str(c), str(a)])
			f = open("ener-area-out.xvg")
			ls = f.readlines()
			data = []
			data.append(float(ls[3].split("Average +/- sd projected area per lipid: ")[1].split(" ")[0]))
			data.append(float(ls[4].split("Calculate compressibility moduleus: ave ")[1].split(" ")[0]))
			f.close()
			subprocess.call(["rm ener-area-out.xvg"])
			M.append(data)

print(M)
sys.exit(0)
