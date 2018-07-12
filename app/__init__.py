from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from .categories.routes import categories
    from .posts.routes import posts
    from .main.routes import main
    from .auth.routes import auth
    app.register_blueprint(categories)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(auth)
    return app
