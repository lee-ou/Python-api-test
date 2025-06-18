import glob
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


def get_cases_data(yaml_path):
    """
    Read YAML file with given path and return it as a dictionary
    :param yaml_path: 文件路径
    :return: 数据
    """
    with open(yaml_path, 'r', encoding='utf-8') as file:
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
    获取datas目录下所有子目录中的yaml文件路径(排序完成的文件)
    :return: 排序后的yaml文件路径列表
    """
    return sorted(glob.glob('./datas/**/*.y*ml') + glob.glob('./datas/*.yaml'))
