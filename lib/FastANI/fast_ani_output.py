
# This object represents the output data after running the FastANI binary
# It needs some minor parsing and annotation


class FastANIOutput:
    '''
    Given the result string from running the fastANI binary, parse it into discrete/named parts

    Example result string from fastANI:
    data/Shigella_flexneri_2a_01.fna data/Escherichia_coli_str_K12_MG1655.fna 97.7443 1305 1608
    '''

    def __init__(self, string):
        parts = string[:-1].split(" ")
        self.percentage_match = parts[2]
        self.orthologous_matches = parts[3]
        self.total_fragments = parts[4]
        pass
