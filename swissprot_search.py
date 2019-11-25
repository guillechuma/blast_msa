from Bio import ExPASy
from Bio import SwissProt

def swissprot_search():

    f = open('output/seq_accession.txt')
    db = f.readline()
    for accession in f:
        handle = ExPASy.get_sprot_raw(accession)
        record = SwissProt.read(handle)
        print(record)

swissprot_search()