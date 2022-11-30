from Hotel.models import TaiKhoan, LoaiPhong, hinhAnhPhong, ThongTinPhong, khachHang, hoaDon, hoaDon_ThongTinPhong, nhanVien, TaiKhoan_KhachHang, phieuDatPhong, phieuThuePhong
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


def get_all_rooms():
    return LoaiPhong.query.all()


def get_all_images():
    return hinhAnhPhong.query.all()


# def get_all_rooms_info():
#     return ThongTinPhong.query.all()
#
#
# def customer():
#     return khachHang.query.all()
#
#
# def bill():
#     return hoaDon.query.all()
#
#
# def bill_rooms_info():
#     return hoaDon_ThongTinPhong.query.all()
#
#
# def employee():
#     return nhanVien.query.all()
#
#
# def account_customer():
#     return TaiKhoan_KhachHang.query.all()
#
#
# def reservation_ticket():
#     return phieuDatPhong.query.all()
#
#
# def rent_ticket():
#     return phieuThuePhong.query.all()
