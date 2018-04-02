# -*- coding: utf-8 -*-

#BEGIN_HEADER
import os
from KBaseReport.KBaseReportClient import KBaseReport
from pprint import pformat
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
        print('Starting FastANI function. Params=')
        print(params)
        print('Validating parameters.')
        if 'workspace_name' not in params:
            raise ValueError('Parameter workspace_name is not set in input arguments')
        if 'assembly_input_ref' not in params:
            raise ValueError('Parameter assembly_input_ref is not set in input arguments')
        report_obj = {
            'objects_created': [],
            'text_message': 'Hiya'
        }
        report = KBaseReport(self.callback_url)
        report_info = report.create({
            'report': report_obj,
            'workspace_name': params['workspace_name']
        })
        output = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref']
        }
        print('Returning:' + pformat(output))
        return output
