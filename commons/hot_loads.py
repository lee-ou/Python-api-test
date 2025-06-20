import random
from utils.yaml_handle import read_config


class HotLoads:
    """热加载类"""

    def env(self):
        """获取项目环境"""
        return read_config('ENV', 'test_url')
    
    def get_random_number(self, min_val=1, max_val=100):
        """
        获取指定范围内的随机整数
        Args:
            min_val (int): 最小值，默认为1
            max_val (int): 最大值，默认为100
            
        Returns:
            int: 随机整数
        """
        return random.randint(min_val, max_val)

