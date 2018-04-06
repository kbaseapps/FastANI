import os

# Construct some pretty-ish output for FastANI


def get_result_data(output_paths):
    '''
    Create a list of objects of all the result data from running fastani
    '''
    result_data = []
    print('OUTPUT PATHS', output_paths)
    for path in output_paths:
        with open(path) as file:
            contents = file.read()
            parts = contents[:-1].split(" ")
            if len(parts) == 5:
                result_data.append({
                    'query_path': parts[0],
                    'reference_path': parts[1],
                    'percentage_match': parts[2],
                    'orthologous_matches': parts[3],
                    'total_fragments': parts[4],
                    'viz_path': path + '.visual.pdf'
                })
            else:
                print('Invalid result:', contents)
    return result_data


def create_html_tables(result_data):
    '''
    For each result, create an html table for it
    '''
    headers = ['Query', 'Reference', 'ANI Estimate', 'Orthologous Matches', 'Total Fragments']
    rows = []
    for result in result_data:
        row = [
            os.path.basename(result['query_path']),
            os.path.basename(result['reference_path']),
            result['percentage_match'],
            result['orthologous_matches'],
            result['total_fragments']
        ]
        rows.append(__join_with_dom_tag('td', row))
    html = "<table><thead><tr>"
    # Insert the headers
    html += __join_with_dom_tag('th', headers)
    html += "</tr></thead><tbody>"
    # Insert the rows
    html += __join_with_dom_tag('tr', rows)
    html += "</tbody></table>"
    return html


def __join_with_dom_tag(tag, list):
    '''
    Wrap an array of strings into tags.
    eg. __join_with_dom_tag('td', ['x', 'y']) -> "<td>x</td><td>y</td>"
    '''
    open_tag = "<" + tag + ">"
    end_tag = "</" + tag + ">"
    join_with = end_tag + open_tag  # eg. </tr><tr>
    return open_tag + join_with.join(list) + end_tag
