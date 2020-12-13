 1258  Rscript adjToadjmatrix.R Basal-mirnagen.base.adj 
 1261  head -n1 MatTriSup.adj | tr "\t" "\n" | head -n 514 # Check principio de los genes
 1262  head -n1 MatTriSup.adj | tr "\t" "\n" | wc -l # Check total de genes
 1263  cut -f 514-14284  MatTriSup.adj  &> colgenes.out
 1264  head -514 colgenes.out > colgensrowmirnas.out
 1265  head -n1 MatTriSup.adj | tr "\t" "\n" | head -n 513 > mirnaids
 1266  sed -i '1 i\mirnas' mirnaids
 1267  paste -d' ' mirnaids colgensrowmirnas.out > tmp
 1269  head -n1 tmp | tr "\t" "\n" | wc -l
 1274  Rscript adj2list.R 
sort -r -k3,3 Her2-mirnagen.txt > tmp
