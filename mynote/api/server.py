from flask import Flask, render_template
from mynote.api import router
from mynote.api.db import Db


def create_app(root_path, db_path):
    app = Flask(__name__, root_path=root_path)
    frontend(app) # web
    app.register_blueprint(router.api_blue) # api

    # 解决flask模版与vue的冲突
    app.jinja_env.variable_start_string = '++++'
    app.jinja_env.variable_end_string = '++++'

    # db
    # db = Db(db_path)

    return app

def frontend(app:Flask):
    @app.route('/')
    def index():
        return render_template("index.html")