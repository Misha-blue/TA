dic = {}
from Bio import SeqIO
handle = open("Final.fasta", "rU")
l = SeqIO.parse(handle, "fasta")
for i in l:
    dic[i.description] = str(i.seq)
sort = sorted(dic.items(), key=lambda item: item[0])
file = open('Final_sorted.fasta', 'w')
for i in range(len(sort)):
    file.write(">"+str(sort[i][0])+"\n"+str(sort[i][1])+"\n\n")
file.close()


