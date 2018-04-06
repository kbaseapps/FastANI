import multiprocessing
from AssemblyUtil.AssemblyUtilClient import AssemblyUtil

# Fetch genome assemblies in parallel


def fetch_assembly(callback_url, ref):
    '''
    Fetch a single assembly file with a workspace reference
    '''
    assembly_util = AssemblyUtil(callback_url)
    return assembly_util.get_assembly_as_fasta({'ref': ref})['path']


def fetch_multiple(callback_url, refs):
    '''
    Fetch multiple assembly files in parallel and return them in an array
    :param callback_url:
    :param refs: array of workspace references to assemblies
    :returns: array of file path
    '''
    pool = multiprocessing.Pool(processes=len(refs))
    jobs = []
    for ref in refs:
        jobs.append(pool.apply_async(fetch_assembly, (callback_url, ref)))
    return [j.get() for j in jobs]
