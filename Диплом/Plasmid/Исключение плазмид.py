def func(a):
    s  = ""
    for i in range(len(a)):
        if a[i] == " ":
            j = i+2
            while a[j] != '"':
                s = s + a[j]
                j +=1
    return(s)
massiv = []
number_file = open('Numbers.txt', 'r')
for line in number_file:
    massiv.append(func(line))
massiv.remove('')
print(len(massiv))

p = 0
from Bio import SeqIO
file = open('Prefinal.fasta', 'w')
for record in SeqIO.parse('General_file.fasta', "fasta"):
    m = 0
    for i in range(len(massiv)):
        if massiv[i] in record.description:
            m +=1
    if m == 0:
        file.write(">"+str(record.description)+"\n"+str(record.seq)+"\n\n")
    else:
        print(m)
        p+=1
print(p)
file.close()



    
