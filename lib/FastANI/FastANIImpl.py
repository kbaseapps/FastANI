# -*- coding: utf-8 -*-

#BEGIN_HEADER
import os
# from KBaseReport.KBaseReportClient import KBaseReport TODO
import subprocess
from fast_ani_output import FastANIOutput
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
        :param params: Currently empty -- TODO
        :returns: Returns a dict of 'report_name' and 'report_ref'
        '''
        #BEGIN fast_ani
        print('Starting FastANI function and validating parameters.')
        # if 'workspace_name' not in params:
        #     raise ValueError('Parameter workspace_name is not set in input arguments')
        # if 'assembly_input_ref' not in params:
        #     raise ValueError('Parameter assembly_input_ref is not set in input arguments')
        # Construct the shell command for running FastANI using
        args = [
            "../bin/FastANI/fastANI",
            "-q", "../bin/FastANI/data/Escherichia_coli_str_K12_MG1655.fna",
            "-r", "../bin/FastANI/data/Shigella_flexneri_2a_01.fna",
            "-o", "/dev/stdout"
        ]
        # TODO handle the error case
        result_str = subprocess.check_output(args)
        output = FastANIOutput(result_str)
        # report_obj = {
        #     'objects_created': [],
        #     'text_message': "Total percentage match: " + output.percentage_match
        # }
        # report = KBaseReport(self.callback_url)
        # report_info = report.create({'report': report_obj})
        # results = {'report_name': report_info['name'], 'report_ref': report_info['ref']}
        results = {'percentage_match': output.percentage_match}
        #END fast_ani
        # return [results] TODO make report
        return results
