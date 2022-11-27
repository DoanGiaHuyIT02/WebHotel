from Hotel.models import TaiKhoan
from Hotel import db
from flask_login import current_user
import hashlib


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return TaiKhoan.query.filter(TaiKhoan.username.__eq__(username.strip()),
                             TaiKhoan.password.__eq__(password)).first()


def register(name, username, password, phoneNumber, avatar):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = TaiKhoan(name=name, username=username.strip(), password=password, phoneNumber=phoneNumber, avatar=avatar)
    db.session.add(u)
    db.session.commit()


def get_user_by_id(user_id):
    return TaiKhoan.query.get(user_id)
