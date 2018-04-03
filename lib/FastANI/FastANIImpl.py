# -*- coding: utf-8 -*-

#BEGIN_HEADER
import os
from KBaseReport.KBaseReportClient import KBaseReport
from fast_ani_proc import FastANIProc
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
        if 'workspace_name' not in params:
            raise ValueError('Parameter "workspace_name" is not set in input arguments')
        if 'reference_genome' not in params and 'reference_list' not in params:
            raise ValueError('Pass a parameter for either "reference_genome" or "reference_list"')
        # Download the query genome
        assembly_util = AssemblyUtil(self.callback_url)
        query_file = assembly_util.get_assembly_as_fasta({
            'ref': params['query_genome']
        })
        # Fetch either a single reference genome or a list of references
        # In either case, we pass an array of references to FastANIProc
        if params['reference_genome']:
            ref = assembly_util.get_assembly_as_fasta({'ref': params['reference_genome']})
            refs = [ref['path']]
        else:
            refs = ['xyz']  # TODO fetch references from AssemblySet (???)
            pass
        fast_ani_proc = FastANIProc(query_file['path'])
        fast_ani_proc.run(refs)
        report_obj = {
            'objects_created': [],
            'text_message': 'Total percentage match: ' + fast_ani_proc.percentage_match
        }
        report = KBaseReport(self.callback_url)
        report_info = report.create({
            'report': report_obj,
            'workspace_name': params['workspace_name']
        })
        results = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
            'percentage_match': fast_ani_proc.percentage_match,
            'orthologous_matches': fast_ani_proc.orthologous_matches,
            'total_fragments': fast_ani_proc.total_fragments
        }
        #END fast_ani
        return results
