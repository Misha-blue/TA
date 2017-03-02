library("Biostrings")
s = readDNAStringSet("Final.fasta",use.names = T, seek.first.rec = T) 
discription <- names(s) 
s <- as.data.frame(s)
s$id <- rownames(s)
rownames(s) <- (1:nrow(s))
colnames(s) <- c('seq', 'id')

get_genus <- function(df){
  id <- df$id
  genus <- sapply(id, function(x) strsplit(x,split = ' ')[[1]][1])
  return(genus)
}

s$genus <- get_genus(s)

get_domen <- function(df) {
  id <- df$id
  domen <- sapply(id, function(x) tail(strsplit(x,split = '~')[[1]], n=1))
  return(domen)
}

s$domen <- get_domen(s)

unique_domens <- unique(s$domen) # only 26 WTF?????

get_number_for_genus <- function(genus){
  return(length(unique(s[s$genus==genus,]$domen)))
}

number_of_domens_for_genus <-sapply(unique(s$genus), get_number_for_genus)

saveRDS(number_of_domens_for_genus, file = 'number_of_domen_for_genus.rds')
number_of_domens_for_genus <- readRDS('number_of_domen_for_genus.rds')
