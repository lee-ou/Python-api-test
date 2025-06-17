import copy
import re
import logging
import jsonpath
from typing import Any

from utils.yaml_handle import write_extract

logger = logging.getLogger(__name__)
# 保存变量类型映射字典
SAVE_TYPE_DICT = {
    'json': lambda resp, save_expr, index: jsonpath.jsonpath(resp, save_expr)[index],
    'text': lambda resp, save_expr, index: re.findall(save_expr, resp.text)[index],
    'attr': lambda resp, save_expr: getattr(resp, save_expr)
}


def save_var(resp: Any, extract: dict) -> bool:
    """
    缓存中间变量（接口关联参数）
    :param resp: 响应对象
    :param extract: 缓存表达式
    :return:
    """
    new_resp = copy.deepcopy(resp)
    new_resp.json = new_resp.json()
    try:
        for var_name, value in extract.items():
            logger.warning(f'正在缓存变量： {var_name} | {value}')
            save_type, save_expr, index = value
            if save_type not in ('json', 'text'):
                save_type = 'attr'
            if index in (None, ''):
                index = 0
            save_var_func = SAVE_TYPE_DICT.get(save_type)
            var_value = save_var_func(new_resp, save_expr, index)
            write_extract({var_name: var_value})
        return True
    except Exception as e:
        logger.error(f'变量保存失败，失败原因：{e}')
