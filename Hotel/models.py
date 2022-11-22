from sqlalchemy import Column, Integer, String, Float, Boolean, Text, ForeignKey, Enum, DATE, DATETIME
from sqlalchemy.orm import relationship
from Hotel import db, app
from enum import Enum as UserEnum
# from flask_login import UserMixin


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class ThongTinPhong(db.Model):
    __tablename__ = 'thongTinPhong'
    maPhong = Column(Integer,  primary_key=True, nullable=False)
    soPhong = Column(String(50), nullable=False)
    loaiPhong = Column(String(50), nullable=False)
    donGia = Column(Float, nullable=False)
    tinhTrang = Column(Boolean, nullable=False)
    hoaDon_ThongTinPhong = relationship('hoaDon_ThongTinPhong', backref='thontinphong', lazy=True)
    ThongTinPhong_phieuDatPhong = relationship('ThongTinPhong_phieuDatPhong', backref='thontinphong', lazy=True)
    ThongTinPhong_phieuThuePhong = relationship('ThongTinPhong_phieuThuePhong', backref='thontinphong', lazy=True)


class khachHang(db.Model):
    __tablename__ = 'khachhang'
    MaKhachHang = Column(Integer,  primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    address = Column(String(200))
    phone = Column(String(20))
    CCCD = Column(String(20))
    LoaiKhach = Column(String(50))
    taiKhoan = relationship('TaiKhoan', backref='khachhang', lazy=True)
    phieuDatPhong = relationship('KhachHang', backref='phieudatphong', lazy=True)


class hoaDon(db.Model):
    __tablename__ = 'HoaDon'
    maHoaDon = Column(Integer, primary_key=True, nullable=False)
    TongTien = Column(Float, nullable=False)
    hoaDon_ThongTinPhong = relationship('hoaDon_ThongTinPhong', backref='hoadon', lazy=True)


class hoaDon_ThongTinPhong(db.Model):
    __tablename__ = 'hoaDon_ThongTinPhong'
    hoaDon_ThongTinPhong_id = Column(Integer, primary_key=True, nullable=False)
    maHoaDon = Column(Integer, ForeignKey(hoaDon.maHoaDon), nullable=False)
    maPhong = Column(Integer, ForeignKey(ThongTinPhong.maPhong), nullable=False)


class nhanVien(db.Model):
    __tablename__ = 'nhanvien'
    maNhanVien = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    address = Column(String(200))
    phone = Column(String(20))
    CCCD = Column(String(20))
    tuoi = Column(String(3))
    ngayVaoLam = Column(DATE)
    email = Column(String(50))
    taiKhoan = relationship('TaiKhoan', backref='nhanvien', lazy=True)


class TaiKhoan (db.Model, UserMixin):
    __tablename__ = 'TaiKhoan'
    taiKhoan_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    maNhanVien = Column(Integer, ForeignKey(nhanVien.maNhanVien), unique=True, nullable=False)
    MaKhachHang = Column(Integer, ForeignKey(khachHang.MaKhachHang), nullable=False)


class phieuDatPhong(db.Model):
    __tablename__ = 'phieuDatPhong'
    maPhieuDatPhong = Column(Integer, primary_key=True, nullable=False)
    ngayNhanPhong = Column(DATETIME, nullable=False)
    ngayTraPhong = Column(DATETIME, nullable=False)
    maKhachHang = Column(Integer, ForeignKey(khachHang.MaKhachHang), nullable=False)
    chiTiet_DSKhachHang = relationship('chiTietDSKhachHang', backref='phieudatphong', lazy=True)
    ThongTinPhong_phieuDatPhong = relationship('ThongTinPhong_phieuDatPhong', backref='phieudatphong', lazy=True)


class phieuThuePhong(db.Model):
    __tablename__ = 'phieuThuePhong'
    maPhieuThuePhong = Column(Integer, primary_key=True, nullable=False)
    ngayNhanPhong = Column(DATETIME, nullable=False)
    ngayTraPhong = Column(DATETIME, nullable=False)
    chiTiet_DSKhachHang = relationship('chiTietDSKhachHang', backref='phieuthuephong', lazy=True)
    ThongTinPhong_phieuThuePhong = relationship('ThongTinPhong_phieuThuePhong', backref='phieuthuephong', lazy=True)


class chiTiet_DSKhachHang(db.Model):
    __tablename__ = 'chiTiet_DSKhachHang'
    machiTietDSKhachHang = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    address = Column(String(200))
    phone = Column(String(20))
    CCCD = Column(String(20))
    LoaiKhach = Column(String(50))
    maPhieuThuePhong = Column(Integer, ForeignKey(phieuThuePhong.maPhieuThuePhong), nullable=False)
    maPhieuDatPhong = Column(Integer, ForeignKey(phieuDatPhong.maPhieuDatPhong), nullable=False)



class ThongTinPhong_phieuDatPhong(db.Model):
    __tablename__ = 'ThongTinPhong_phieuDatPhong'
    ThongTinPhong_phieuDatPhong_id = Column(Integer, primary_key=True, nullable=False)
    maPhieuDatPhong = Column(Integer, ForeignKey(phieuDatPhong.maPhieuDatPhong), nullable=False)
    maPhong = Column(Integer, ForeignKey(ThongTinPhong.maPhong), nullable=False)


class ThongTinPhong_phieuThuePhong(db.Model):
    __tablename__ = 'ThongTinPhong_phieuThuePhong'
    ThongTinPhong_phieuThuePhong_id = Column(Integer, primary_key=True, nullable=False)
    maPhieuThuePhong = Column(Integer, ForeignKey(phieuThuePhong.maPhieuThuePhong), nullable=False)
    maPhong = Column(Integer, ForeignKey(ThongTinPhong.maPhong), nullable=False)



class baoCaoDoanhThuTheoThang(db.Model):
    __tablename__ = 'baoCaoDoanhThuTheoThang'
    maBaoCao = Column(Integer, primary_key=True, nullable=False)
    thoiGian = Column(DATE, nullable=False)
    tongDoanhThu = Column(Float, nullable=False)
    ChiTiet_baoCaoDoanhThuTheoThang = relationship('ChiTiet_baoCaoDoanhThuTheoThang', backref='baocaodoanhthutheothang', lazy=True)


class ChiTiet_baoCaoDoanhThuTheoThang(db.Model):
    __tablename__ = 'ChiTiet_baoCaoDoanhThuTheoThang'
    maChiTietBaoCao = Column(Integer, primary_key=True, nullable=False)
    loaiPhong = Column(String(50), nullable=False)
    DoanhThu = Column(Float, nullable=False)
    soLuotThue = Column(Float, nullable=False)
    tiLe = Column(Float, nullable=False)
    maBaoCao = Column(Integer, ForeignKey(baoCaoDoanhThuTheoThang.maBaoCao, ondelete='CASCADE'), nullable=False)


class baoCaoMatDoSuDung(db.Model):
    __tablename__ = 'baoCaoMatDoSuDung'
    mabaoCaoMatDoSuDung = Column(Integer, primary_key=True, nullable=False)
    thoiGian = Column(DATE, nullable=False)
    ChiTiet_baoCaoMatDoSuDung = relationship('ChiTiet_baoCaoMatDoSuDung', backref='baocaomatdosudung', lazy=True)


class ChiTiet_baoCaoMatDoSuDung(db.Model):
    __tablename__ = 'ChiTiet_baoCaoMatDoSuDung'
    maChiTietBaoCaoMatDoSuDung = Column(Integer, primary_key=True, nullable=False)
    Phong = Column(Integer, nullable=False)
    soNgayThue = Column(Float, nullable=False)
    tiLe = Column(Float, nullable=False)
    mabaoCaoMatDoSuDung = Column(Integer, ForeignKey(baoCaoMatDoSuDung.mabaoCaoMatDoSuDung, ondelete='CASCADE'), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()