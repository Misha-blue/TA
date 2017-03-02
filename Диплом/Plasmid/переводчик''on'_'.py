def chose(a):
    p = ''
    m = 0
    while a[m] != '~':
        p = p+a[m]
        m+=1
    return(p)
from Bio import SeqIO
m = 0
file = open('Распределние по доменам, формат для GBlock/Mraz.fasta', 'w')
file1 = open('Распределние по доменам, формат для GBlock/Mraz1.fasta', 'w')
for record in SeqIO.parse('Распределение по домена амино/Mraz.fasta', "fasta"):
    m +=1
    s = record.description.replace(" ","_")
    file.write(">"+chose(s)+"\n"+str(record.seq)+"\n\n")
    file1.write(">"+str(m)+"\n"+str(record.seq)+"\n\n")
file.close()
file1.close()
