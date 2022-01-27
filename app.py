from flask import Flask, jsonify, make_response, request
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import uuid
import jwt
import datetime



app = Flask(__name__)

app.config['SECRET_KEY'] = '004f2af45d3a4e161a7dd2d17fdae47f'
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/manthantrivedi/Documents/Bacancy/bacancy_blogs/flask_auth/myflaskproject/bookstore.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
#class user in db
class Users(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   public_id = db.Column(db.Integer)
   name = db.Column(db.String(50))
   password = db.Column(db.String(50))
   admin = db.Column(db.Boolean)
class cart(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
   name = db.Column(db.String(50), unique=True, nullable=False)
   Author = db.Column(db.String(50), unique=True, nullable=False)
   image = db.Column(db.String(50), nullable=False)
   prize = db.Column(db.Integer)
db.create_all()