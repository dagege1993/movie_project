from . import home  # 从当前目录引入蓝图对象
from flask import render_template, redirect, url_for


# @home.route('/')
# def index():
#     return render_template('home/index.html')


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


@home.route('/user')
def user():
    return render_template('home/user.html')


@home.route('/pwd/')
def pwd():
    return render_template('home/pwd.html')


@home.route('/comments/')
def comments():
    return render_template('home/comments.html')


@home.route('/loginlog/')
def loginlog():
    return render_template('home/loginlog.html')


@home.route('/moviecol/')
def moviecol():
    return render_template('home/moviecol.html')
@home.route('/')
def index():
    return render_template('home/index.html')


@home.route('/animation/')
def animation():
    return render_template('home/animation.html')