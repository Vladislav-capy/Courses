import init,os,db
from dotenv import load_dotenv
from flask import Flask

load_dotenv()
app:Flask=init.create_app()
app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("SQLALCHEMY_DATABASE_URI")
app.config["SECRET_KEY"]=os.environ.get("SECRET_KEY")
db.db.init_app(app)
with app.app_context():
    db.db.create_all()
app.run(host=os.environ.get("HOST"),port=os.environ.get("PORT"),debug=True)