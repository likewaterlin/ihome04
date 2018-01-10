# -*- coding: utf-8 -*-
import re

import logging
from flask import current_app
from flask import request,jsonify

from api_1_0 import api
from ihome import redis_store
from models import User
from utils.response_code import RET


@api.route('/users', methods=['POST'])
def register():
    resp_json = request.get_json
    mobile = resp_json.get('mobile')
    sms_code = resp_json.get('sms_code')
    password = resp_json.get('password')

    if not all([mobile,sms_code,password]):
        return jsonify({'errno':RET.PARAMERR,'errmsg':'参数不完整'})

    if not re.match(r'1[34578]\d{9}',mobile):
        return jsonify({'errno':RET.PARAMERR,'errmsg':'不正确的手机号'})

    try:
        real_sms_code = redis_store.get('sms_code_'+mobile)
    except Exception as e:
        current_app.loger.error(e)
        return jsonify({'errno': RET.DBERR, 'errmsg': '访问数据库异常'})


    if real_sms_code is None:
        return jsonify({'errno':RET.NODATA,'errmsg':'短信验证已过期'})

    if sms_code!=real_sms_code:
        return jsonify({'errno':RET.DATAERR,'errmsg':'短信验证码输入错误'})

    try:
        redis_store.delete('sms_code_'+mobile)
    except Exception as e:
        logging.error(e)

    user = User(name=mobile,mobile=mobile)
    user.password = password