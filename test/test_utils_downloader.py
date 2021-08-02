import unittest
import utils.downloader as downloader
import os
import shutil

QUERY = downloader.QUERY
REF = downloader.REF

scratch = '/kb/module/test/scratch_dir'
REFS = {
    'A': '123/4/5',
    'B': '234/5/6',
    'C': '345/6/7',
    'D': '456/7/8',
}


class TestDownloader(unittest.TestCase):
    def test_dedupe_input__no_valid_ids(self):

        test_input = [
            {
                'err_str': QUERY,
                'input': {QUERY: [None, '', None, None], REF: [REFS['A']]},
            },
            {
                'err_str': REF,
                'input': {
                    QUERY: [REFS['A'], REFS['A'], REFS['A']],
                    REF: ['', '', '', ''],
                },
            },
            {
                'err_str': QUERY + ' or ' + REF,
                'input': {QUERY: [None, '', None, None], REF: ['', '', '', '']},
            },
        ]

        for test in test_input:
            with self.assertRaisesRegexp(
                ValueError, f'No valid inputs found in {test["err_str"]} set'
            ):
                downloader.dedupe_input(test['input'])

    def test_dedupe_input__ids_in_both(self):
        test_input = [
            {
                'err_arr': [REFS['A']],
                'input': {QUERY: [REFS['A'], None, ''], REF: ['', None, REFS['A']]},
            },
            {
                'err_arr': [REFS['B']],
                'input': {
                    QUERY: [REFS['A'], None, None, REFS['B']],
                    REF: [REFS['B'], REFS['B'], REFS['C'], REFS['B']],
                },
            },
            {
                'err_arr': [REFS['A'], REFS['B'], REFS['C']],
                'input': {
                    QUERY: [REFS['A'], REFS['B'], REFS['C']],
                    REF: [REFS['C'], REFS['B'], REFS['A']],
                },
            },
        ]

        for test in test_input:
            with self.assertRaisesRegexp(
                ValueError,
                'IDs found in query and reference sets:\n' + '\n'.join(test['err_arr']),
            ):
                downloader.dedupe_input(test['input'])

    def test_dedupe_input__ok(self):
        test_input = [
            {
                'input': {QUERY: [REFS['A'], REFS['B']], REF: [REFS['C'], REFS['D']]},
                'output': {
                    QUERY: set([REFS['A'], REFS['B']]),
                    REF: set([REFS['C'], REFS['D']]),
                    'all': set([REFS['A'], REFS['B'], REFS['C'], REFS['D']]),
                },
            },
            {
                'input': {
                    QUERY: [
                        None,
                        '',
                        REFS['A'],
                        None,
                        None,
                        '',
                        REFS['B'],
                        REFS['B'],
                        REFS['A'],
                        REFS['B'],
                    ],
                    REF: [
                        REFS['C'],
                        REFS['C'],
                        REFS['C'],
                        REFS['C'],
                        REFS['D'],
                        REFS['C'],
                        REFS['C'],
                        REFS['C'],
                        REFS['C'],
                    ],
                },
                'output': {
                    QUERY: set([REFS['A'], REFS['B']]),
                    REF: set([REFS['C'], REFS['D']]),
                    'all': set([REFS['A'], REFS['B'], REFS['C'], REFS['D']]),
                },
            },
        ]

        for test in test_input:
            self.assertEqual(downloader.dedupe_input(test['input']), test['output'])

    def check_file_contents(self, new_file, ref_text):

        with open(new_file, 'r') as f:
            rendered_text = f.read()
            self.assertMultiLineEqual(rendered_text.rstrip(), '\n'.join(ref_text))

    def run_dump_paths_to_file(self, output_dir):

        # ensure the output dir no longer exists
        shutil.rmtree(output_dir, ignore_errors=True)
        self.assertFalse(os.path.isdir(output_dir))

        paths = {QUERY: ['this', 'that', 'the other'], REF: ['wherever', 'whenever']}

        for input_type in [QUERY, REF]:
            output_file = os.path.join(scratch, input_type + '.txt')
            self.assertFalse(os.path.isfile(output_file))

        output_files = downloader.dump_paths_to_file(paths, scratch)
        for input_type in [QUERY, REF]:
            self.check_file_contents(output_files[input_type], paths[input_type])

    def test_dump_paths_to_file__ok(self):
        self.run_dump_paths_to_file(scratch)

    def test_dump_paths_to_file__create_intermed_dirs(self):
        # ensure that we can create intervening directories
        output_dir = os.path.join(scratch, 'path', 'to', 'new', 'dir')
        self.run_dump_paths_to_file(output_dir)


if __name__ == '__main__':
    unittest.main()
