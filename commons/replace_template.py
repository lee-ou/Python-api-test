import json
import re
import logging

from commons.hot_loads import HotLoads

logger = logging.getLogger(__name__)


def replace_data(resp):
    replace_expr = '\\$\\{(.*?)\\((.*?)\\)\\}'
    str_resp = json.dumps(resp)
    new_str_resp = ''

    if '${' in str_resp and '}' in str_resp:
        result_list = re.findall(replace_expr, str_resp)
        for func_info in result_list:
            func_name, func_args = func_info
            old_value = '${' + func_name + '(' + func_args + ')}'
            if func_args == '':
                new_value = getattr(HotLoads(), func_name)()
            elif ',' in func_args:
                new_value = getattr(HotLoads(), func_name)(*func_args.split(','))
            else:
                new_value = getattr(HotLoads(), func_name)(func_args)
            new_str_resp = str_resp.replace(old_value, new_value)
    new_resp = json.loads(new_str_resp, strict=False)

    return new_resp
