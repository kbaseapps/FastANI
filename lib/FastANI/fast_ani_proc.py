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

    def __init__(self, queries, references):
        '''
        Initialize a FastANIProc object using query and reference genome filepaths
        :param queries: List of paths to FASTA files of query genomes
        :param references: List of paths to FASTA files of reference genomes
        '''
        self.results = []
        query_path = self.create_file_list(queries)
        reference_path = self.create_file_list(references)
        args = [
            'fastANI',
            '--ql', query_path,
            '--rl', reference_path,
            '-o', '/dev/stdout'
        ]
        # TODO handle the error case
        self.raw_output = subprocess.check_output(args)

    def create_file_list(self, paths):
        '''
        Create a file that lists paths, one per line (required by fastANI)
        :param refs: a list of genome fasta pathnames
        '''
        # Check that all paths exist
        for path in paths:
            if not os.path.isfile(path):
                raise ValueError('File path does not exist for reference assembly: ' + path)
        contents = "\n".join(paths)
        file = tempfile.NamedTemporaryFile(delete=False)
        file.write(contents)
        file.close()
        return file.name
