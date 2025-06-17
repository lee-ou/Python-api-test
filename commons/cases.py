import logging
import allure
from commons.all_requests import request_client
from commons.assert_cases import assert_cases
from commons.module import verfiy_module
from commons.save_extract import save_var

logger = logging.getLogger(__name__)


def excute_cases(info: dict) -> None:
    """
    执行测试用例方法
    :param info: 用例数据
    :return:
    """
    allure.title(info.get('module'))
    allure.description(info.get('title'))

    logger.info(f"执行用例：{info.get('module')}==>{info.get('title')}")
    info = verfiy_module(info)
    try:
        resp = request_client.send_request(**info.get('request'))
        extract = info.get('extract')
        validate = info.get('validate')
        if extract:
            logger.info(extract)
            save_var(resp,extract)

        if validate:
            assert_cases(resp, validate)
    except Exception as e:
        logger.error(f'用例执行失败：{e}')
        raise e
