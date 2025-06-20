import glob
import yaml
import os


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
    将提取的数据写入到extract.yaml文件中
    :param data: 需要写入的数据
    :return:
    """
    with open('extract.yaml', mode='a+', encoding='utf-8') as file:
        yaml.safe_dump(data, file, default_flow_style=False)


def get_sorted_yaml_files():
    """
    获取datas目录下所有子目录中的yaml文件路径(排序完成的文件)
    :return: 排序后的yaml文件路径列表
    """
    return sorted(glob.glob('./datas/**/*.y*ml') + glob.glob('./datas/*.yaml'))



def find_file_path(target_basename):
    """
    根据无后缀文件名查找完整文件路径
    参数:
        target_basename: 目标文件名(不带后缀)
    返回:
        匹配文件的完整路径，未找到返回None
    """
    for root, dirs, files in os.walk('./datas'):
        for filename in files:
            # 分离文件名和后缀
            basename, ext = os.path.splitext(filename)
            if basename == target_basename:
                return os.path.join(root, filename)
    return None