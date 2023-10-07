import os

from data.db import db_session
from dotenv import load_dotenv
from flask import Flask, render_template


load_dotenv()

db_session.global_init("data/db/db_files/models.sqlite")
DB_SESSION = db_session.create_session()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.route("/")
def index():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(port=os.getenv("PORT"), host=os.getenv("HOST"))
