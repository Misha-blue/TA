s = read.table("with_plasmids.txt")
s <- as.data.frame(s) 
colnames(s) <- c('qseqid','sseqid', '%_ident','query_len','alignment_length', 'match','gap','qstart','qend', 'ssart', 'send' ,'evalue', 'bitscore') 
m <- unique(s$qseqid)
m <- length(m)
View(s) 

s$alight <- s$qend-s$qstart+1
s$query_cover <- s$alight/s$query_len*100

new <- subset.data.frame(s , subset = s$query_cover>90 & s$`%_ident`>95)
View(new)
m <- unique(new$qseqid)
m <- length(m)
