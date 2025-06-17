from utils.yaml_handle import read_config


class HotLoads:
    """热加载类"""

    def env(self):
        """获取项目环境"""
        return read_config('ENV', 'test_url')
