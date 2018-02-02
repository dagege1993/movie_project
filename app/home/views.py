from . import home  # 从当前目录引入蓝图对象
from flask import render_template, redirect, url_for


@home.route('/')
def index():
    return render_template('home/index.html')


@home.route('/login/')
def login():
    return render_template('home/login.html')


@home.route('/logout/')
def logout():
    #  redirect() 函数重定向用户到其它地方
    return redirect(url_for('home.login'))


@home.route('/regist/')
def regist():
    return render_template('home/regist.html')
