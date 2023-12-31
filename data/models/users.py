import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime
from data.db.db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = "users"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String(collation="NOCASE"))
    name = sqlalchemy.Column(sqlalchemy.String(collation="NOCASE"))
    birth_date = sqlalchemy.Column(sqlalchemy.Date, default="")
    age = sqlalchemy.Column(sqlalchemy.Integer, default="")
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, default="")
    hashed_password = sqlalchemy.Column(sqlalchemy.String, default="")

    def __init__(self, surname, name, birth_date, email):
        self.surname = surname
        self.name = name
        self.birth_date = birth_date
        self.age = calculate_age(birth_date)
        self.email = email

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


def calculate_age(born_date):
    today = datetime.date.today()
    return today.year - born_date.year - ((today.month, today.day) < (born_date.month, born_date.day))
