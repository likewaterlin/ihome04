# coding:utf-8
from logging.handlers import RotatingFileHandler

import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from config import config_dict,Config
from utils.common import RegexConverter
from flask_wtf.csrf import CSRFProtect
import logging



db = SQLAlchemy()

csrf = CSRFProtect()

redis_store = None

# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)  # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logging.getLogger().addHandler(file_log_handler)

def create_app(config_name):

    app = Flask(__name__)
    config_mode = config_dict[config_name]
    app.config.from_object(config_mode)

    # 给app的路由转换器字典增加我们自定义的转换器
    app.url_map.converters['re'] = RegexConverter

    db.init_app(app)
    # csrf.init_app(app)
    global redis_store
    redis_store = redis.StrictRedis(port=Config.REDIS_PORT, host=Config.REDIS_HOST)

    # 创建能够将默认存放在cookie的sesion数据, 转移到redis的对象
    # http://pythonhosted.org/Flask-Session/
    Session(app)



    from api_1_0 import api
    app.register_blueprint(api,url_prefix='/api/v1_0')

    import web_html
    app.register_blueprint(web_html.html)

    return app, db

