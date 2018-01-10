# -*- coding: utf-8 -*-


from flask import Blueprint,current_app
from flask import make_response
from flask_wtf.csrf import generate_csrf

html = Blueprint('html',__name__)

# @html.route('/')
# def index():
#     return current_app.send_static_file('html/index.html')
#
# @html.route('/<file_name>')
# def get_file_name(file_name):
#     return current_app.send_static_file('html/'+file_name)

@html.route('/<re(r".*"):file_name>')
def get_html_file(file_name):

    #print(file_name)
    # 1. 处理没有文件名, 自行拼接首页
    if not file_name:

        file_name = 'index.html'
    # 2. 如果发现文件名不叫"favicon.ico", 再拼接html/路径
    # favicon.ico: 浏览器为了显示图标, 会自动向地址发出一个请求
    if file_name != 'favicon.ico':

        file_name = 'html/' + file_name

    print(file_name)
    # 将html当做静态文件返回
    # 3. 如果文件名是'favicon.ico', 就直接返回
    # return current_app.send_static_file(file_name)

    # generate_csrf会检测当前session, 如果有, 则返回session中的. 如果没有, 则重新创建
    # generate_csrf的作用是新建session  （随机生成一个token值）
    csrf_token = generate_csrf()
    response = make_response(current_app.send_static_file(file_name))
    response.set_cookie('csrf_token', csrf_token)
    return response
