import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

from utils.yaml_handle import read_config

mail_config = read_config("SMTP")
title = read_config('REPORT', 'title')
logger = logging.getLogger(__name__)


class SendEmail:
    """发送邮件"""

    def __init__(self):  # 初始化邮箱服务器配置
        self.smtp_server = mail_config.get('smtp_server')
        self.smtp_port = mail_config.get('smtp_port')
        self.sender_email = mail_config.get('sender_email')
        self.sender_password = mail_config.get('sender_password')
        self.recipient_email = mail_config.get('recipient_email')
        self.sender = mail_config.get('sender')
        self.recipient = mail_config.get('recipient')

    def _email_body(self, data):
        """从HTML模板中加载邮件内容"""
        success_rate = round(((data.get('passed') + data.get('skipped')) / data.get('total')) * 100, 2)

        # 读取HTML模板文件
        template_path = os.path.join(os.path.dirname(__file__), 'email_template.html')
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()

        # 替换占位符
        email_body = template_content.replace("{{ total }}", f"{data.get('total')}") \
            .replace("{{ passed }}", f"{data.get('passed')}") \
            .replace("{{ failed }}", f"{data.get('failed')}") \
            .replace("{{ error }}", f"{data.get('error')}") \
            .replace("{{ skipped }}", f"{data.get('skipped')}") \
            .replace("{{ success_rate }}", f"{success_rate}%") \
            .replace('{{ passed_percent }}', f"{round((data.get('passed') / data.get('total')) * 100, 2)}%") \
            .replace('{{ failed_percent }}', f"{round((data.get('failed') / data.get('total')) * 100, 2)}%") \
            .replace('{{ error_percent }}', f"{round((data.get('error') / data.get('total')) * 100, 2)}%") \
            .replace('{{ skipped_percent }}', f"{round((data.get('skipped') / data.get('total')) * 100, 2)}%")
        return email_body

    def send_email(self, result_data):
        # 构建邮件内容
        msg = MIMEText(self._email_body(result_data), "html", "utf-8")
        msg["From"] = formataddr((self.recipient, self.sender_email))
        msg["To"] = formataddr((self.sender, self.recipient_email))
        msg["Subject"] = Header(title, "utf-8")
        try:
            # 连接邮件服务器并发送
            server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            server.login(self.sender_email, self.sender_password)
            response = server.sendmail(self.sender_email, [self.recipient_email], msg.as_string())
            if not response:
                logger.info("邮件发送成功！")
            else:
                logger.warning(f"邮件可能已发送，但服务器返回非预期响应: {response}")
        except Exception as e:
            logger.error(f"邮件发送失败，错误原因: {e}")
