import os
directory = 'Скачанное из NCBI'
path_f = []
path_add = []
for d, dirs, files in os.walk(directory): 
    for f in files:
        path_add.append(f)
        path = os.path.join(d,f)
        path_f.append(path)
print (path_add)

import Bio
from Bio import SeqIO        
a = open('Рода из NCBI/Butyrivibrio.fasta', 'w')
for i in range(len(path_f)):
    for record in SeqIO.parse (path_f[i], "fasta"):
        if 'Butyrivibrio' in record.description:
            a.write ('>' + record.description  + ' ' + str(path_add[i])[0:-9] + '\n')
            a.write (str(record.seq) + '\n')
a.close()
