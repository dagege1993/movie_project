from flask import Blueprint
# 实例化一个蓝图对象
home = Blueprint('home', __name__)
# 把试图函数的内容导入进来
import app.home.views
