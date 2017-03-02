import os
directory = 'Скачанное из Pfam/Antitoxin'
path_f = []
path_add = []
for d, dirs, files in os.walk(directory): 
    for f in files:
        path_add.append(f)
        path = os.path.join(d,f)
        path_f.append(path)
print (path_f)


import Bio
from Bio import SeqIO
from Bio import Entrez
import time
Entrez.email = 'vorosviktoriya@yandex.ru'

for i in range(len(path_f)):
    id_list = []
    id_list1 = []
    seq_list = []
    s = ''
    p = 0
    for record in SeqIO.parse (path_f[i], "fasta"):
        id_list.append(record.id)
    for m in range(len(id_list)):
        j = 0
        while id_list[m][j] != '/':
            s = s + id_list[m][j]
            j+=1
        id_list[m] = s
        s = ''
    lenth = len(id_list)
    print (lenth)
    f = open('ex.txt', 'w')
    while p <= lenth:
        n = []
        j = p
        while (j>= p) and (j<lenth) and (j<(p+1000)):
            n.append(id_list[j])
            j+=1
        p+=1000
        handle = Entrez.efetch( db = "protein", id = n, rettype = "fasta",retmode = "text")
        time.sleep(1)
        f.write(handle.read())
    f.close()
    for record in SeqIO.parse("ex.txt", "fasta" ):
        id_list1.append(record.description)
        seq_list.append(record.seq)
    print(len(id_list1))
    print(len(seq_list))
    l = "Скачанное из NCBI/Antitoxin/" + str(path_add[i])
    print (l)
    a = open(l, 'w')
    for j in range(len(id_list1)):
        a.write(">"+id_list1[j]+"\n")
        a.write(str(seq_list[j])+"\n")
    a.close()

        

    
