#  app 初始化
from flask import Flask

app = Flask(__name__)
app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

# 注册蓝图
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")  # 区分路由
