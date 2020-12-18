import pandas as pd
import random, sys
from pathlib import Path

# Settings
nsample = 100
nmats = 10

# Filesystem
fin = sys.argv[1]
fout = 'Out/' + fin.split('.')[0]
Path("Out").mkdir(exist_ok=True)

# Running
mat = pd.read_csv(sys.argv[1], sep = "\t")
muestras = mat.shape[1]-1
for i in range(nmats):
	print('Iteracion ' + str(i))
	rlist = random.sample(range(1, muestras), nsample)
	rlist.insert(0,0)
	newmat = mat.iloc[:,rlist]
	# print(newmat)
	fname = fout + '-rand-' + str(i+1) + '.tsv'
	newmat.to_csv(fname,sep = '\t',index = None)



