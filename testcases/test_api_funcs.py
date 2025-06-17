import os

import allure
import pytest
import logging

from commons.cases import excute_cases
from utils.yaml_handle import get_sorted_yaml_files, get_cases_data, read_config

logger = logging.getLogger(__name__)
title = read_config('REPORT', 'title')


@allure.epic(title)
class TestApiFuncs:
    pass


def create_test_funcs(data):
    """
    Create test functions using
    :param data: 测试用例文件路径
    :return: 测试用例（方法）
    """

    @pytest.mark.parametrize('info', get_cases_data(data))
    def funcs(self, info):
        logger.info('===========================开始执行===========================')
        excute_cases(info)
        logger.info('===========================执行完成===========================\n')

    return funcs


for file_path in get_sorted_yaml_files():
    file_name = os.path.basename(file_path).replace('.yaml', '')
    setattr(TestApiFuncs, f'test_{file_name}', create_test_funcs(file_path))
