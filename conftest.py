import datetime
import logging
import time
import pytest
from utils.clear_old_files import DataClearUtils
from utils.notification_utils import RobotNotice
from utils.send_email_utils import SendEmail
from utils.user_auth import UserAuth
from utils.yaml_handle import read_config

logger = logging.getLogger(__name__)
dd_switch = read_config('DingTalk_RobotNotice', 'switch')
smtp_switch = read_config('SMTP', 'switch')


@pytest.fixture(scope='session', autouse=True)
def handle_fixture():
    """
    执行测试全后置处理
    """
    # 前置操作
    DataClearUtils().data_clear()
    UserAuth().get_auth_code()
    yield
    # 后置操作
    pass


def pytest_configure(config):
    """设置日志文件名称，通过时间戳生成保存每次执行测试的日志文件"""
    new_log_file = f'./outputs/log/pytest-{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.log'
    config.option.log_file = new_log_file


def pytest_terminal_summary(terminalreporter):
    """收集测试结果数据"""
    passed = len(terminalreporter.stats.get("passed", []))
    failed = len(terminalreporter.stats.get("failed", []))
    skipped = len(terminalreporter.stats.get("skipped", []))
    error = len(terminalreporter.stats.get("error", []))
    total = passed + failed + skipped + error
    duration = round(time.time() - terminalreporter._sessionstarttime, 3)
    logger.info(f"执行用例数：{total}，通过：{passed}，失败：{failed}，跳过：{skipped}，错误：{error}，耗时：{duration}秒")
    data = {
        'total': total,
        'passed': passed,
        'failed': failed,
        'skipped': skipped,
        'error': error,
        'duration': duration
    }
    SendEmail().send_email(data) if dd_switch else logger.info('未开启发送邮件功能开关')
    RobotNotice().send_dingtalk_msg(data) if smtp_switch else logger.info('未开启钉钉通知功能开关')
