import logging
import allure
from commons.all_requests import request_client
from commons.assert_cases import assert_cases
from commons.module import verfiy_module
from commons.replace_template import replace_data
from commons.save_extract import save_var

logger = logging.getLogger(__name__)


def excute_cases(case_info: dict) -> None:
    """
    执行测试用例方法
    :param case_info: 用例数据
    :return:
    """
    allure.title(case_info.get('module'))
    allure.description(case_info.get('title'))

    logger.info(f"执行用例：{case_info.get('module')}==>{case_info.get('title')}")
    new_case_info = replace_data(verfiy_module(case_info))
    try:
        resp = request_client.send_request(**new_case_info.get('request'))
        extract = new_case_info.get('extract')
        validate = new_case_info.get('validate')
        if extract:
            logger.info(extract)
            save_var(resp,extract)

        if validate:
            assert_cases(resp, validate)
    except Exception as e:
        logger.error(f'用例执行失败：{e}')
        raise e
