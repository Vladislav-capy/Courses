from flask import render_template,redirect,url_for,Blueprint,request,flash,session,send_from_directory
import models
import db
views=Blueprint("views",__name__)

@views.route("/main",methods=["GET",])
def main():
    if "login" not in session:
        return redirect(url_for("auth.register"))
    else:
        return redirect(url_for("course.get_courses"))

@views.route("/image/<string:img_name>",methods=["GET",])
def get_image(img_name):
    return send_from_directory("static/media",img_name)