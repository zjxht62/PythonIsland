import yaml
from path_util import get_config_path
def load_yaml(subject):
    print(subject.value)
    config_path = get_config_path('yaml_confs',f'colums_conf_{subject.value}.yaml')
    with open(config_path) as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def get_all_from_columns(subject):
    from_columns_list = []
    confs = load_yaml(subject)
    for conf in confs:
        from_columns_list.extend(conf['from'])
    return from_columns_list

if __name__ == '__main__':
    print(load_yaml())
