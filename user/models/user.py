from db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import abort


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    def save_to_db(self):
        try:
            self.salt_password()
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            abort(500, message="something goes wrong with your db action")

    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def salt_password(self):
        self.password = generate_password_hash(self.password)

    def password_is_valid(self, password):
        return check_password_hash(self.password, password)

    def json(self):
        return dict(id=self.id, name=self.name, username=self.username, email=self.email)

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def all(cls):
        return cls.query.all()
