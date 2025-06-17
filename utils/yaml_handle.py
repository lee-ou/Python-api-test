import os

import yaml


def read_extract_file(key):
    """
    Read YAML file with given key and return it as a dictionary
    :param key: 目标值名称
    :return: 目标值
    """
    with open('extract.yaml', mode='r', encoding='utf-8') as file:
        return yaml.safe_load(file)[key]


def get_cases_data(path):
    """
    Read YAML file with given path and return it as a dictionary
    :param path: 文件路径
    :return: 数据
    """
    with open(path, mode='r', encoding='utf-8') as file:
        return yaml.safe_load(file)


def read_config(node, key=None):
    with open('config/config.yaml', mode='r', encoding='utf-8') as file:
        if key:
            return yaml.safe_load(file)[node][key]
        return yaml.safe_load(file)[node]


def write_extract(data: dict):
    """
    Write YAML file with given data and return it as a dictionary with key as key and value as value
    :param data: 需要写入的数据
    :return:
    """
    with open('extract.yaml', mode='a+', encoding='utf-8') as file:
        yaml.dump(file, data, default_flow_style=False)


def get_sorted_yaml_files():
    """
    获取datas目录下所有子目录中的yaml文件路径
    先对子目录排序，再对每个子目录下的文件排序
    
    参数:
        datas_dir: 数据目录路径
        
    返回:
        排序后的yaml文件路径列表
    """
    yaml_paths = []

    # 获取所有子目录并排序
    subdirs = [d for d in os.listdir('./datas')
               if os.path.isdir(os.path.join('./datas', d))]
    subdirs.sort()

    # 遍历每个子目录
    for subdir in subdirs:
        subdir_path = os.path.join('./datas', subdir)

        # 获取子目录下所有yaml文件并排序
        files = [f for f in os.listdir(subdir_path)
                 if f.endswith(('.yaml', '.yml'))]
        files.sort()

        # 添加完整路径到结果列表
        for file in files:
            yaml_paths.append(os.path.join(subdir_path, file))

    return yaml_paths
