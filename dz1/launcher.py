from flask import Flask,render_template,redirect,session,request
from flask_socketio import SocketIO,emit,join_room,leave_room
import datadz
import os
import game

def create():
    app=Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///base"
    app.config["SECRET_KEY"]="login"
    app.register_blueprint(game.game,url_prefix="/")
    datadz.data.init_app(app)
    init_database(app)
    return app

def init_database(app):
    os.makedirs("instance",exist_ok=True)
    with app.app_context():
        datadz.data.create_all()