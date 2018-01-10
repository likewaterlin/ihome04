#coding:utf-8



from . import api

import logging


@api.route('/')
def hello_world():
    logging.debug('debug')
    logging.info('info')
    logging.warn('warn')
    logging.error('error')
    return 'hello world!'

