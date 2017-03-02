#получение названия всех файлов директории
import os
directory = 'Рода из NCBI/Рода, NCBI, аминокислоты'
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
from Bio import Entrez
import time
Entrez.email = 'vorosviktoriya@yandex.ru'

id_list = []
gene_id = []

#функции для названия, чтобы выбрать только координаты начала-конца, а также номер соответствующего генома
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
                while ( a[j] != ")" ):
                    if a[j]!= ',':
                        end = end + a[j]
                    else:
                        break
                    j+=1
            else:
                while (j < len(a)):
                    end = end + a[j]
                    j+=1
        if (a[i-1] == '.') and (a[i] == '.') and (a[i+1] == '>'):
            j = i+2
            if a[-1] == ")":
                while (a[j] != ")" ):
                    if a[j]!= ',':
                        end = end + a[j]
                    else:
                        break
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

def chose(a):
    i = 1
    s = ''
    while a[-i] != ' ':
        s = a[-i] + s
        i +=1 
    return(s)

def descript(a):
    s = ''
    for i in range(len(a)):
        if ((a[i] == '[') and (a[i+1] != '[')):
            j = i+1
            while a[j] != ']':
                s = s + a[j]
                j+=1
        elif ((a[i] == '[') and (a[i+1] == '[')):
            j =i+2
            while a[j] != ']':
                s = s+ a[j]
                j = j+1
            j = j+1
            while a[j] != ']':
                s = s+ a[j]
                j = j+1
            break
    return(s)

        
        





#парсинг gb и получеине
for i in range(len(path_add)):
    id_list = []
    gene_id = []
    name_list = []
    description_list = []
    for record in SeqIO.parse ('Рода_NCBI_без_повторов/'+path_add[i], "fasta"):
        id_list.append(record.id)
        name_list.append(chose(record.description))
        description_list.append(descript(record.description))
    print(path_add[i])
    print(len(id_list))







    file = open("Рода из NCBI Nucleotide/"+path_add[i], 'w')
    file1 = open("Simple_amino/"+path_add[i], 'w')
    from Bio.SeqFeature import SeqFeature, FeatureLocation
    from Bio import SeqIO
    m = 0
    for seq_record in SeqIO.parse("gb_files/"+path_add[i]+".gb", "genbank"):
        for i in range(len(seq_record.features)):
            if seq_record.features[i].type == 'CDS':
#                print(seq_record.id)
                start = funcstart(seq_record.features[i].qualifiers["coded_by"][0])
                end = funcend(seq_record.features[i].qualifiers["coded_by"][0])
#                print(start)
#                print(end)
#                print(gene(seq_record.features[i].qualifiers["coded_by"][0]))
                gene_id.append(gene(seq_record.features[i].qualifiers["coded_by"][0]))
                feature_number =  i
                id_list.append(seq_record.id)
#                print(seq_record.features[i].location.strand)
#делаем запрос на геном
                handle=Entrez.efetch(db="sequences", id=gene_id[0], rettype="fasta", retmode="text")
                for result in SeqIO.parse(handle, "fasta"):
                    genome = result.seq
#обрезаем нужный кусок генома

                sequence = genome[(int(start)-1):int(end)]
                if "complement" in seq_record.features[i].qualifiers["coded_by"][0]:
                    sequence = sequence.reverse_complement()
                else:
                    sequence = sequence

                file.write(">"+description_list[m]+'~'+seq_record.id+"~"+ name_list[m]+"\n"+str(sequence)+"\n\n")
                gene_id = []
            else:
                file1.write(">"+seq_record.id+"~"+description_list[m]+"~"+ name_list[m]+"\n")
                
        m +=1
    print(m)

    file.close()
    file1.close()

'''    
#апись в gb file        
    a = open("C:/Users/voros/Desktop/Создание каталога/gb_files/"+path_add[i]+".gb", "w")
    lenth=len(id_list)
    p = 0
    while p <= lenth:
        n = []
        j = p
        while (j>= p) and (j<lenth) and (j<(p+20)):
            n.append(id_list[j])
            j+=1
        p+=20
        handle = Entrez.efetch( db = "protein", id = n, rettype = "gb",retmode = "text")
        a.write(handle.read())
    a.close()'''









