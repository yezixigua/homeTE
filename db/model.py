from flask import Flask
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User {}  email {}>'.format(self.username, self.email)


def db_test():
    db.create_all()

    admin = User(username='admin1', email='admin@exampl1e.com')

    # db.session.add(admin)
    db.session.commit()

    users = User.query.all()

    print(users)


if __name__ == '__main__':
    db_test()

