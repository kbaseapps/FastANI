# -*- coding: utf-8 -*-
import sys
import os
import subprocess
import multiprocessing

# This module provides a way to run the fastANI binary, pass
# in data, and read the output


def run_fast_ani(scratch, paths):
    """
    :param scratch: file path of the scratch directory
    :param paths: dict with keys 'query' - path to the query genome file
                                 'reference' - path to the reference genome file
    :returns: output file path
    """
    out_name = 'fastani.out'
    out_path = os.path.join(scratch, out_name)
    args = [
        'fastANI',
        '--ql',
        paths['query'],
        '--rl',
        paths['reference'],
        '--visualize',
        '-o',
        out_path,
        '--threads',
        '2',
    ]
    try:
        _run_subprocess(args, 'fastANI')
    except OSError as err:
        print(('Error running fastANI:', str(err), 'with args:', args))
        raise err
    except Exception:
        print(('Unexpected error:', sys.exc_info()[0], 'with args:', args))
    _visualize(paths['query'], paths['reference'], out_path)
    return [out_path]

# TODO: update this method
def _visualize(path1, path2, out_path):
    """
    Given the output path for a fastANI result, build the PDF visualization file using Rscript
    $ Rscript scripts/visualize.R B_quintana.fna B_henselae.fna fastani.out.visual
    """
    r_path = os.path.join(os.path.dirname(__file__), 'scripts', 'visualize.R')
    script_path = os.path.abspath(r_path)
    args = ['Rscript', script_path, path1, path2, out_path + '.visual']
    try:
        _run_subprocess(args, 'Rscript visualization')
    except OSError as err:
        print(('Error running visualizer:', str(err), 'with args:', args))
        raise err
    except Exception:
        print(('Unexpected error:', sys.exc_info()[0], 'with args:', args))


def _run_subprocess(args, proc_name):
    """Run a sub-process, logging stdout/err."""
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = proc.communicate()
    print(('=' * 80))
    # Note that neither fastANI nor Rscript seem to make use of stdout/err properly. fastANI prints
    # all results to stderr
    print(('Results for ' + proc_name))
    print(stdout)
    print(stderr)
    print(('=' * 80))
