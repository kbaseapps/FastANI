# -*- coding: utf-8 -*-

#BEGIN_HEADER
import os
from KBaseReport.KBaseReportClient import KBaseReport
import subprocess
from fast_ani_output import FastANIOutput
from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
#END_HEADER


class FastANI:
    '''
    FastANI wrapper as a KBase SDK module
    '''
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        #END_CONSTRUCTOR

    def fast_ani(self, ctx, params):
        '''
        Run the FastANI utility on a query genome and set of reference genomes to find similarity
        :param ctx: the sdk context object
        :param params: A dict of parameters
        :returns: A dict of return values
        '''
        #BEGIN fast_ani
        print('Starting FastANI function and validating parameters.')
        param_names = ['workspace_name', 'query_genome_ref']
        for name in param_names:
            if name not in params:
                raise ValueError('Parameter ' + name + ' is not set in input arguments')
        # Download the query genome as fasta
        assembly_util = AssemblyUtil(self.callback_url)
        query_file = assembly_util.get_assembly_as_fasta({
            'ref': params['query_genome_ref']
        })
        reference_file = assembly_util.get_assembly_as_fasta({
            'ref': params['reference_genome_ref']
        })
        # Construct the shell command for running FastANI
        args = [
            "fastANI",
            "-q", query_file['path'],
            "-r", reference_file['path'],
            "-o", "/dev/stdout"
        ]
        # TODO handle the error case
        result_str = subprocess.check_output(args)
        output = FastANIOutput(result_str)
        report_obj = {
            'objects_created': [],
            'text_message': "Total percentage match: " + output.percentage_match
        }
        report = KBaseReport(self.callback_url)
        report_info = report.create({
            'report': report_obj,
            'workspace_name': params['workspace_name']
        })
        results = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
            'percentage_match': output.percentage_match,
            'orthologous_matches': output.orthologous_matches,
            'total_fragments': output.total_fragments
        }
        #END fast_ani
        return results
