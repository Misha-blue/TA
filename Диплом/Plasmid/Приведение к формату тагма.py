def chose(a):
    s = []
    p = ''
    m = 0
    for i in range(len(a)):
        s.append(a[i])
    for i in range(len(s)):
        if s[i] == '~':
            m +=1
        if m == 2:
            s[i] = '|'
            m -=1
    for i in range(len(s)):
        p += s[i]
    return(p)
       
from Bio import SeqIO
file = open('final_fot_tagma.fasta', 'w')
for record in SeqIO.parse('Final.fasta', "fasta"):
    file.write(">"+str(chose(record.description))+"\n"+str(record.seq)+"\n\n")
file.close()
