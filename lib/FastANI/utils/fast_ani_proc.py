# -*- coding: utf-8 -*-
import sys
import os
import subprocess
import multiprocessing

# This module provides a way to run the fastANI binary, pass
# in data, and read the output


def run_fast_ani_pairwise(scratch, paths):
    """
    Given a list of assembly paths, run fastANI on every pair
    Runs in parallel on each cpu
    :param scratch: string path where to put all output
    :param paths: list of paths to each assembly file (fasta format)
    :returns: array of output result paths
    """
    # We have to cap cpus at 2 so we dont overuse our container node's resources
    # If we only have 1 cpu available, it will just run serial but threaded
    pool = multiprocessing.Pool(processes=2)
    jobs = []
    for p1 in paths:
        for p2 in paths:
            if p1 == p2:
                continue
            jobs.append(pool.apply_async(__run_proc, (scratch, p1, p2)))
    out_paths = [j.get() for j in jobs]
    return out_paths


def __run_proc(scratch, path1, path2):
    """
    :param scratch: file path of the scratch directory
    :param path1: path for the query genome file
    :param path2: path for the reference genome file
    :returns: output file path
    """
    def basename(path): return os.path.basename(path).split('.')[0]
    out_name = basename(path1) + '-' + basename(path2) + '.out'
    out_path = os.path.join(scratch, out_name)
    args = ['fastANI', '-q', path1, '-r', path2, '--visualize', '-o', out_path, '--threads', '2']
    try:
        subprocess.Popen(args).wait()
    except OSError as err:
        print('Error running fastANI:', str(err), 'with args:', args)
        raise err
    except:
        print('Unexpected error:', sys.exc_info()[0], 'with args:', args)
    __visualize(path1, path2, out_path)
    return out_path


def __visualize(path1, path2, out_path):
    """
    Given the output path for a fastANI result, build the PDF visualization file using Rscript
    $ Rscript scripts/visualize.R B_quintana.fna B_henselae.fna fastani.out.visual
    """
    script_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'scripts', 'visualize.R')
    )
    args = ['Rscript', script_path, path1, path2, out_path + '.visual']
    try:
        subprocess.Popen(args).wait()
    except OSError as err:
        print('Error running visualizer:', str(err), 'with args:', args)
        raise err
    except:
        print('Unexpected error:', sys.exc_info()[0], 'with args:', args)
