from Bio import SeqIO
from Bio import Entrez
import time
Entrez.email = 'vorosviktoriya@yandex.ru'

id_list = []
protein_gi = []
gene_id = []

def funcstart (a):
    start = ''
    for i in range(len(a)):
        if (a[i] == ':') and (a[i+1] != '<'):
            j = i+1
            while a[j] != '.':
                start = start + a[j]
                j+=1
        if (a[i] == ':') and (a[i+1] == '<'):
            j = i+2
            while a[j] != '.':
                start = start + a[j]
                j+=1   
    return (start)


def funcend (a):
    end = ''
    for i in range(len(a)):
        if (a[i-1] == '.') and (a[i] == '.') and (a[i+1] != '>'):
            j = i+1
            if a[-1] == ")":
                while (a[j] != ")"):
                    end = end + a[j]
                    j+=1
            else:
                while (j < len(a)):
                    end = end + a[j]
                    j+=1
        if (a[i-1] == '.') and (a[i] == '.') and (a[i+1] == '>'):
            j = i+2
            if a[-1] == ")":
                while (a[j] != ")"):
                    end = end + a[j]
                    j+=1
            else:
                while (j < len(a)):
                    end = end + a[j]
                    j+=1
        
    return(end)
def gene(a):
    name = ''
    j = 0
    while a[j] != ':':
        name = name + a[j]
        if a[j-1] == '(':
            name = ''
            name = name + a[j]
        j += 1
    return (name)
    
          
#получение id номеров из последовательности для Bifidobacterii
for record in SeqIO.parse ('Рода из NCBI/Рода, NCBI, аминокислоты/Lactobacillus.fasta', "fasta"):
    id_list.append(record.id)
print(len(id_list))
'''
for accn in id_list:
    esearch_handle = Entrez.esearch(db="protein", term=accn)
    esearch_result= Entrez.read(esearch_handle)
    esearch_handle.close()
    protein_gi.append(esearch_result["IdList"][0])
print(len(protein_gi))
print(protein_gi)

handle = Entrez.elink(dbfrom="protein", db = "gene", LinkName="protein_nuccore", id = protein_gi)
result = Entrez.read(handle)

for i in range(len(result)):
    if (result[i]["LinkSetDb"] != []):
        dna_id = result[i]["LinkSetDb"][0]["Link"][0]["Id"]
        gene_id.append(dna_id)
print(gene_id)
print(len(gene_id))


handle=Entrez.efetch(db="sequences", id=gene_id, rettype="gbwithparts", retmode="text")
genome = SeqIO.parse(handle, "gb").next()

'''

''''''
#Дополнительный файл по которому бум доставать CDS


a = open("Неподписанные нуклеотидные последовательности/lacto.gb", "w")
lenth=len(id_list)
p = 0
while p <= lenth:
    n = []
    j = p
    while (j>= p) and (j<lenth) and (j<(p+20)):
        n.append(id_list[j])
        j+=1
    p+=20
    print(len(n))
    handle = Entrez.efetch( db = "protein", id = n, rettype = "gb",retmode = "text")
    a.write(handle.read())
a.close()




file = open("Неподписанные нуклеотидные последовательности/lacto.fasta", 'w')
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO

m = 0

for seq_record in SeqIO.parse("Неподписанные нуклеотидные последовательности/lacto.gb", "genbank"):
    for i in range(len(seq_record.features)):
        if seq_record.features[i].type == 'CDS':
            start = funcstart(seq_record.features[i].qualifiers["coded_by"][0])
            end = funcend(seq_record.features[i].qualifiers["coded_by"][0])
            gene_id.append(gene(seq_record.features[i].qualifiers["coded_by"][0]))
            feature_number =  i
            id_list.append(seq_record.id)
#делаем запрос на геном

            handle=Entrez.efetch(db="sequences", id=gene_id[0], rettype="fasta", retmode="text")
            for result in SeqIO.parse(handle, "fasta"):
                genome = result.seq
                description = result.description
#обрезаем нужный кусок генома

            sequence = genome[(int(start)-1):int(end)]

            file.write(">"+description+"\n"+str(sequence)+"\n\n")
            gene_id = []
    m += 1
file.close()

print(m)


        
'''            
            for accn in id_list:
                esearch_handle = Entrez.esearch(db="protein", term=accn)
                esearch_result= Entrez.read(esearch_handle)
                esearch_handle.close()
                protein_gi.append(esearch_result["IdList"][0])

            handle = Entrez.elink(dbfrom="protein", db = "gene", LinkName="protein_nuccore", id = protein_gi)
            result = Entrez.read(handle)

            for i in range(len(result)):
                if (result[i]["LinkSetDb"] != []):
                    dna_id = result[i]["LinkSetDb"][0]["Link"][0]["Id"]
                    gene_id.append(dna_id)

                                
            handle=Entrez.efetch(db="sequences", id=gene_id, rettype="fasta", retmode="text")
            for result in SeqIO.parse(handle, "fasta"):
                genome = result.seq
                description = result.description'''





