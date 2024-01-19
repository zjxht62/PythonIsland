import yaml
def load_yaml():
    with open('colums_conf.yaml') as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def get_all_from_columns():
    from_columns_list = []
    confs = load_yaml()
    for conf in confs:
        from_columns_list.extend(conf['from'])
    return from_columns_list

if __name__ == '__main__':
    print(load_yaml())
