import yaml


def get_add_data():
    with open('../data/add_data.yml', encoding='utf-8') as f:
        result = yaml.safe_load(f)
    return result


def get_div_data():
    with open('../data/div_data,yml', encoding='utf-8') as f:
        result = yaml.safe_load(f)
    return result