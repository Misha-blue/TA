a = ['Alistipes','Bacteroides','Odoribacter','Parabacteroides', 'Prevotella', 'Acidaminococcus', 'Anaerococcus', 'Anaerofustis', 'Anaerostipes', 'Anaerotruncus', 'Blautia', 'Bryantella', 'Butyrivibrio', 'Catenibacterium', 'Clostridium', 'Coprococcus', 'Dorea', 'Dialister', 'Enterococcus', 'Eubacterium', 'Faecalibacterium', 'Holdemania', 'Lactobacillus', 'Leuconostos', 'Listeria', 'Mitsuokella', 'Megamonas', 'Megasphaera', 'Parvimonas', 'Pediococcus', 'Roseburia', 'Ruminococcus', 'Streptococcus', 'Subdoligranulum', 'Turicibacter', 'Veillonella', 'Weissella', 'Actinomyces', 'Bifidobacterium', 'Collinsella', 'Eggerthella', 'Gordonibacter', 'Desulfovibrio', 'Enterobacter', 'Escherichia', 'Helicobacter', 'Klebsiella', 'Oxalobacter', 'Proteus', 'Providencia', 'Anaerobaculum', 'Akkermansia', 'Fusobacterium', 'Methanobrevibacter', 'Mollicutes']
b = ['AbrB-like', 'Arc', 'BrnA_antitoxin', 'CcdA', 'CopG_antitoxin', 'DUF1778', 'DUF1902', 'DUF217', 'DUF2540', 'DUF2610', 'HicB-like_2', 'HicB', 'HicB_lk_antitox', 'MazE_antitoxin', 'MetJ', 'Mraz', 'Omega_Repress', 'ParD', 'ParD_antitoxin', 'ParD_like', 'ParG', 'PhdYeFM_antitox', 'PHD_like', 'PrlF_antitoxin', 'PSK_trans_fac', 'REGB_T4', 'RelB', 'RepB-RCR_reg', 'RHH_1', 'RHH_3', 'RHH_4', 'RHH_5', 'RHH_7', 'SeqA_N', 'TraY', 'VapB_antitoxin', 'VirC2', 'BrnT_toxin', 'CcdB', 'DUF1918', 'Gp49', 'HicA_toxin', 'HigB-like_toxin', 'ParE-like_toxin', 'ParE_toxin', 'PemK_toxin', 'RelE', 'YafQ_toxin', 'YoeB_toxin']
n = []
for i  in range(len(b)):
    s = ''
    s = b[i]
    n.append(s)
print(n)


for i in range(len(b)):
    b[i] = open('Распределение по домена амино/'+n[i]+'.fasta', 'w')
from Bio import SeqIO
handle = open("Final_file_protein.fasta", "rU")
l = SeqIO.parse(handle, "fasta")
for record in l:
    for i in range(len(n)):
        if str(n[i]) in record.description:
            b[i].write(">"+str(record.description)+"\n"+str(record.seq)+"\n\n")
for i  in range(len(n)):
    b[i].close()
