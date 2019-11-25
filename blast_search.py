'''
This function reads a fasta file and makes a BLAST search over the internet
and returns appropiate output
'''

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
from Bio import SearchIO

def blast_search(file, program, database):
    #Locate the file
    record = SeqIO.read(file, format = 'fasta')

    #Make query
    result_handle = NCBIWWW.qblast(program, database, record.format('fasta'))

    #Handle the output into a xml file
    with open('output/my_blast.xml', 'w') as save_to:
        save_to.write(result_handle.read())
        result_handle.close()



def test():
    E_VALUE_THRESH = 0.001
    #blast_search('data/test.fasta', 'blastp', 'swissprot')
    blast_records = SearchIO.read('output/my_blast.xml', 'blast-xml')
    records = []
    for blast_record in blast_records:
        records.append(blast_record[0].hit)
    SeqIO.write(records,'data/msa.fasta', 'fasta')

    '''
    for blast_record in blast_records:
        if blast_record.alignments: #Skip queries with no matches
            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    if hsp.expect < E_VALUE_THRESH:
                        print('****Alignment****')
                        print('sequence: ' + alignment.title)
                        print('length: '+ str(alignment.length))
                        print('e value: ' + str(hsp.expect))
                        print(hsp.query[0:75] + '...')
                        print(hsp.match[0:75] + '...')
                        print(hsp.sbjct[0:75] + '...')
    '''