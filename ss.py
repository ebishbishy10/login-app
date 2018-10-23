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

from tray import db

db.create_all()
