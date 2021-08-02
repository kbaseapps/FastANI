import os
import subprocess
import tempfile
import time
import unittest
from configparser import ConfigParser  # py3
from os import environ

from FastANI.FastANIImpl import FastANI
from FastANI.FastANIServer import MethodContext
from FastANI.authclient import KBaseAuth as _KBaseAuth
from installed_clients.AssemblyUtilClient import AssemblyUtil
from installed_clients.WorkspaceClient import Workspace as workspaceService


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
        cls.ctx.update(
            {
                'token': token,
                'user_id': user_id,
                'provenance': [
                    {
                        'service': 'FastANI',
                        'method': 'please_never_use_it_in_production',
                        'method_params': [],
                    }
                ],
                'authenticated': 1,
            }
        )
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
        wsName = 'test_FastANI_' + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    def load_fasta_file(self, path, name):
        assembly_util = AssemblyUtil(self.callback_url)
        return assembly_util.save_assembly_from_fasta(
            {
                'file': {'path': path},
                'workspace_name': self.getWsName(),
                'assembly_name': name,
            }
        )

    def test_fastani_binary(self):
        """
        Run the compiled binary using the given example data
        This only tests that fastANI has installed and runs correctly
        it does not test any python wrapping
        """
        tmp_dir = tempfile.mkdtemp()
        out_path = os.path.join(tmp_dir, 'fastani.out')
        data_dir = os.path.join(os.path.dirname(__file__), 'data')
        test_file_1 = os.path.join(data_dir, 'shigella.fna')
        test_file_2 = os.path.join(data_dir, 'ecoli.fna')
        args = ['fastANI', '-q', test_file_1, '-r', test_file_2, '-o', out_path]
        subprocess.call(args)
        self.assertTrue(os.path.isfile(out_path))

    def test_run_fast_ani(self):
        """
        Test a run of the full FastANIImpl function using several assembly/genome refs.
        """

        # CANNOT BE RUN -- ws is deleted/inaccessible?
        assembly_id1 = '34819/10/1'
        genome_id1 = '34819/14/1'
        genome_id2 = '34819/13/1'
        genome_id3 = '34819/3/2'
        results = self.getImpl().fast_ani(
            self.getContext(),
            {
                'workspace_name': self.getWsName(),
                'reference': [assembly_id1, genome_id1],
                'query': [genome_id2, genome_id3],
            },
        )
        print('Results:', results)
        self.assertTrue(len(results[0]['report_name']))
        self.assertTrue(len(results[0]['report_ref']))
