import pandas as pd
import os, sys

name = sys.argv[1]
n = sys.argv[2]
nodelist = sys.argv[3]
nodename = sys.argv[4]

df = pd.read_csv(nodelist, sep='\t')
genes = df[nodename].tolist()

os.chdir("adj")
wlines = []
for i in genes:
  fname = name + '_h_' + i + '_k0.' + n + '.adj'
  fh = open(fname, "r")
  lines = fh.read().splitlines()
  last_line = lines[-1]
  wlines.append(last_line)
  fh.close()

with open('mat.adj', 'w') as f:
    for l in wlines:
        f.write("%s\n" % l)

