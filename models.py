from db import db

class User(db.Model):
    login=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(200),nullable=False)
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(30),unique=True,nullable=False)
    avatar_name=db.Column(db.String(100))

class Courses(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30))
    description=db.Column(db.String(50))
    image_name=db.Column(db.String(100))
    theory_text=db.Column(db.Text)

class Question(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    course_id=db.Column(db.Integer)
    question=db.Column(db.Text)
    answer=db.Column(db.String(100))