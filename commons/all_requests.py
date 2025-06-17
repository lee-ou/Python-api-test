import requests
import logging
from utils.yaml_handle import read_config

logger = logging.getLogger(__name__)


class AllRequests:
    """接口统一请求"""

    def __init__(self):
        self.sess = requests.session()

    def _prepare_files(self, files_dict: dict):
        """文件上传参数"""
        files = {}
        try:
            for name, path in files_dict.items():
                files[name] = open(path, 'rb')
            return files
        except Exception as e:
            logger.error(f"文件打开失败: {e}")
            raise e

    def send_request(self, **kwargs):
        """接口请求"""
        try:
            if 'files' in kwargs.keys():
                kwargs['files'] = self._prepare_files(kwargs['files'])

            for key, value in kwargs.items():
                logger.info(f'请求{key}参数: {value}')

            resp = self.sess.request(**kwargs)
            logger.info(f'接口响应时间：{resp.elapsed}')
            resp_result = resp.json() if 'json' in resp.headers.get('Content-Type') else resp.text
            return resp_result
        except Exception as e:
            logger.error(f'请求失败: {e}')


request_client = AllRequests()
