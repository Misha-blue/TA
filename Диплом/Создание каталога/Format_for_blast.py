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
                
        
from Bio import SeqIO
file = open('BLAST_@/General_file_with_acc.fasta', 'w')
for record in SeqIO.parse('BLAST_@/General_file.fasta', "fasta"):
    file.write(">"+str(chose(record.description))+" "+str(record.description)+"\n"+str(record.seq)+"\n\n")
file.close()
                          
