import logging

from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class Module:
    """用例格式模版"""
    module: dict
    title: dict
    request: dict

    extract: dict = None
    validate: dict = None


def verfiy_module(caseinfo):
    """
    格式校验
    :param caseinfo: 用例数据
    :return: 返回其本身
    """
    try:
        Module(**caseinfo)
        return caseinfo
    except Exception as e:
        logger.info(f'用例不符合模版格式要求，{e}')
