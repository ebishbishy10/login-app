#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_login import LoginManager, UserMixin, login_user, \
    login_required, logout_user, current_user

Base = declarative_base()


class User(UserMixin, Base):

    __tablename__ = 'usersData'
    id = Column(Integer, primary_key=True)
    username = Column(String(15), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(80))


engine = create_engine('sqlite:///userData.db')
Base.metadata.create_all(engine)
