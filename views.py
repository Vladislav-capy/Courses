from flask import render_template,redirect,url_for,Blueprint,request,flash,session,send_from_directory
import models
import db
views=Blueprint("views",__name__)

@views.route("/main",methods=["GET",])
def main():
    return render_template("main.html")

@views.route("/image/<string:img_name>",methods=["GET",])
def get_image(img_name):
    return send_from_directory("static/media",img_name)