# -*- coding:utf-8 -*-

from werkzeug.routing import BaseConverter


# 自定义正则转换器
class RegexConverter(BaseConverter):
    # 重新init方法, 增加参数
    # regex: 就是在使用时, 传入的正则表达式
    def __init__(self, url_map, regex):
        # 调用父类方法
        super(RegexConverter, self).__init__(url_map)
        self.regex = regex
