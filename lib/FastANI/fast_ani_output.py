# -*- coding: utf-8 -*-
import os
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('FastANI', 'templates'),
    autoescape=select_autoescape(['html'])
)

# Construct some pretty-ish output for FastANI


def get_result_data(output_paths):
    """
    Create a list of objects of all the result data from running fastani
    """
    result_data = []
    for path in output_paths:
        with open(path) as file:
            contents = file.read()
            parts = contents[:-1].split(" ")
            if len(parts) == 5:
                result_data.append({
                    'query_path': __filename(parts[0]),
                    'reference_path': __filename(parts[1]),
                    'percentage_match': parts[2],
                    'orthologous_matches': parts[3],
                    'total_fragments': parts[4],
                    'viz_path': path + '.visual.pdf',
                    'viz_filename': os.path.basename(path + '.visual.pdf')
                })
            else:
                print('Invalid result:', contents)
    result_data = sorted(result_data, key=lambda r: float(r['percentage_match']))
    return result_data


def create_file_links(result_data):
    """
    For each result, create a file link dict that can be used in the kbase report
    """
    files = []
    for result in result_data:
        path = result['viz_path']
        basename = os.path.basename(result['viz_path']).split('.')[0]
        files.append({
            'path': path,
            'name': basename,
            'label': result_data['query_assembly'] + '-' + result_data['reference_assembly'],
            'description': 'PDF visualization of ANI matches'
        })
    return files


def create_html_tables(result_data):
    """
    For each result, create an html table for it
    """
    headers = ['Query', 'Reference', 'ANI Estimate', 'Matches',
               'Total', 'Visualization']
    template = env.get_template('result_tables.html')
    return template.render(headers=headers, results=result_data)


def __filename(path):
    "Return the filename, without extension, of a full path"
    return os.path.splitext(os.path.basename(path))[0]
