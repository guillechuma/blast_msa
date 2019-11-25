'''
This function reads a blast-xml file result and makes fasta file with all alignments
in a file named msa.fasta
'''

from Bio import SeqIO
from Bio import SearchIO


def blast_output_parse(blast_xml):

    EVALUE_THRESHOLD = 0.001
    QCOVER_THRESHOLD = 0.6
    blast_records = SearchIO.read(blast_xml, 'blast-xml')
    #records = []
    ids = []
    db = blast_records.target
    query_len = blast_records.seq_len
    for blast_record in blast_records:
        align_len = blast_record[0].aln_span
        query_cover = align_len/query_len
        # Only keep alignments that are below the e value threshold
        if ((blast_record[0].evalue < EVALUE_THRESHOLD) and (query_cover > QCOVER_THRESHOLD)):
            #records.append(blast_record[0].hit)
            ids.append(blast_record.accession)
    #SeqIO.write(records, 'data/msa.fasta', 'fasta')

    #Save all accesion ids to a text file
    with open('output/seq_accession.txt', 'w') as f:
        for id in ids:
            f.write("%s\n" % id)

if __name__ == '__main__':
    blast_output_parse('output/my_blast.xml')