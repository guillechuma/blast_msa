from blast_search import blast_search
from blast_output_parse import blast_output_parse
from entrez_search import entrez_search
from run_clustal_omega import run_clustal_omega

def msa_creator(fasta_file):

    print('Peforming blast search')
    blast_search(fasta_file, 'blastp', 'swissprot')
    print('DONE')

    print('Parsing blast result')
    print('Getting accesion number of hits')
    blast_output_parse('output/my_blast.xml')
    print('DONE')

    print('Retrieving sequence from entrez')
    entrez_search()
    print('DONE')

    print('Running clustal omega to make msa')
    run_clustal_omega('data/msa.fasta')
    print('DONE')

    print('Program finished')


msa_creator('data/test.fasta')