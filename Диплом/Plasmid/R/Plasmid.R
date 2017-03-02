s = read.table('File_with_plasmid.txt')
s <- as.data.frame(s)
View(s)
colnames(s) <- c('qseqid','sseqid', '%_ident','query_len','alignment_length', 'match','gap','qstart','qend', 'ssart', 'send' ,'evalue', 'bitscore') 
View(s)

s$alight <- s$qend-s$qstart+1
s$query_cover <- s$alight/s$query_len*100
View(s)

new <- subset.data.frame(s , subset = s$query_cover>90 & s$`%_ident`>80)
View(new)

m <-as.character(unique(new$qseqid))

write.table(m , file = "Numbers.txt")

