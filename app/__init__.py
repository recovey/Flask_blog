from flask import Flask  # 从flask包中导入Flask类
from config import Config
from flask_sqlalchemy import SQLAlchemy  # 从包中导入类
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel
from flask import request
from flask_babel import lazy_gettext as _l

app = Flask(__name__)  # 将Flask类的实例 赋值给名为 app 的变量。这个实例成为app包的成员。
app.config.from_object(Config)
db = SQLAlchemy(app)  # 数据库对象
migrate = Migrate(app, db)  # 迁移引擎对象
print('等会谁（哪个包或模块）在使用我：', __name__)
login = LoginManager(app)
login.login_view = 'login'
mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
babel = Babel(app)

# 语言监测
@babel.localeselector
def get_locale():
    print(request.accept_languages.best_match(app.config['LANGUAGES']))
    return request.accept_languages.best_match(app.config['LANGUAGES'])


login = LoginManager(app)
login.login_view = 'login'
login.login_message = _l('Please log in to access this page.')


from app import routes, models  # 从app包中导入模块routes