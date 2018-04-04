from AssemblyUtil.AssemblyUtilClient import AssemblyUtil

# Some simple boilerplate to fetch an assembly path


def fetch_assembly(callback_url, ref):
    assembly_util = AssemblyUtil(callback_url)
    return assembly_util.get_assembly_as_fasta({'ref': ref})['path']


def fetch_multiple(callback_url, refs):
    '''
    Fetch multiple assembly files and return them in an array
    :param callback_url:
    :param refs: array of workspace references to assemblies
    :returns: array of paths
    '''
    paths = []
    for ref in refs:
        paths.append(fetch_assembly(callback_url, ref))
    return paths
