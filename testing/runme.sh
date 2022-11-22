# Batch run
# for i in $(ls *.tsv); do bash run.sh $i; done > salida &

partools="$(pwd)/../parallel"
aracnebin="../bin/aracne2"

[[ ! -f $aracnebin ]] \
	&& echo "No binary: $aracnebin" && exit 15

[[ ! -d $partools ]] \
	&& echo "No parallel tools: ../bin/aracne2" && exit 15

ftsv=$1

[[ $ftsv == "" ]] && echo "need .tsv file" && exit 15

# ftsv="norm-Control.tsv" 
echo "Processing MI calculations for: $ftsv ..."
nom=$(echo $ftsv | cut -d. -f 1)

awk '{print $1}' $ftsv > node.list
cname=$(head -1 node.list)
echo "Column Index Name: $cname"

SECONDS=0
python ${partools}/aracne-par.py $ftsv node.list $cname $(nproc) &> aracne.log 
echo "ARACNe time: $(echo $SECONDS/60 | bc -l) minutes."

rm -rf *adj *log mat.adj node.list 
