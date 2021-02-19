import pandas as pd
from re import match
import numpy as np
import sys, glob
from termcolor import colored, cprint
from pathlib import Path


logprint = lambda x: cprint(x, 'red', attrs=["bold"])
msgprint = lambda x: cprint(x, 'green', attrs=["bold"])



def procs_mi( fin, fout):
	# mat = pd.read_csv("expr-all-ctrl-complete.tsv", sep = "\t")
	mat = pd.read_csv(fin, sep = "\t")
	mat.index = mat.columns
	msgprint("Size of matrix: " + str(mat.shape))
	# mat.isnull().sum().sum()

	genes = list(filter(lambda v: match('^ENS', v), mat.columns))
	ngenes = len(genes) # 16290
	msgprint("Genes without miRNAs: " + str(ngenes))

	if mat.iloc[:ngenes,:].isnull().sum().sum() != 0:
		print("NAs on mirna-gen matrix...")
		sys.exit(15)

	gen_gen = mat.iloc[:ngenes,:ngenes]
	gen_gen.index = gen_gen.columns
	gen_gen = gen_gen.where(np.triu(np.ones(gen_gen.shape),1).astype(np.bool))
	gen_gen = gen_gen.stack().reset_index()
	gen_gen.columns = ['Source','Target','MI']
	gen_gen = gen_gen.sort_values('MI', ascending=False)
	print(gen_gen)
	msgprint("Writing: " + fout + '-gengen.tsv')
	gen_gen.to_csv(fout + '-gengen.tsv', 
		index = False, header=True, sep='\t')
	# gen-gen interactions: 132673905

	gen_mirna = mat.iloc[:ngenes,ngenes:]
	gen_mirna = gen_mirna.stack().reset_index()
	gen_mirna.columns = ['Source','Target','MI']
	gen_mirna = gen_mirna.sort_values('MI', ascending=False)
	print(gen_mirna)
	msgprint("Writing: " + fout + '-genmirna.tsv')
	gen_mirna.to_csv(fout + '-genmirna.tsv', 
		index = False, header=True, sep='\t')
	# gen-miRNA interactions: 

	alldata = pd.concat([gen_gen, gen_mirna])
	alldata = alldata.sort_values('MI', ascending=False)	
	print(alldata)
	msgprint("Writing: " + fout + '-all.tsv')
	alldata.to_csv(fout + '-all.tsv', 
		index = False, header=True, sep='\t')



######################################################################
## MAIN
Path("expr-miRNA").mkdir(parents=True, exist_ok=True)

for file in sorted(glob.glob('*-complete.tsv')):
	logprint("Using file: " + file)

	prefix = '-'.join(file.split('-')[:-1])
	prefix = 'expr-miRNA/' + prefix

	procs_mi(file,prefix)
