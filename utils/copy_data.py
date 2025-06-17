import copy


def copy_data(data):
    """
    使用深拷贝复制一个新的数据
    :param data:
    :return:
    """
    new_data = copy.deepcopy(data)
    new_data.json = new_data.json()
    return new_data
