# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
from KBaseReport.KBaseReportClient import KBaseReport
from fast_ani_proc import FastANIProc
from fast_ani_output import FastANIOutput
from fetch_assembly import fetch_multiple
#END_HEADER


class FastANI:
    '''
    Module Name:
    FastANI

    Module Description:
    A KBase module: FastANI
    '''

    VERSION = "0.0.1"
    GIT_URL = "https://github.com/jayrbolton/kbase-fastANI.git"
    GIT_COMMIT_HASH = "c2dfe6c350b994f4d1ae04c95163473af8033487"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        #END_CONSTRUCTOR
        return

    def fast_ani(self, ctx, params):
        """
        :param params: instance of type "FastANIParams" (fast_ani input) ->
           structure: parameter "workspace_name" of String, parameter
           "query_assembly_refs" of list of String, parameter
           "reference_assembly_refs" of list of String
        :returns: instance of type "FastANIResults" (fast_ani output) ->
           structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        # ctx is the context object
        # return variables are: results
        #BEGIN fast_ani
        print('Starting FastANI function and validating parameters.')
        for name in ['workspace_name', 'query_assembly_refs', 'reference_assembly_refs']:
            if name not in params:
                raise ValueError('Parameter "' + name + '" is not set in input arguments')
        # Download the query assemblies
        query_files = fetch_multiple(self.callback_url, params['query_assembly_refs'])
        reference_files = fetch_multiple(self.callback_url, params['reference_assembly_refs'])
        fast_ani_proc = FastANIProc(query_files, reference_files)
        fast_ani_output = FastANIOutput(fast_ani_proc.raw_output)
        report_info = KBaseReport(self.callback_url).create({
            'report': {'objects_created': [], 'text_message': fast_ani_output.summary},
            'workspace_name': params['workspace_name']
        })
        results = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref']
        }
        #END fast_ani
        return [results]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
