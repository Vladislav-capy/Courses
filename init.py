import os
from flask import Flask
import auth,views,db,courses
def create_app():
    app=Flask(__name__)
    app.register_blueprint(auth.auth)
    app.register_blueprint(views.views)
    app.register_blueprint(courses.course)
    return app