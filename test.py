import json
import re
from bs4 import BeautifulSoup


def clean_beauty(line):
    soup = BeautifulSoup(line, 'html.parser')
    if ':' in line:
        return soup.get_text().split(':')[1].strip()
    else:
        return soup.get_text().strip()


with open('UnitTestDataLarger.json') as f:
    data = json.load(f)['DATA']['A']

output = []

for item in data:
    definition = ""
    sub_definitions = []
    cur_list = []
    cur_term = {}
    main_definition = ""
    f = 0
    for paragraph in item['body'].split('dd>')[1].split('<br>'):
        current_sub_def = {}
        text = paragraph.strip().encode('ascii', 'ignore').decode()
        par = re.sub(r'<i>.*?</i>', '', text)
        if len(par) < 4:
            continue
        if par.startswith('<b>'):
            if par.endswith("</b>"):
                if cur_term:
                    if cur_list:
                        cur_term['sub_definitions'].append(cur_list)
                        cur_list = []
                    sub_definitions.append(cur_term)
                    cur_term = {}

                cur_term = {"term": clean_beauty(par), "definition": "", "sub_definitions": []}
                f = 't'
            elif re.match(r'[1-9]', par[3]):
                if f == 'a':
                    sub_definitions.append(cur_list)
                    cur_list = []
                current_sub_def['definition'] = clean_beauty(par)
                sub_definitions.append(current_sub_def)
                f = 1

            elif re.match(r'[a-z]', par[3]):
                if f == 1 or f == 't' or f == ':':
                    cur_list = []
                    current_sub_def['definition'] = clean_beauty(par)
                    cur_list.append(current_sub_def)
                    f = 'a'

                elif f == 'a':
                    current_sub_def['definition'] = clean_beauty(par)
                    cur_list.append(current_sub_def)
            elif par.startswith('<b>:</b>'):
                definition = clean_beauty(par)
                if f == 't' or f == 1:
                    if not cur_term:
                        cur_term = {'definition': '', 'sub_definitions': []}
                    cur_term['definition'] = definition
                    f = ':'
                elif f == ':':
                    if not cur_term:
                        cur_term = {'definition': '', 'sub_definitions': []}
                    cur_term['sub_definitions'].append({'definition': cur_term['definition']})
                    cur_term['sub_definitions'].append({'definition': definition})
                    cur_term['definition'] = ''
                else:
                    main_definition = definition
                    f = ':'
    if cur_list:
        sub_definitions.append(cur_list)
    if cur_term:
        sub_definitions.append(cur_term)
    term = item['title']
    output.append({
        "term": term,
        "definition": clean_beauty(main_definition),
        "sub_definitions": sub_definitions
    })


with open('Outcome1.json', 'w') as f:
    json.dump(output, f, indent=4)