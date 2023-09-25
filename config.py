class Config:
    """多套环境的公共配置"""
    version = "v1.0"
    # 钉钉群机器人通知
    # DING_TALK = {
    #     "access_token": "****复制你的token****",
    # }


class TestConfig(Config):
    """测试环境"""
    BASE_URL = 'https://staging.freightapp.com'
    USERNAME = 'victor.lin@unisco.com'
    PASSWORD = 'cHo1TncxMDA='

    USER_ID = '28511'
    USER_TOKEN = 'WjBJ8QSCfc'
    ORDER_ID = '5968628'
    PU_ID = '5529092'


class UatConfig(Config):
    """联调环境"""
    BASE_URL = 'http://www.baidu.com'


# 环境关系映射
env = {
    "test": TestConfig,
    "uat": UatConfig
}
