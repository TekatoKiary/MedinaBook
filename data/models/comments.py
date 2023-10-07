import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin
from data.db.db_session import SqlAlchemyBase


class Comment(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'comments'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    patient_id = sqlalchemy.Column(sqlalchemy.Integer)
    user_id = sqlalchemy.Column(sqlalchemy.Integer)
    comment_text = sqlalchemy.Column(sqlalchemy.Text)

    def __init__(self, patient_id, user_id, comment_text):
        self.patient_id = patient_id
        self.user_id = user_id
        self.comment_text = comment_text
