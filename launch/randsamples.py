import pandas as pd
import random

nsample = 100
mat = pd.read_csv("Norm_tumorSC.txt", sep = "\t")
muestras = mat.shape[1]-1
for i in range(10):
	print('Iteracion :' + str(i))
	rlist = random.sample(range(1, muestras), nsample)
	rlist.insert(0,0)
	newmat = mat.iloc[:,rlist]
	print(newmat)
	fname = 'Out/TSC-rand-' + str(i+1) + '.tsv'
	newmat.to_csv(fname,sep = '\t',index = None)



