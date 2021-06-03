import sys
file1=open(sys.argv[1],'r')
file2=open(sys.argv[2],'r')
file1_dic=dict()
file2_dic=dict()
for line1 in file1:
    line1_1=line1.strip('\n')
    file1_array=line1_1.split('\t')
    file1key=file1_array[0]+';'+file1_array[1]
    file1_dic[file1key]=file1_array[2:]
for line2 in file2:
    line2_1=line2.strip('\n')
    file2_array=line2_1.split('\t')
    file2key=file2_array[0]+';'+file2_array[1]
    file2_dic[file2key]=file2_array[2:]
outfile=open(sys.argv[3],'w')
for key in file1_dic.keys():
    name=key.split(";")
    if file2_dic.get(key):
        nsen=int(file1_dic[key][0])+int(file2_dic[key][0])
        npmid=int(file1_dic[key][1])+int(file2_dic[key][1])
        outfile.write('\t'.join(name)+'\t')
        outfile.write(str(nsen)+'\t')
        outfile.write(str(npmid)+'\t')
        outfile.write(file1_dic[key][2]+';'+file2_dic[key][2]+'\t')
        outfile.write(file1_dic[key][3]+';'+file2_dic[key][3]+'\t'+'\n')
    else:
        outfile.write('\t'.join(name)+'\t')
        outfile.write(file1_dic[key][0]+'\t')
        outfile.write(file1_dic[key][1]+'\t')
        outfile.write(file1_dic[key][2]+'\t')
        outfile.write(file1_dic[key][3]+'\n')
for key1 in file2_dic.keys():
    name=key1.split(";")
    if file1_dic.get(key1):
        continue
    else:
        outfile.write('\t'.join(name)+'\t')
        outfile.write(file2_dic[key1][0]+'\t')
        outfile.write(file2_dic[key1][1]+'\t')
        outfile.write(file2_dic[key1][2]+'\t')
        outfile.write(file2_dic[key1][3]+'\n')
outfile.close()
