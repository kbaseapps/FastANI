import os
import uuid
from DataFileUtil.DataFileUtilClient import DataFileUtil
from KBaseReport.KBaseReportClient import KBaseReport

# This module handles creating a KBase report object from fast_ani_output html


def create_report(callback_url, scratch, workspace_name, html):
    '''
    Create KBase extended report object for the output html
    '''
    dfu = DataFileUtil(callback_url)
    report_name = 'fastANI_report_' + str(uuid.uuid4())
    report_client = KBaseReport(callback_url)
    html_folder = os.path.join(scratch, report_name)
    os.mkdir(html_folder)
    with open(os.path.join(html_folder, "index.html"), 'w') as file:
        file.write(html)
    shock = dfu.file_to_shock({
        'file_path': html_folder,
        'make_handle': 0,
        'pack': 'zip'
    })
    html_files = [{
        'shock_id': shock['shock_id'],
        'name': 'index.html',
        'label': 'html_files',
        'description': 'FastANI HTML report'
    }]
    report = report_client.create_extended_report({
        'direct_html_link_index': 0,
        'html_links': html_files,
        'report_object_name': report_name,
        'workspace_name': workspace_name
    })
    return {
        'report_name': report['name'],
        'report_ref': report['ref']
    }
