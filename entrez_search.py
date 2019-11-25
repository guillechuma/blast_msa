from Bio import Entrez
from Bio import SeqIO

def entrez_search():
    Entrez.email = "guillechuma24@gmail.com"
    f = open('output/seq_accession.txt')
    db = f.readline()
    records = []
    for id in f:
        handle = Entrez.efetch(db='protein', id=id, rettype='fasta', retmode='text')
        record = handle.read()
        records.append(record)
        handle.close()

    with open('data/msa.fasta', 'w') as f:
        for fasta in records:
            f.write("%s\n" % fasta)

entrez_search()