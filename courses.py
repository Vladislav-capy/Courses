from flask import render_template,redirect,url_for,Blueprint,request,flash,session
import models
import db
import uuid
course=Blueprint("course",__name__)

@course.route("/courses",methods=["GET",])
def get_courses():
    return render_template("main.html",courses=models.Courses.query.all())

@course.route("/add_course",methods=["POST",])
def add_course():
    name=request.form.get("name")
    description=request.form.get("description")
    image=request.files.get("image")
    if image==None:
        image_name="default.png"
    else:
        image_name=uuid.uuid4().hex
        image.save(f"static/media/{image_name}")
    new_course=models.Courses(name=name,description=description,image_name=image_name)
    db.db.session.add(new_course)
    db.db.session.commit()
    return redirect("courses.get_courses")

        