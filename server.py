from data.db import db_session
from flask import Flask, render_template, url_for

db_session.global_init("data/db/db_files/models.sqlite")
dataBase = db_session.create_session()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'


@app.route('/')
def index():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
