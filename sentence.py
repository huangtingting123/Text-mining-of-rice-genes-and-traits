import re
import sys
gene=open("gene_sym.txt",'r')
trait=open("rice_trait.txt",'r')
abstract=open(sys.argv[1],'r')
gene_array=[]
trait_array=[]
abstract_dic=dict()
out_dic=dict()
for line in gene:
    line_1=line.strip('\n')
    symbol=line_1.split('\t')[1]
    gene_array.append(symbol)
for line1 in trait:
    line1_1=line1.strip('\n')
    trait_array.append(line1_1)
for line2 in abstract:
    line2_1=line2.strip('\n')
    lis=line2_1.split('\t')
    if len(lis)==2:
        abstract_dic[lis[0]]=lis[1]
        abst=lis[1].split('. ')
        for i in abst:
            for gene_name in gene_array:
                if re.search('^'+gene_name+'[\s\']|\s'+gene_name+'[\s.\']|\s'+gene_name+'$',i, re.I):
                    for trait_name in trait_array:
                        if re.search('^'+trait_name+'[\s\']|\s'+trait_name+'[\s.\']|\s'+trait_name+'$',i, re.I):
                            dic_key=gene_name+";"+trait_name
                            if(out_dic.get(dic_key)):
                                out_dic[dic_key]['sen'].add(i)
                                out_dic[dic_key]['pmid'].add(lis[0])
                            else:
                                out_dic[dic_key]={'sen':set(),'pmid':set()}
                                out_dic[dic_key]['sen'].add(i)
                                out_dic[dic_key]['pmid'].add(lis[0])
                        else:
                            continue
                else:
                    continue
outfile=open(sys.argv[2],'w')
for key in out_dic.keys():
    name=key.split(";")
    outfile.write('\t'.join(name)+'\t')
    outfile.write(str(len(out_dic[key]['sen'])))
    outfile.write('\t')
    outfile.write(str(len(out_dic[key]['pmid'])))
    outfile.write('\t')
    outfile.write(';'.join(out_dic[key]['pmid'])+'\t')
    outfile.write(';'.join(out_dic[key]['sen'])+'\n')
outfile.close()
