from sqlalchemy import Column, Integer, String, Float, Boolean, Text, ForeignKey, Enum, DATE, DATETIME
from sqlalchemy.orm import relationship
from Hotel import db, app
from enum import Enum as UserEnum
from flask_login import UserMixin


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2
    EMPLOYEE = 3


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class LoaiPhong(db.Model):
    __tablename__ = 'loaiphong'
    loaiPhongId = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    loaiPhong = Column(String(50), nullable=False)
    moTa = Column(String(10000), nullable=False)
    kichThuoc = Column(String(100), nullable=False)
    soGiuong = Column(String(100), nullable=False)
    donGia = Column(Float, nullable=False)
    hinhAnhChinh = Column(String(100), nullable=False)
    thongTinPhong = relationship('ThongTinPhong', backref='loaiphong', lazy=True)
    hinhAnh = relationship('hinhAnhPhong', backref='loaiphong', lazy=True)


class hinhAnhPhong(db.Model):
    __tablename__ = 'hinhanhphong'
    hinhAnhID = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    hinhAnh = Column(String(100), nullable=False)
    loaiPhong_id = Column(Integer, ForeignKey(LoaiPhong.loaiPhongId), nullable=False)

class ThongTinPhong(db.Model):
    __tablename__ = 'thongTinPhong'
    maPhong = Column(Integer,  primary_key=True, nullable=False, autoincrement=True)
    soPhong = Column(String(50), nullable=False)
    tinhTrang = Column(Boolean, nullable=False, default=True)
    loaiPhong_id = Column(Integer, ForeignKey(LoaiPhong.loaiPhongId), nullable=False)
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
    taiKhoanKhachHang_id = relationship('TaiKhoan_KhachHang', backref='khachhang', lazy=True)
    phieuDatPhong = relationship('phieuDatPhong', backref='khachhang', lazy=True)


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


class TaiKhoan(BaseModel, UserMixin):
    __tablename__ = 'taikhoan'
    # taiKhoan_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    phoneNumber = Column(String(12), nullable=False)
    avatar = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    taiKhoanKhachHang_id = relationship('TaiKhoan_KhachHang', backref='taikhoan', lazy=True)
    maNhanVien = relationship('nhanVien', backref='taikhoan', lazy=True)

    def __str__(self):
        return self.username


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
    taiKhoan = Column(Integer, ForeignKey(TaiKhoan.id), unique=True, nullable=False)



class TaiKhoan_KhachHang(db.Model):
    __tablename__ = 'taikhoan_khachhang'
    TKKH_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    KhachHang_id = Column(Integer, ForeignKey(khachHang.MaKhachHang), nullable=False)
    taiKhoan_id = Column(Integer, ForeignKey(TaiKhoan.id), nullable=False)


class phieuDatPhong(db.Model):
    __tablename__ = 'phieuDatPhong'
    maPhieuDatPhong = Column(Integer, primary_key=True, nullable=False)
    ngayNhanPhong = Column(DATETIME, nullable=False)
    ngayTraPhong = Column(DATETIME, nullable=False)
    maKhachHang = Column(Integer, ForeignKey(khachHang.MaKhachHang), nullable=False)
    chiTiet_DSKhachHang = relationship('chiTiet_DSKhachHang', backref='phieudatphong', lazy=True)
    ThongTinPhong_phieuDatPhong = relationship('ThongTinPhong_phieuDatPhong', backref='phieudatphong', lazy=True)


class phieuThuePhong(db.Model):
    __tablename__ = 'phieuThuePhong'
    maPhieuThuePhong = Column(Integer, primary_key=True, nullable=False)
    ngayNhanPhong = Column(DATETIME, nullable=False)
    ngayTraPhong = Column(DATETIME, nullable=False)
    chiTiet_DSKhachHang = relationship('chiTiet_DSKhachHang', backref='phieuthuephong', lazy=True)
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
        db.drop_all()
        db.create_all()

        import hashlib
        password = str(hashlib.md5('123456'.encode('utf-8')).hexdigest())
        u = TaiKhoan(name='Huy', username='huy', password=password, phoneNumber='0123456789',
                     avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     active=True, user_role=UserRole.ADMIN)
        db.session.add(u)
        db.session.commit()

        lp1 = LoaiPhong(loaiPhong='Standard Single', moTa='Phòng tiêu chuẩn, đơn giản với mức giá trung bình',
                        kichThuoc='30', soGiuong='2 giường đơn', donGia='3.5',
                        hinhAnhChinh='https://res.cloudinary.com/dgkrvmsli/image/upload/v1669642480/room-1_skeg8g.jpg')
        lp2 = LoaiPhong(loaiPhong='Standard Double', moTa='Phòng tiêu chuẩn, đơn giản với mức giá trung bình',
                        kichThuoc='35', soGiuong='1 giường đơn, 1 giường đôi', donGia='4.0',
                        hinhAnhChinh='https://res.cloudinary.com/dgkrvmsli/image/upload/v1669642479/room-2_ieduxp.jpg')
        lp3 = LoaiPhong(loaiPhong='Prenium', moTa='Phòng ở cao cấp với đầy đủ các tiện nghi, nội thất sang trọng',
                        kichThuoc='45', soGiuong='2 giường đôi', donGia='5.0',
                        hinhAnhChinh='https://res.cloudinary.com/dgkrvmsli/image/upload/v1669642490/room-3_k5e12i.jpg')
        db.session.add_all([lp1, lp2, lp3])
        db.session.commit()

        t1 = ThongTinPhong(soPhong='001', tinhTrang=True, loaiPhong_id=1)
        t2 = ThongTinPhong(soPhong='002', tinhTrang=True, loaiPhong_id=1)
        t3 = ThongTinPhong(soPhong='003', tinhTrang=True, loaiPhong_id=1)
        t4 = ThongTinPhong(soPhong='101', tinhTrang=True, loaiPhong_id=2)
        t5 = ThongTinPhong(soPhong='102', tinhTrang=True, loaiPhong_id=2)
        t6 = ThongTinPhong(soPhong='103', tinhTrang=True, loaiPhong_id=2)
        t7 = ThongTinPhong(soPhong='201', tinhTrang=True, loaiPhong_id=3)
        t8 = ThongTinPhong(soPhong='202', tinhTrang=True, loaiPhong_id=3)
        t9 = ThongTinPhong(soPhong='203', tinhTrang=True, loaiPhong_id=3)
        db.session.add_all([t1, t2, t3, t4, t5, t6, t7, t8, t9])
        db.session.commit()

        h1 = hinhAnhPhong(hinhAnh='https://res.cloudinary.com/dgkrvmsli/image/upload/v1669642480/room-1_skeg8g.jpg',
                          loaiPhong_id=1)
        h2 = hinhAnhPhong(hinhAnh='https://res.cloudinary.com/dgkrvmsli/image/upload/v1669642479/room-2_ieduxp.jpg',
                          loaiPhong_id=2)
        h3 = hinhAnhPhong(hinhAnh='https://res.cloudinary.com/dgkrvmsli/image/upload/v1669642490/room-3_k5e12i.jpg',
                          loaiPhong_id=3)
        h4 = hinhAnhPhong(hinhAnh='https://res.cloudinary.com/dgkrvmsli/image/upload/v1669645332/room1.1_esrtbt.jpg',
                          loaiPhong_id=1)
        h5 = hinhAnhPhong(hinhAnh='https://res.cloudinary.com/dgkrvmsli/image/upload/v1669645333/room1.2_rmi0sj.jpg',
                          loaiPhong_id=1)
        db.session.add_all([h1, h2, h3, h4, h5])
        db.session.commit()

