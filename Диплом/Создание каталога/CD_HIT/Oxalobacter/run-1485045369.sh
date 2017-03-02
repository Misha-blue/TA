#!/bin/sh
#$ -S /bin/bash
#$ -v PATH=/home/oasis/data/webcomp/RAMMCAP-ann/bin:/usr/local/bin:/usr/bin:/bin
#$ -v BLASTMAT=/home/oasis/data/webcomp/RAMMCAP-ann/blast/bin/data
#$ -v LD_LIBRARY_PATH=/home/oasis/data/webcomp/RAMMCAP-ann/gnuplot-install/lib
#$ -v PERL5LIB=/home/hying/programs/Perl_Lib
##$ -q all.q
#$ -pe orte 4
#$ -e /home/oasis/data/webcomp/web-session/1485045369/1485045369.err
#$ -o /home/oasis/data/webcomp/web-session/1485045369/1485045369.out
cd /home/oasis/data/webcomp/web-session/1485045369
faa_stat.pl 1485045369.fas.0

/home/oasis/data/NGS-ann-project/apps/cd-hit/cd-hit -i 1485045369.fas.0 -d 0 -o 1485045369.fas.1 -c 1 -n 5  -G 1 -g 1 -b 20 -s 0.0 -aL 0.0 -aS 0.0 -T 4 -M 32000
faa_stat.pl 1485045369.fas.1
/home/oasis/data/NGS-ann-project/apps/cd-hit/clstr_sort_by.pl no < 1485045369.fas.1.clstr > 1485045369.fas.1.clstr.sorted
clstr_list.pl 1485045369.fas.1.clstr 1485045369.clstr.dump
gnuplot1.pl < 1485045369.fas.1.clstr > 1485045369.fas.1.clstr.1; gnuplot2.pl 1485045369.fas.1.clstr.1 1485045369.fas.1.clstr.1.png
clstr_list_sort.pl 1485045369.clstr.dump 1485045369.clstr_no.dump
clstr_list_sort.pl 1485045369.clstr.dump 1485045369.clstr_len.dump len
clstr_list_sort.pl 1485045369.clstr.dump 1485045369.clstr_des.dump des
tar -zcf 1485045369.result.tar.gz * --exclude=*.dump --exclude=*.env
echo hello > 1485045369.ok
