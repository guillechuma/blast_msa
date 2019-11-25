from Bio.Align.Applications import ClustalOmegaCommandline
import os

in_file = "data/msa.fasta"

def run_clustal_omega(msa_file):

    out_file = 'output/msa_output_carbapemenase.fasta'
    clustalomega_cline = ClustalOmegaCommandline(infile=msa_file, outfile=out_file, auto=False)
    cmd = str(clustalomega_cline) + ' --force'
    print(cmd)
    os.system(cmd)



run_clustal_omega(in_file)