import yaml
import json

from yaml.loader import BaseLoader

def load_yaml_into_pyhton(filepath):
    with open(filepath,'r') as file_to_read:
        dict_of_yaml_file = yaml.load(file_to_read, Loader=BaseLoader)

    return dict_of_yaml_file

def load_yaml_into_json(yaml_filepath, json_filepath):
    dict_of_data = load_yaml_into_pyhton(yaml_filepath)

    with open(json_filepath, 'w') as file_to_write:
        json.dump(dict_of_data, file_to_write)


if __name__ == '__main__':
    load_yaml_into_json('verify.yaml','verify.json')
    load_yaml_into_json('xmas.yaml','xmas.json')   