import os

import allure
import pytest
import logging

from commons.cases import excute_cases
from utils.yaml_handle import get_sorted_yaml_files, get_cases_data

logger = logging.getLogger(__name__)


@allure.epic('XXX接口自动化测试报告')
class TestApiFuncs:
    pass


def create_test_funcs(data):
    """
    Create test functions using
    :param data: 测试用例文件路径
    :return: 测试用例（方法）
    """

    @pytest.mark.parametrize('info', get_cases_data(data))
    def funcs(self, info, request):
        excute_cases(info)

    return funcs


for file_path in get_sorted_yaml_files():
    file_name = os.path.basename(file_path).replace('.yaml', '')
    setattr(TestApiFuncs, f'test_{file_name}', create_test_funcs(file_path))
