import json
import yaml


def load_json_into_python(filepath):
    json_file = open(filepath,'r')
    dict_of_json_file = json.load(json_file)
    json_file.close()
    return dict_of_json_file


def load_json_into_yaml(json_filepath,yaml_filepath):
    #open yaml file
    #make yaml file?
    
    dict_of_data = load_json_into_python(json_filepath)
    
    with open(yaml_filepath, 'w') as file_descriptor:
        yaml.dump(dict_of_data, file_descriptor)


if __name__ == '__main__':
    load_json_into_yaml('donuts.json','donuts.yaml')
    load_json_into_yaml('emojis.json','emojis.yaml')







