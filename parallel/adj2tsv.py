# Convierte una matriz de adyacencia de ARACNe 
# en una matriz completa en formato tsv
import sys, os
import pandas as pd
from pathlib import Path


fout = Path(sys.argv[1]).stem + '-complete.tsv'

lines = [line.rstrip('\n') for line in open(sys.argv[1])]

rows = []
gnames = []
c = 0
for l in lines:
  vals = l.split()
  name = vals[0]
  row = []
  for i in range(2, len(vals), 2):
    row.append(vals[i])
  row.insert(c,0)
  rows.append(row)
  gnames.append(name)
  c=c+1
gnames = [x.upper() for x in gnames]
df = pd.DataFrame(rows, columns = gnames)  
df.to_csv(fout, sep='\t', index=False)
