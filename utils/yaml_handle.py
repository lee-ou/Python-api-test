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


def write_extract(data: dict):
    """
    Write YAML file with given data and return it as a dictionary with key as key and value as value
    :param data: 需要写入的数据
    :return:
    """
    with open('extract.yaml', mode='a+', encoding='utf-8') as file:
        yaml.dump(file, data, default_flow_style=False)


def clear_extract():
    """
    Clear YAML file
    :return:
    """
    with open('extract.yaml', mode='w', encoding='utf-8') as file:
        file.truncate()


def get_sorted_yaml_files():
    """
    获取指定目录及其子目录下所有.yaml/.yml文件路径，并排序
    :return: 排序后的文件路径列表
    """
    yaml_files = []

    # 遍历目录树
    for root, _, files in os.walk('datas'):
        for file in files:
            if file.lower().endswith(('.yaml', '.yml')):
                # 拼接完整路径
                full_path = os.path.join(root, file)
                yaml_files.append(full_path)

    # 按文件名排序
    yaml_files.sort()
    return yaml_files
