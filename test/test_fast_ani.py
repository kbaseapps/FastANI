import os
import sys
import unittest
dirname = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(dirname, '../lib/FastANI/')))

from fast_ani_output import get_result_data, create_html_tables  # noqa
from fast_ani_proc import run_fast_ani_pairwise  # noqa

# Test the fastANI python utilites in /lib/FastANI


class TestFastANI(unittest.TestCase):

    def test_fast_ani_proc_and_output(self):
        dir = os.path.abspath(dirname + '/../data')
        path1 = os.path.join(dir, 'shigella.fna')
        path2 = os.path.join(dir, 'ecoli.fna')
        out_paths = run_fast_ani_pairwise('/tmp', [path1, path2])
        self.assertEqual(set(out_paths), set([
            '/tmp/ecoli-ecoli.out',
            '/tmp/ecoli-shigella.out',
            '/tmp/shigella-ecoli.out',
            '/tmp/shigella-shigella.out'
        ]))
        result_data = get_result_data(out_paths)
        print(result_data)
        self.assertEqual(len(result_data), 4)
        self.assertEqual(result_data[0]['orthologous_matches'], '1603')
        self.assertEqual(result_data[0]['percentage_match'], '100')
        self.assertEqual(result_data[0]['total_fragments'], '1608')
        table_data = create_html_tables(result_data)
        expected_table = "<table><thead><tr><th>Query</th><th>Reference</th><th>ANI Estimate</th><th>Orthologous Matches</th><th>Total Fragments</th></tr></thead><tbody><tr><td>shigella.fna</td><td>shigella.fna</td><td>100</td><td>1603</td><td>1608</td></tr><tr><td>shigella.fna</td><td>ecoli.fna</td><td>97.7443</td><td>1305</td><td>1608</td></tr><tr><td>ecoli.fna</td><td>shigella.fna</td><td>97.6765</td><td>1324</td><td>1547</td></tr><tr><td>ecoli.fna</td><td>ecoli.fna</td><td>100</td><td>1547</td><td>1547</td></tr></tbody></table>"  # noqa
        self.assertEqual(table_data, expected_table)


if __name__ == '__main__':
    unittest.main()
