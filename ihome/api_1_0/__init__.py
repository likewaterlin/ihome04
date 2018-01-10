# conding:utf-8
from flask import Blueprint


api = Blueprint('api',__name__)

import index, verify_code
