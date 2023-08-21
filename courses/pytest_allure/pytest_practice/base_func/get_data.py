import os
import yaml


def get_data(file, name, level):
    path = get_abpath(file)
    with open(path, encoding='utf-8') as f:
        result = yaml.safe_load(f)
    data = result.get(name).get(level).get('data')
    ids = result.get(name).get(level).get('ids')
    return data, ids

def get_abpath(file):
    cur_path = os.path.abspath(__file__)
    pro_path = os.path.dirname(cur_path)
    data_path = file
    final = os.path.abspath(os.path.join(pro_path, '../data', data_path))
    return final

# print(get_data('../data/data.yml', 'add', 'P1'))
# get_abpath('data.yml')
print(get_data('data.yml', 'add', 'P1'))