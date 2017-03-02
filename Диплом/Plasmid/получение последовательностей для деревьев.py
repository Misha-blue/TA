from Bio import SeqIO
s = []
file = open('Распределние по доменам, формат для GBlock/Mraz2.fasta', 'w')
for record in SeqIO.parse('Распределние по доменам, формат для GBlock/Mraz.fasta', "fasta"):
    s.append(record.description)
print(s)
m = 0
for record1 in SeqIO.parse('Распределние по доменам, формат для GBlock/Mraz1 (2).fasta', "fasta"):
    file.write(">"+s[m]+"\n"+str(record1.seq)+"\n\n")
    m+=1
file.close()
