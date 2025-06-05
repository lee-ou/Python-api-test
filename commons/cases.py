import logging

import allure

from commons.all_requests import request_client
from commons.module import verfiy_module

logger = logging.getLogger(__name__)


def excute_cases(info):
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
        resp = request_client.send_request(**info['request'])

        if info['extract']:
            pass

        if info['validate']:
            pass
    except Exception as e:
        logger.error(f'用例执行失败：{e}')
