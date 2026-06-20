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
    if image==None or not image.filename:
        image_name="default.png"
    else:
        image_name=uuid.uuid4().hex
        image.save(f"static/media/{image_name}")
    new_course=models.Courses(name=name,description=description,image_name=image_name)
    db.db.session.add(new_course)
    db.db.session.commit()
    return redirect(url_for("course.edit_course",course_id=new_course.id))

@course.route("/delete_course/<int:course_id>",methods=["DELETE"])
def delete_course(course_id):
    course=models.Courses.query.filter_by(id=course_id).first()
    if not course:
        flash("No such course")
        return redirect(url_for("course.get_courses"))
    else:
        db.db.session.delete(course)
        db.db.session.commit()
        return redirect(url_for("course.get_courses"))
    
@course.route("/course/<int:course_id>",methods=["GET",])
def coursee(course_id):
    course=models.Courses.query.filter_by(id=course_id).first()
    if not course:
        flash("No such course")
        return redirect(url_for("course.get_courses"))
    else:
        return render_template("course_page.html",info=course)
    
@course.route("/edit_course/<int:course_id>",methods=["GET",])
def edit_course(course_id):
    course=models.Courses.query.filter_by(id=course_id).first()
    if not course:
        flash("No such course")
        return redirect(url_for("course.get_courses"))
    else:
        return render_template("edit_course.html",info=course)