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

    def __init__(self, queries, references, scratch):
        '''
        Initialize a FastANIProc object using query and reference genome filepaths
        :param scratch: String path of the scratch dir
        :param queries: List of paths to FASTA files of query genomes
        :param references: List of paths to FASTA files of reference genomes
        '''
        self.results = []
        query_path = self.create_file_list(queries)
        reference_path = self.create_file_list(references)
        # I tried using /dev/stdout, but it seems to not work in prod
        out_path = scratch + '/fast_ani.out'
        args = [
            'fastANI',
            '--ql', query_path,
            '--rl', reference_path,
            '-o', out_path
        ]
        # TODO handle the error case
        proc = subprocess.Popen(args)
        proc.wait()  # Blocking
        with open(out_path) as file:
            self.raw_output = file.read()

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
