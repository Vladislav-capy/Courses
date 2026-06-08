from flask import render_template,redirect,url_for,Blueprint,request,flash,session
import models
import db
views=Blueprint("views",__name__)

@views.route("/main",methods=["GET",])
def main():
    return render_template("main.html")