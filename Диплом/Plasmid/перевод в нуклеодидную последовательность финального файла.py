def chose(a):
    s = ''
    m = 0
    for i in range(len(a)):
        if (m == 0) and(a[i] == '~'):
            j = i+1
            m +=1
            while (a[j] != "~"):
                s = s + a[j]
                j+=1
    return(s)
                
id_list = []
description_list = []
from Bio import SeqIO
file = open('Final_file_protein', 'w')
for record in SeqIO.parse('Final.fasta', "fasta"):
    id_list.append(chose(record.description))
    description_list.append(record.description)

print(len(description_list))


from Bio import Entrez
import time
Entrez.email = 'vorosviktoriya@yandex.ru'



id_list1 = []
seq_list = []
s = ''
p = 0


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
    seq_list.append(record.seq)
print(len(seq_list))
a = open('Final_file_protein.fasta', 'w')
for j in range(len(description_list)):
    a.write(">"+description_list[j]+"\n")
    a.write(str(seq_list[j])+"\n\n")
a.close()

