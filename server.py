import init,os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()
app:Flask=init.create_app()
app.config["SECRET_KEY"]=os.environ.get("SECRET_KEY")
app.run(host=os.environ.get("HOST"),port=os.environ.get("PORT"),debug=True)