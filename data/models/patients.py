import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin
import datetime
from data.db.db_session import SqlAlchemyBase


class Patient(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = "patients"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String(collation="NOCASE"))
    name = sqlalchemy.Column(sqlalchemy.String(collation="NOCASE"))
    birth_date = sqlalchemy.Column(sqlalchemy.Date, default="")
    age = sqlalchemy.Column(sqlalchemy.Integer, default="")
    diagnosis = sqlalchemy.Column(sqlalchemy.Text, default="")
    symptoms = sqlalchemy.Column(sqlalchemy.Text, default="")
    recommendations = sqlalchemy.Column(sqlalchemy.Text, default="")

    def __init__(self, surname, name, birth_date, diagnosis, symptoms, recommendations):
        self.surname = surname
        self.name = name
        self.birth_date = birth_date
        self.age = calculate_age(birth_date)
        self.diagnosis = diagnosis
        self.symptoms = symptoms
        self.recommendations = recommendations


def calculate_age(born_date):
    today = datetime.date.today()
    return today.year - born_date.year - ((today.month, today.day) < (born_date.month, born_date.day))
