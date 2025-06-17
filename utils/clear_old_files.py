import logging
import os.path
import shutil
import os.path
from glob import glob

logger = logging.getLogger(__name__)


class DataClearUtils:
    """数据清理工具类"""

    def _clear_extract(self):
        """清除extract文件数据"""
        with open("extract.yaml", "w") as f:
            f.truncate()

    def _clear_logs(self):
        """清理历史日志文件"""
        log_file = glob(os.path.join('./outputs/log', '*.log'))
        if len(log_file) > 8:
            log_file.sort()
            for i in log_file:
                os.remove(i)

    def _clear_reports(self):
        """清理历史测试报告数据"""
        report_file = glob(os.path.join('./outputs/reports', '*'))
        dirs = [d for d in report_file if os.path.isdir(d)]
        if len(dirs) > 8:
            dirs.sort()
            for f in dirs:
                shutil.rmtree(f)

    def data_clear(self):
        """数据清理"""
        self._clear_extract()
        self._clear_logs()
        self._clear_reports()
