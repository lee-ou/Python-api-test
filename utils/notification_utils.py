import logging
import requests

from utils.yaml_handle import read_config

logger = logging.getLogger(__name__)
title = read_config('REPORT', 'title')
config = read_config('DingTalk_RobotNotice')


class RobotNotice:
    """钉钉群机器人通知"""

    def __init__(self, report_url=None):
        self.sub = title
        self.access_token = config.get('webhook_token')
        self.at_mobiles = config.get('mobile')  # 默认要@的用户手机号列表
        self.report_url = report_url or "未提供报告地址"

    def _msg_text(self, data):
        """生成通知文本内容"""
        try:
            total = int(data['total'])
            passed = int(data['passed'])
            skipped = int(data['skipped'])
            failed = int(data['failed'])
            error = int(data['error'])
            success_rate = round(((passed + skipped) / total) * 100, 2) if total > 0 else 0
            at_mobiles_str = ' '.join([f'@{mobile}' for mobile in self.at_mobiles])
            content_text = (
                f"家长们，UI自动化跑完啦！\n"
                f"用例运行总数:  {total} 个\n"
                f"通过用例个数:  {passed} 个\n"
                f"失败用例个数:  {failed} 个\n"
                f"异常用例个数:  {error} 个\n"
                f"跳过用例个数:  {skipped} 个\n"
                f"成功率:  {success_rate} %\n"
                f"--------------------------------------------\n"
                f"说明：成功率=(通过数+跳过数)/总用例数\n"
                f"测试报告地址：{self.report_url}\n"
                f"详细情况可通过访问测试报告链接查看，谢谢！\n"
                f"{at_mobiles_str}"
            )
            return content_text

        except (KeyError, ValueError) as e:
            logger.error(f"生成通知文本时发生错误: {e}")
            return f"{title}生成失败，数据有误。"

    def send_dingtalk_msg(self, result_data: dict, is_at_all=False) -> bool:
        """
        发送钉钉群聊通知
        :param result_data:
        :param is_at_all: 是否@所有人，默认为False
        :return: 发送是否成功
        """
        webhook_url = f'https://oapi.dingtalk.com/robot/send?access_token={self.access_token}'
        headers = {'Content-Type': 'application/json'}
        payload = {
            "msgtype": "text",
            "text": {
                "content": self._msg_text(result_data)
            },
            "at": {
                "atMobiles": self.at_mobiles,
                "isAtAll": is_at_all
            }
        }

        try:
            response = requests.post(webhook_url, json=payload, headers=headers, timeout=10)
            response_data = response.json()

            if response.status_code == 200 and response_data.get("errcode") == 0:
                logger.info("钉钉通知发送成功")
                return True
            else:
                logger.error(f"钉钉通知发送失败: {response_data.get('errmsg', '未知错误')}")
                return False

        except requests.RequestException as e:
            logger.error(f"钉钉通知发送失败，网络请求异常: {e}")
            return False
