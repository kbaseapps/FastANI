import subprocess
import tempfile
import os

# This module provides a way to run the fastANI binary, pass
# in data, and read the output


class FastANIProc:
    '''
    A wrapper for the FastANI binary, allowing easy parsing of parameters and results

    Example result string from fastANI:
    "data/Shigella_flexneri_2a_01.fna data/Escherichia_coli_str_K12_MG1655.fna 97.7443 1305 1608"

    This module can be expanded if we need more parsing/processing
    functionality
    '''

    def __init__(self, query_path):
        '''
        Initialize a FastANIProc object using the path of a genome to query against
        :param query_path: Pass in the file path for the FASTA file of the genome to query
        '''
        self.query_path = query_path
        if not os.path.isfile(query_path):
            raise ValueError('File path does not exist for query assembly: ' + query_path)
        return

    def run(self, refs):
        '''
        Execute fastANI against a single reference or a list of references
        :param refs: List of paths to FASTA files of reference genomes
        '''
        reference_path = self.create_reference_file(refs)
        args = [
            'fastANI',
            '-q', self.query_path,
            '--rl', reference_path,
            '-o', '/dev/stdout'
        ]
        # TODO handle the error case
        out_str = subprocess.check_output(args)
        self.get_output(out_str)
        return self

    def create_reference_file(self, ref_paths):
        '''
        Create a file that lists paths, one per line (required by fastANI)
        :param refs: a list of genome fasta pathnames
        '''
        # Check that all paths exist
        for path in ref_paths:
            if not os.path.isfile(path):
                raise ValueError('File path does not exist for reference assembly: ' + path)
        contents = "\n".join(ref_paths)
        file = tempfile.NamedTemporaryFile(delete=False)
        file.write(contents)
        file.close()
        return file.name

    def get_output(self, out_str):
        '''
        Parse the output content after executing the binary
        :param out_str: Output string from running FastANI (see self.run)
        '''
        parts = out_str[:-1].split(" ")
        self.percentage_match = parts[2]
        self.orthologous_matches = parts[3]
        self.total_fragments = parts[4]
        return self
