# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
from .utils.fast_ani_proc import run_fast_ani
from .utils.fast_ani_output import get_result_data
from .utils.downloader import download_fasta
from .utils.fast_ani_report import create_report
#END_HEADER


class FastANI:
    '''
    Module Name:
    FastANI

    Module Description:
    A KBase module: FastANI
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.1.2"
    GIT_URL = "https://github.com/kbaseapps/FastANI.git"
    GIT_COMMIT_HASH = "6b8449884055b99090887a23cd0aafffd5770a6f"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        #END_CONSTRUCTOR
        pass


    def fast_ani(self, ctx, params):
        """
        :param params: instance of type "FastANIParams" (fast_ani input) ->
           structure: parameter "workspace_name" of String, parameter
           "reference" of list of type "workspace_ref", parameter "query" of
           list of type "workspace_ref"
        :returns: instance of type "FastANIResults" (fast_ani output) ->
           structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        # ctx is the context object
        # return variables are: results
        #BEGIN fast_ani
        print('Starting FastANI function and validating parameters.')
        if not params.get('workspace_name'):
            print('Parameters provided were', str(params))
            raise TypeError('Must pass a non-empty `workspace_name` arg.')

        for p in ['query', 'reference']:
            if not params.get(p) or params[p] == '' or params[p] == []:
                print('Parameters provided were', str(params))
                raise TypeError('Must pass both `query` and `reference` sequences.')
            if isinstance(params[p], str):
                params[p] = [params[p]]

        ws_name = params['workspace_name']
        # Download the data
        paths = download_fasta(params, self.shared_folder, self.callback_url)
        output_paths = run_fast_ani(self.shared_folder, paths)
        result_data = get_result_data(output_paths)
        results = create_report(
            self.callback_url, self.shared_folder, ws_name, result_data
        )
        #END fast_ani

        # At some point might do deeper type checking...
        if not isinstance(results, dict):
            raise ValueError('Method fast_ani return value ' +
                             'results is not type dict as required.')
        # return the results
        return [results]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {
            'state': 'OK',
            'message': '',
            'version': self.VERSION,
            'git_url': self.GIT_URL,
            'git_commit_hash': self.GIT_COMMIT_HASH,
        }
        #END_STATUS
        return [returnVal]
