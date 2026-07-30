from flask import render_template,redirect,url_for,Blueprint,request,flash,session
import models
import db,auth
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
    if "login" not in session:
        return redirect(url_for("auth.register"))
    else:
        course=models.Courses.query.filter_by(id=course_id).first()
        question=models.Question.query.filter_by(course_id=course_id).all()
        if not course:
            flash("No such course")
            return redirect(url_for("course.get_courses"))
        else:
            return render_template("course_page.html",info=course,quest=question)
    
@course.route("/edit_course/<int:course_id>",methods=["GET",])
def edit_course(course_id):
    course=models.Courses.query.filter_by(id=course_id).first()
    if not course:
        flash("No such course")
        return redirect(url_for("course.get_courses"))
    else:
        return render_template("edit_course.html",info=course)

@course.route("/save",methods=["POST",])
def save():
    info=request.get_json()
    theory_text=info["theory_text"]
    questions=info["questions"]
    course=models.Courses.query.filter_by(id=info["course_id"]).first()
    course.theory_text=theory_text
    db.db.session.commit()
    questions2=models.Question.query.filter_by(course_id=info["course_id"]).all()
    for i in questions2:
        db.db.session.delete(i)
    for i in questions:
        new_question=models.Question(course_id=info["course_id"],question=i[0],answer=i[1])
        db.db.session.add(new_question)
    db.db.session.commit()
    return "ok"

@course.route("/check_answers/<int:course_id>",methods=["POST",])
def check_answers(courseid):
    answers=request.get_json()
    correct_answers=models.Question.query.filter_by(course_id=courseid).all()
    
    return "ok"