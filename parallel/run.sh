# Generar el gene list con la primer columna del tsv
# awk '{print $1}' Basal-mirnaGen.tsv > gene.list
# modificar el nombre de la coluna en el script aracne-par.py
python aracne-par.py norm-Control.tsv gene.list gene &> salida.log &
python joinadj.py
mv adj/mat.adj .
python adj2sif.py > mat.sif
sort -r -k3,3 mat.sif | head -10000 > Control-IM-1e5.txt
