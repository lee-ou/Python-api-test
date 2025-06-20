import requests
import logging

from utils.yaml_handle import read_config, write_extract

logger = logging.getLogger(__name__)


class UserAuth:

    def __init__(self):
        self._user_email = read_config('BaseConfig', 'test_email')

    def _get_msg_code(self):
        url = 'https://mid-api-test.channelwill.com/mid-admin/v1/auth/login-code'
        data = {'email': self._user_email}
        resp = requests.post(url, json=data).json()
        return resp['data']['code']

    def get_auth_code(self):
        try:
            code = self._get_msg_code()
            url = 'https://mid-api-test.channelwill.com/mid-admin/v1/auth/login'
            data = {'code': code, 'email': self._user_email}
            resp = requests.post(url, json=data).json()
            token = resp['data']['access_token']
            write_extract({'Authorization': f'Bearer {token}'})
            logger.info(f'鉴权码获取成功')
        except Exception as e:
            logger.error(f'鉴权码获取失败，失败原因：{e}')
