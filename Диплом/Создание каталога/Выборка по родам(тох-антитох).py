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
print (len(path_add))

roda = ['Alistipes','Bacteroides','Odoribacter','Parabacteroides', 'Prevotella', 'Acidaminococcus', 'Anaerococcus', 'Anaerofustis', 'Anaerostipes', 'Anaerotruncus', 'Blautia', 'Bryantella', 'Butyrivibrio', 'Catenibacterium', 'Clostridium', 'Coprococcus', 'Dorea', 'Dialister', 'Enterococcus', 'Eubacterium', 'Faecalibacterium', 'Holdemania', 'Lactobacillus', 'Leuconostos', 'Listeria', 'Mitsuokella', 'Megamonas', 'Megasphaera', 'Parvimonas', 'Pediococcus', 'Roseburia', 'Ruminococcus', 'Streptococcus', 'Subdoligranulum', 'Turicibacter', 'Veillonella', 'Weissella', 'Actinomyces', 'Bifidobacterium', 'Collinsella', 'Eggerthella', 'Gordonibacter', 'Desulfovibrio', 'Enterobacter ', 'Escherichia', 'Helicobacter', 'Klebsiella', 'Oxalobacter ', 'Proteus', 'Providencia', 'Anaerobaculum', 'Akkermansia', 'Fusobacterium', 'Methanobrevibacter', 'Mollicutes']
print(len(roda))
m = 0

import Bio
from Bio import SeqIO
for j in range(len(roda)):
    a = open('Рода из NCBI/'+roda[j]+'.fasta', 'w')
    for i in range(len(path_f)):
        for record in SeqIO.parse (path_f[i], "fasta"):
            if roda[j] in record.description:
                a.write ('>' + record.description  + ' ' + str(path_add[i])[0:-9] + '\n')
                a.write (str(record.seq) + '\n' +'\n')
    m +=1
    a.close()
    print(m)
