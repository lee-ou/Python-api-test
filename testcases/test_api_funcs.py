import glob
import os
import allure
import pytest
import logging
from commons.cases import excute_cases
from utils.yaml_handle import find_file_path, get_sorted_yaml_files, get_cases_data, read_config

logger = logging.getLogger(__name__)
title = read_config('REPORT', 'title')
case_filter = read_config('BaseConfig', 'run_case_filter')
TEST_FLAG = 0
TEST_FLAG_DICT = {
    0: '识别到需要执行全部测试用例',
    1: '识别到仅执行单个指定测试用例',
    2: '识别到仅执行多个指定测试用例'
}
    

@allure.epic(title)
class TestApiFuncs:
    pass


def create_test_funcs(path):
    """
    创建测试用例
    :param path: 测试用例文件路径
    :return: 测试用例（方法）
    """

    @pytest.mark.parametrize('case_info', get_cases_data(path))
    def funcs(self, case_info):
        logger.info('===========================开始执行===========================')
        excute_cases(case_info)
        logger.info('===========================执行完成===========================\n')

    return funcs




if case_filter == 'ALL':
    TEST_FLAG = 0
    logger.info(TEST_FLAG_DICT.get(TEST_FLAG))
    for file_path in get_sorted_yaml_files():
        file_name = os.path.basename(file_path).replace('.yaml', '')
        setattr(TestApiFuncs, f'test_{file_name}', create_test_funcs(file_path))
else:
    if ',' not in case_filter:
        TEST_FLAG =1
        logger.info(f'{TEST_FLAG_DICT.get(TEST_FLAG)}: {case_filter}')
        case_path = find_file_path(case_filter)
        setattr(TestApiFuncs, f'test_{case_filter}', create_test_funcs(case_path))
    else:
        TEST_FLAG = 2
        logger.info(f'{TEST_FLAG_DICT.get(TEST_FLAG)}: {case_filter}')
        for case_name in case_filter.split(','):
            case_path = find_file_path(case_name)
            setattr(TestApiFuncs, f'test_{case_name}', create_test_funcs(case_path))
