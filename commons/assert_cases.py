import logging
import re
import jsonpath
from typing import Any, Dict

from utils.copy_data import copy_data

logger = logging.getLogger(__name__)

# 断言类型映射字典，支持扩展添加新的断言类型
ASSERT_TYPE_DICT = {
    'contain': lambda expected, actual: expected in actual,
    'equal': lambda expected, actual: expected == actual,
    'not_contain': lambda expected, actual: expected not in actual,
    'not_equal': lambda expected, actual: expected != actual,
    'db_assert': ''
}


def assert_cases(resp: Any, validate: Dict[str, Any]) -> bool:
    """
    执行多种断言验证
    :param resp: 响应对象
    :param validate: 断言规则字典，如 {'equal': {'status': 200}}
    :return: bool 所有断言是否通过
    """
    new_resp = copy_data(resp)
    try:
        for assert_type, assert_value in validate.items():
            logger.info(f'使用{assert_type}断言，断言参数：{assert_value}')
            assert_type_func = ASSERT_TYPE_DICT.get(assert_type, None)
            if not assert_type_func:
                logger.error(f"不支持的断言类型: {assert_type}")
                return False
            expected, extract_type, expression, index = assert_value
            if index in (None, ''):
                index = 0
            if extract_type == 'json':
                actual = jsonpath.jsonpath(new_resp, expression)[index]
            elif extract_type == 'text':
                actual = re.findall(expression, new_resp.text)[index]
            else:
                actual = getattr(new_resp, extract_type)
            assert_type_func(expected, actual) if actual else logger.warning(f"实际结果：{actual} 为空")
        logger.info('断言通过')
    except Exception as e:
        logger.error(f"断言失败: {e}")
        return False
