# ARACNE-multicore


- ``src/ARACNE.src.tar.gz`` -> Source code of ARACNe2.
- ``parallel`` -> Python middleware scripts  for run ARACNe2 on a platform multicore.
- ``launch`` -> Dirctory to run ARACNe2 multicore.

## Pre-requisites

- python 3
- pandas
- multiprocessing 
- functools
- os, sys

## (Optional) Installing miniconda as bioconda

```bash
bash install-miniconda.sh
```

## 01 - Compiling ARACNe2

```bash
bash compile-aracne.sh
```

## 02 - Running ARACNe2 Multicore

Copy  matrix gene expression into directory ``launch``:

``bash run.sh norm-Stage1.tsv &> salida &``

For run multiple *tsvs*:

``for i in $(ls *.tsv); do bash run.sh $i; done > salida &``


## 03 - Random samples

To get a list of files with n samples randomized.

```
$ cd launch
$ mkdir Out
$ python randsamples.py
```

We considered file input is in folder launch. If you need change this input filename you can modify the code.

On *Out* directory is saved all files that you can copy to launch to run ARACne.