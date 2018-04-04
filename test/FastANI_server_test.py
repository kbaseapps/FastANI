# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
# import requests
import subprocess

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except ImportError:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from FastANI.FastANIImpl import FastANI
from FastANI.FastANIServer import MethodContext
from FastANI.authclient import KBaseAuth as _KBaseAuth

from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
from shutil import copyfile

# Test file data provided by FastANI
TEST_FILE_1 = '/tmp/fastANI-data/Escherichia_coli_str_K12_MG1655.fna'
TEST_FILE_2 = '/tmp/fastANI-data/Shigella_flexneri_2a_01.fna'


class FastANITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('FastANI'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'FastANI',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL)
        cls.serviceImpl = FastANI(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_FastANI_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    def load_fasta_file(self, path, name):
        assembly_util = AssemblyUtil(self.callback_url)
        return assembly_util.save_assembly_from_fasta({
            'file': {'path': path},
            'workspace_name': self.getWsName(),
            'assembly_name': name
        })

    def test_fastani_binary(self):
        '''
        Run the compiled binary using the given example data
        '''
        out_path = '/tmp/fastani-out.txt'
        args = [
            'fastANI',
            '-q', TEST_FILE_2,
            '-r', TEST_FILE_1,
            '-o', out_path
        ]
        subprocess.call(args)
        self.assertTrue(os.path.isfile(out_path))
        return

    def test_single_reference(self):
        '''
        Test a basic call to FastANIImpl.fast_ani using a query and reference assembly
        Copy the FastANI example data into the scratch dir
        '''
        a_path = self.scratch + '/a.fna'
        b_path = self.scratch + '/b.fna'
        copyfile(TEST_FILE_1, a_path)
        copyfile(TEST_FILE_2, b_path)
        a_ref = self.load_fasta_file(a_path, 'test_assembly_a')
        b_ref = self.load_fasta_file(b_path, 'test_assembly_b')
        query_refs = [a_ref, b_ref]
        reference_refs = [b_ref, a_ref]
        results = self.getImpl().fast_ani(self.getContext(), {
            'workspace_name': self.getWsName(),
            'query_assembly_refs': query_refs,
            'reference_assembly_refs': reference_refs
        })
        self.assertTrue(len(results[0]['report_name']))
        self.assertTrue(len(results[0]['report_name']))
        return

    def test_invalid_refs(self):
        '''
        Test invalid data types
        '''
        # TODO
        # The below test is not useful as it just throws an AssemblyUtil exception
        # a_path = self.scratch + '/a_empty.fna'
        # b_path = self.scratch + '/b_empty.fna'
        # open(a_path, 'a').close()
        # open(b_path, 'a').close()
        # query_assembly = self.load_fasta_file(a_path, 'test_query')
        # reference_assembly = self.load_fasta_file(b_path, 'reference_assembly')
        # results = self.getImpl().fast_ani(self.getContext(), {
        #     'workspace_name': self.getWsName(),
        #     'query_assembly': query_assembly,
        #     'reference_assembly': reference_assembly
        # })
        # print(results)
        # return

    def test_assembly_set(self):
        '''
        Test the output data when running on multiple queries and references
        '''
        # TODO
        # a_path = self.scratch + '/a.fna'
        # copyfile(TEST_FILE_1, a_path)
        # query_assembly = self.load_fasta_file(a_path, 'test_query')
        pass
