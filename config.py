# -*- coding: utf-8 -*-

import redis

class Config(object):

    DEBUG = True

    # Flask的数据库设置3306端口可以考虑不用写
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/ihomesh04'
    # 动态追踪修改设置，如未设置只会提示警告，不建议开启（未来会默认disable状态的)
    SQLALCHEMY_TRACK_MODIFICATIONS= False

    # 创建redis实例用到的参数
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    SECRET_KEY = 'gC3mALnjFSMTl8hOh2JAwtjEY/o22/k061PK5mXlbg8='

    # 配置session存储到redis中
    PERMANENT_SESSION_LIFETIME = 86400  # 单位是秒, 设置session过期的时间
    SESSION_TYPE = 'redis'  # 指定存储session的位置为redis
    SESSION_USE_SIGNER = True  # 对数据进行签名加密, 提高安全性
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 设置redis的ip和端口


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

config_dict = {
    'develop':DevelopmentConfig,
    'product':ProductionConfig

}


