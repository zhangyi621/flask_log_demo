import os
import logging
from logging.handlers import RotatingFileHandler


def created_handler(basedir):
    LOG_PATH = os.path.abspath(os.path.join(os.path.join(basedir, os.path.pardir), 'logs'))
    # 创建handler
    handler = RotatingFileHandler(os.path.join(LOG_PATH, 'flask_demo.log'), maxBytes=100 * 1024 * 1024, backupCount=10,
                                  encoding="utf-8")
    # 设置handler日志级别
    handler.setLevel(logging.DEBUG)
    # 设置handler打印格式
    fmt_str = logging.Formatter(
        '时间:%(asctime)-15s 日志级别:%(levelname)s 文件名:%(filename)s 行数:%(lineno)d 进程号:%(process)d 当前线程号:%(thread)s 日志信息:%(message)s')
    handler.setFormatter(fmt_str)
    # 设置过滤器
    return handler
