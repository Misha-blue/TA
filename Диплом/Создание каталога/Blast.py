'''import Bio
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
result_handle = NCBIWWW.qblast("blastp", "nr", "WP_012938051")
blast_result = open("C:/Users/voros/Desktop/Создание каталога/Рода из NCBI/my_blast.xml", "w")
blast_result.write(result_handle.read())
blast_result.close()
result_handle.close()'''

'''
E_VALUE_THRESH = 0.04

for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
         if hsp.expect < E_VALUE_THRESH:
             print('****Alignment****')
             print('sequence:', alignment.title)
             print('length:', alignment.length)
             print('e value:', hsp.expect)
             print(hsp.query[0:75] + '...')
             print(hsp.match[0:75] + '...')
             print(hsp.sbjct[0:75] + '...')'''
import Bio
from Bio import SeqIO
from Bio.Blast import  NCBIWWW
from Bio.Blast import NCBIXML
id_list = []
file_string = ''

path_f = open("Рода из NCBI/Acidaminococcus.fasta")
for record in SeqIO.parse (path_f, "fasta"):
    id_list.append(record.id)
    print(record.id)

fasta_files = id_list
for i in range(len(fasta_files)):
    File = open("Acidaminococcus"+str(i)+".fasta","w")
    print(fasta_files[i])
    result_handle = NCBIWWW.qblast("blastp", "nr", fasta_files[i], hitlist_size=10)

    blast_records = NCBIXML.parse(result_handle) 
    #or blast_record = NCBIXML.read(result_handle) if you only have one seq in file
    E_VALUE_THRESH = 0.001
    for blast_record in blast_records:
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect < E_VALUE_THRESH:
                   file_string += str(alignment)
                   file_string += str(hsp.expect)
    File.write(file_string)









