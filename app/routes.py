from app.forms import LoginForm
from flask import render_template, flash, redirect

from app import app  # 从app包中导入 app这个实例


# 2个路由
@app.route('/')
@app.route('/index')
def index():
    user = {'username': '张三'}  # 用户
    posts = [  # 创建一个列表：帖子。里面元素是两个字典，每个字典里元素还是字典，分别作者、帖子内容。
        {
            'author': {'username': '张三'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': '李四'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': '王五'},
            'body': '今天是10月24！1024程序员节日！'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {},remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
