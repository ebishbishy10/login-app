#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
import os
import sys
from flask import render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from database_setup import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from werkzeug.security import generate_password_hash, \
    check_password_hash
from flask_login import LoginManager, UserMixin, login_user, \
    login_required, logout_user, current_user


PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissuposedtobesecret'
# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:////' + os.path.join(PROJECT_ROOT, 'tmp', 'test.db')

Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# db = SQLAlchemy(app)

engine = create_engine('sqlite:///userData.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
Session = scoped_session(DBSession)
session = Session()


# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(15), unique=True)
#     email = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(80))

@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(int(user_id))


# if serer working!!! check? #

@app.route('/h')
def hello():
    return 'Hello F FWorld!'


# Log in form class #

class LoginForm(FlaskForm):

    username = StringField('username', validators=[InputRequired(),
                           Length(min=8, max=16)])
    password = PasswordField('password', validators=[InputRequired(),
                             Length(min=8, max=80)])
    remember = BooleanField('remember me')


# signup form class #

class RegisterForm(FlaskForm):

    email = StringField('email', validators=[InputRequired(),
                        Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(),
                           Length(min=8, max=16)])
    password = PasswordField('password', validators=[InputRequired(),
                             Length(min=8, max=80)])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = \
            user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return '<h1> Invalid username or password </h>'

        # return '<h1>' + form.username.data + "  " +form.password.data+'</h1>'

    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        try:
            hashed_password = generate_password_hash(form.password.data, method='sha256')
            new_user = User(username=form.username.data, email=form.email.data,
                            password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            # session.remove()
            return '<h1> New user Created </h1>'
        except:
            session.rollback()
            return '<h1> not valid </h1>'

    return render_template('signup.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)