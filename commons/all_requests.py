import requests
import logging

logger = logging.getLogger(__name__)


class AllRequests:
    """
        接口统一请求
    """
    sess = requests.session()

    def send_request(self, **kwargs):
        try:
            for key, value in kwargs.items():
                if 'files' in key:
                    files = {}
                    for name, path in value.items():
                        files[name] = open(path, 'rb')
                    kwargs['files'] = files
                logger.info(f'请求{key}参数: {value}')
            resp = self.sess.request(**kwargs)
            logger.info(f'接口响应时间：{resp.elapsed}')
            if 'json' in resp.headers.get('Content-Type'):
                logger.info(f'接口响应：{resp.json()}')
                return resp.json()
            logger.info(f'接口响应：{resp.text}')
            return resp.text
        except Exception as e:
            logger.error(f'接口请求失败，失败原因：{e}')


request_client = AllRequests()
