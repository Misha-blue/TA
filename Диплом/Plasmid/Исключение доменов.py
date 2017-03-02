massiv = ['Arc', 'DUF1778', 'DUF1902', 'DUF217', 'DUF2540', 'DUF2610', 'MetJ', 'Omega_Repress', 'ParG', 'PSK_trans_fac', 'REGB_T4', 'RepB-RCR_reg', 'RHH_1', 'RHH_3', 'RHH_4', 'RHH_5', 'RHH_7', 'SeqA_N', 'TraY', 'VirC2', 'DUF1918']
print(len(massiv))
print(massiv)


from Bio import SeqIO
file = open('Final.fasta', 'w')
p = 0
for record in SeqIO.parse('Prefinal.fasta', "fasta"):
    m = 0
    for i in range(len(massiv)):
        if massiv[i] in record.description:
            m +=1
    if m == 0:
        file.write(">"+str(record.description)+"\n"+str(record.seq)+"\n\n")
    else:
        print(m)
        p += 1
print(p)
file.close()

