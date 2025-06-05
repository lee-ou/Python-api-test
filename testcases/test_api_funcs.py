import os

import pytest
import logging

from utils.yaml_handle import get_sorted_yaml_files, get_cases_data

logger = logging.getLogger(__name__)


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
        logger.info(info)

    return funcs


for file_path in get_sorted_yaml_files():
    file_name = os.path.basename(file_path).replace('.yaml', '')
    setattr(TestApiFuncs, f'test_{file_name}', create_test_funcs(file_path))
