from flask import Blueprint,render_template,request,redirect,session,url_for,send_from_directory
from werkzeug.security import generate_password_hash,check_password_hash
import datadz
import class2
game=Blueprint("game",__name__)

@game.route("/main")
def main():
    return render_template("main.html",game=class2.Game.query.all())

@game.route("/game",methods=["POST","GET"])
def add_game():
    if request.method=="GET":
        return render_template("main.html",game=class2.Game.query.all())
    else:
        title=request.form.get("book_name")
        genre=request.form.get("author")
        rating=int(request.form.get("rating"))
        if title==None:
            return render_template("main.html",error="Введите название книги",game=class2.Game.query.all())
        if title.replace(" ", "")=="":
            return render_template("main.html",error="Введите название книги",game=class2.Game.query.all())
        if genre.replace(" ", "")=="":
            return render_template("main.html",error="Введите имя автора",game=class2.Game.query.all())
        if genre==None:
            return render_template("main.html",error="Введите имя автора",game=class2.Game.query.all())
        if rating<0:
            return render_template("main.html",error="Введите число от 0 до 10",game=class2.Game.query.all())
        if rating>10:
            return render_template("main.html",error="Введите число от 0 до 10",game=class2.Game.query.all())
        else:
            new_book=class2.Game(title=title,genre=genre,rating=rating)
            datadz.data.session.add(new_book)
            datadz.data.session.commit()
            return render_template("main.html",game=class2.Game.query.all())
