from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_mail import Mail


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
     'mysql://root:147258@localhost:3306/flask?charset=utf8mb4'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
manager = Manager(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    manager.run()