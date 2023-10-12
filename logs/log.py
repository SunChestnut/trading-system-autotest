"""
@Author SunYL
@Time 2023/10/10 15:19
"""
import logging
import os.path
import time

from common.tools import (get_project_path, sep)


def set_log(logger_name: str, log_level: int):
    # 创建 logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    log_path = sep([get_project_path(), "autotest_logs"], False, True)
    # 若日志目录不存在，则自动创建
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    # 日志文件名格式：日志绝对路径+当前时间.log
    local_time = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    log_name = log_path + local_time + ".log"

    # FileHandler 用于将格式化的日志写入磁盘文件。fh_info 写入 info 级别以上的日志信息，fh_debug 写入 debug 级别以上的日志信息
    fh_info = logging.FileHandler(log_name)
    # handler 可以在 logger 设置的日志等级基础上再去过滤低于 handler 设置的日志登记
    fh_info.setLevel(logging.INFO)

    # 定义日志输出格式
    log_format = logging.Formatter(
        "%(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s")
    fh_info.setFormatter(log_format)

    fh_debug = logging.FileHandler(log_path + local_time + "--warn--.log")
    fh_debug.setLevel(logging.WARN)
    fh_debug.setFormatter(log_format)

    logger.addHandler(fh_info)
    logger.addHandler(fh_debug)

    return logger


autotest_log = set_log("自动化测试", logging.INFO)
