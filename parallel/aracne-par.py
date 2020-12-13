import pandas as pd
from multiprocessing import Pool
from functools import partial
import os, sys


def f(x, fexp):
#    fexp = "Control-mirnaGen.tsv"
    cmd = "../bin/aracne2 -H ../bin -i " + fexp + " -p 1 -h "
    cmd = cmd + x # concatena el gen
    cmd = cmd + " > salida-" + x + ".log" 
    os.system(cmd)
    print(cmd)

if __name__ == '__main__':
    fname = sys.argv[1]
    fgenlist = sys.argv[2]
    colname = sys.argv[3]
    procs = int(sys.argv[4])

    print("ParAracne using " + str(procs) + " processors")

    df = pd.read_csv(fgenlist, sep='\t')
# colname es el nombre de la primer columna del archivo genlist
# que tiene los genes o los mirna-gen
    genes = df[colname].tolist()

    p = Pool(procs)
    fparam=partial(f, fexp=fname)
    result = p.map(fparam, genes)
    p.close()
    p.join()

    os.mkdir("adj") 
    os.system("mv *.adj adj")
    os.mkdir("log") 
    os.system("mv *.log log")
