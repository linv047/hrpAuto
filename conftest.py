import pytest
import datetime
from pytest_yaml_yoyo import my_builtins

import os

# os.environ["http_proxy"] = "http://127.0.0.1:8888" # 此处填写你的代理
# os.environ["https_proxy"] = "http://127.0.0.1:8888" # 此处填写你的代理
#获取当前日期
def get_now_date():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d')


my_builtins.get_now_date = get_now_date
