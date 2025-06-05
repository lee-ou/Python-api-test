import os
import time
import logging

logger = logging.getLogger(__name__)


def generate_report():
    """
    生成测试报告
    :return:
    """
    try:
        report_file = os.path.join('./outputs/reports/', 'API-Report' + time.strftime("%Y%m%d%H%M"))
        os.makedirs(report_file)
        os.system("allure generate ./temps -o " + report_file)
    except Exception as e:
        logger.error(f'测试报告生成失败，失败原因：{e}')
