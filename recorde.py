from pytest_yaml_yoyo.mitm_http import RecoderHTTP
"""
步骤：
1.pip 安装 mitmproxy 环境
> pip install mitmproxy
2.复制这里的代码，新建recorde.py 文件，设置过滤环境如:http://127.0.0.1:8001
3.启动服务
> mitmweb -s ./recorde.py -p 8099
4.电脑开启代理，设置对应端口
5.自动录制抓包转成 yaml 用例
"""


addons = [
    RecoderHTTP(['https://staging.freightapp.com'])   # 设置过滤环境
]