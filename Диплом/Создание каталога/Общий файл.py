#получение названия всех файлов директории
import os
directory = 'Рода из NCBI Nucleotide'
path_f = []
path_add = []
for d, dirs, files in os.walk(directory): 
    for f in files:
        path_add.append(f)
        path = os.path.join(d,f)
        path_f.append(path)
print (path_add)
print (len(path_add))



from Bio import SeqIO


a = open("BLAST_@/General_file.fasta", "w")
for i in range(len(path_add)):
    seq_list = []
    name_list = []
    description_list = []
    for record in SeqIO.parse ('Рода из NCBI Nucleotide/'+path_add[i], "fasta"):
        a.write(">"+record.description+"\n"+str(record.seq)+"\n\n")
a.close()
    
    
