from sqlalchemy import Column, Integer, String, Float, Boolean, Text, ForeignKey, Enum, DATE, DATETIME
from datetime import datetime
from sqlalchemy.orm import relationship
from Hotel import db, app
from enum import Enum as UserEnum
from flask_login import UserMixin
from datetime import datetime


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


class LoaiKhach(db.Model):
    __tablename__ = 'loaikhach'
    loaiKhachId = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    loaiKhach = Column(String(50))
    khachHang = relationship('khachHang', backref='loaikhach', lazy=True)


class khachHang(db.Model):
    __tablename__ = 'khachhang'
    MaKhachHang = Column(Integer,  primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    address = Column(String(200))
    phone = Column(String(20))
    CCCD = Column(String(20))
    loaiKhach_id = Column(Integer, ForeignKey(LoaiKhach.loaiKhachId), nullable=False)
    taiKhoanKhachHang_id = relationship('TaiKhoan_KhachHang', backref='khachhang', lazy=True)
    phieuDatPhong = relationship('phieuDatPhong', backref='khachhang', lazy=True)


class hoaDon(db.Model):
    __tablename__ = 'HoaDon'
    maHoaDon = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    TongTien = Column(Float, nullable=False)
    hoaDon_ThongTinPhong = relationship('hoaDon_ThongTinPhong', backref='hoadon', lazy=True)


class hoaDon_ThongTinPhong(db.Model):
    __tablename__ = 'hoaDon_ThongTinPhong'
    hoaDon_ThongTinPhong_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
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
    maNhanVien = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
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
    maPhieuDatPhong = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ngayNhanPhong = Column(DATE, nullable=False)
    ngayTraPhong = Column(DATE, nullable=False)
    maKhachHang = Column(Integer, ForeignKey(khachHang.MaKhachHang), nullable=False)
    chiTiet_DSKhachHang = relationship('chiTiet_DSKhachHang', backref='phieudatphong', lazy=True)
    ThongTinPhong_phieuDatPhong = relationship('ThongTinPhong_phieuDatPhong', backref='phieudatphong', lazy=True)


class phieuThuePhong(db.Model):
    __tablename__ = 'phieuThuePhong'
    maPhieuThuePhong = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ngayNhanPhong = Column(DATETIME, nullable=False)
    ngayTraPhong = Column(DATETIME, nullable=False)
    chiTiet_DSKhachHang = relationship('chiTiet_DSKhachHang', backref='phieuthuephong', lazy=True)
    ThongTinPhong_phieuThuePhong = relationship('ThongTinPhong_phieuThuePhong', backref='phieuthuephong', lazy=True)


class chiTiet_DSKhachHang(db.Model):
    __tablename__ = 'chiTiet_DSKhachHang'
    machiTietDSKhachHang = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    address = Column(String(200))
    phone = Column(String(20))
    CCCD = Column(String(20))
    LoaiKhach = Column(String(50))
    maPhieuThuePhong = Column(Integer, ForeignKey(phieuThuePhong.maPhieuThuePhong), nullable=False)
    maPhieuDatPhong = Column(Integer, ForeignKey(phieuDatPhong.maPhieuDatPhong), nullable=False)


class ThongTinPhong_phieuDatPhong(db.Model):
    __tablename__ = 'ThongTinPhong_phieuDatPhong'
    ThongTinPhong_phieuDatPhong_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    maPhieuDatPhong = Column(Integer, ForeignKey(phieuDatPhong.maPhieuDatPhong), nullable=False)
    maPhong = Column(Integer, ForeignKey(ThongTinPhong.maPhong), nullable=False)


class ThongTinPhong_phieuThuePhong(db.Model):
    __tablename__ = 'ThongTinPhong_phieuThuePhong'
    ThongTinPhong_phieuThuePhong_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    maPhieuThuePhong = Column(Integer, ForeignKey(phieuThuePhong.maPhieuThuePhong), nullable=False)
    maPhong = Column(Integer, ForeignKey(ThongTinPhong.maPhong), nullable=False)


class baoCaoDoanhThuTheoThang(db.Model):
    __tablename__ = 'baoCaoDoanhThuTheoThang'
    maBaoCao = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    thoiGian = Column(DATE, nullable=False)
    tongDoanhThu = Column(Float, nullable=False)
    ChiTiet_baoCaoDoanhThuTheoThang = relationship('ChiTiet_baoCaoDoanhThuTheoThang', backref='baocaodoanhthutheothang', lazy=True)


class ChiTiet_baoCaoDoanhThuTheoThang(db.Model):
    __tablename__ = 'ChiTiet_baoCaoDoanhThuTheoThang'
    maChiTietBaoCao = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    loaiPhong = Column(String(50), nullable=False)
    DoanhThu = Column(Float, nullable=False)
    soLuotThue = Column(Float, nullable=False)
    tiLe = Column(Float, nullable=False)
    maBaoCao = Column(Integer, ForeignKey(baoCaoDoanhThuTheoThang.maBaoCao, ondelete='CASCADE'), nullable=False)


class baoCaoMatDoSuDung(db.Model):
    __tablename__ = 'baoCaoMatDoSuDung'
    mabaoCaoMatDoSuDung = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    thoiGian = Column(DATE, nullable=False)
    ChiTiet_baoCaoMatDoSuDung = relationship('ChiTiet_baoCaoMatDoSuDung', backref='baocaomatdosudung', lazy=True)


class ChiTiet_baoCaoMatDoSuDung(db.Model):
    __tablename__ = 'ChiTiet_baoCaoMatDoSuDung'
    maChiTietBaoCaoMatDoSuDung = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
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
        e = TaiKhoan(name='Hieu', username='hieu', password=password, phoneNumber='0123456789',
                     avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     active=True, user_role=UserRole.EMPLOYEE)
        c = TaiKhoan(name='Thanh', username='thanh', password=password, phoneNumber='0123456789',
                     avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     active=True, user_role=UserRole.USER)
        db.session.add_all([u, e, c])
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

        lk1 = LoaiKhach(loaiKhach='Nội địa')
        lk2 = LoaiKhach(loaiKhach='Nước ngoài')
        db.session.add_all([lk1, lk2])
        db.session.commit()

        k1 = khachHang(name='Gia Huy', address='371 Nguyễn Kiệm', phone='0123456', CCCD='1456789', loaiKhach_id=1)
        k2 = khachHang(name='Minh Thành', address='483 Nguyễn Kiệm', phone='0123456', CCCD='14567895653', loaiKhach_id=2)
        k3 = khachHang(name='Đức Hiếu', address='456 Nguyễn Kiệm', phone='0123456', CCCD='14567898132', loaiKhach_id=1)
        k4 = khachHang(name='Quang Tới', address='459 Nguyễn Kiệm', phone='0123456', CCCD='1456789568', loaiKhach_id=2)
        db.session.add_all([k1, k2, k3, k4])
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
        h6 = hinhAnhPhong(hinhAnh='https://res.cloudinary.com/dgkrvmsli/image/upload/v1669645332/room2.1_vdcvvm.jpg',
                          loaiPhong_id=2)
        h7 = hinhAnhPhong(hinhAnh='https://res.cloudinary.com/dgkrvmsli/image/upload/v1669645330/room2.2_va9a7t.jpg',
                          loaiPhong_id=2)
        h8 = hinhAnhPhong(hinhAnh='https://res.cloudinary.com/dgkrvmsli/image/upload/v1669645331/room3.1_dfqz2y.jpg',
                          loaiPhong_id=3)
        h9 = hinhAnhPhong(hinhAnh='https://res.cloudinary.com/dgkrvmsli/image/upload/v1669645330/room3.3_itb040.jpg',
                          loaiPhong_id=3)
        db.session.add_all([h1, h2, h3, h4, h5, h6, h7, h8, h9])
        db.session.commit()

        phieuDP1 = phieuDatPhong(ngayNhanPhong=datetime(2022, 12, 3), ngayTraPhong=datetime(2022, 12, 5), maKhachHang=1)
        phieuDP2 = phieuDatPhong(ngayNhanPhong=datetime(2022, 12, 4), ngayTraPhong=datetime(2022, 12, 6), maKhachHang=2)
        phieuDP3 = phieuDatPhong(ngayNhanPhong=datetime(2022, 12, 5), ngayTraPhong=datetime(2022, 12, 7), maKhachHang=3)
        db.session.add_all([phieuDP1, phieuDP2, phieuDP3])
        db.session.commit()

        phieuTP1 = phieuThuePhong(ngayNhanPhong=datetime(2022, 12, 3), ngayTraPhong=datetime(2022, 12, 5))
        phieuTP2 = phieuThuePhong(ngayNhanPhong=datetime(2022, 12, 4), ngayTraPhong=datetime(2022, 12, 6))
        phieuTP3 = phieuThuePhong(ngayNhanPhong=datetime(2022, 12, 5), ngayTraPhong=datetime(2022, 12, 7))
        db.session.add_all([phieuTP1, phieuTP2, phieuTP3])
        db.session.commit()

        ct_dsKH1 = chiTiet_DSKhachHang(machiTietDSKhachHang='111', name='Báo Hiếu', address='Tân Bình', phone='123456789',
                                       CCCD='87545624', LoaiKhach=1, maPhieuThuePhong=1, maPhieuDatPhong=1)
        ct_dsKH2 = chiTiet_DSKhachHang(machiTietDSKhachHang='222', name='Thành', address='Nguyễn Kiệm', phone='789556214',
                                       CCCD='202556155', LoaiKhach=1, maPhieuThuePhong=2, maPhieuDatPhong=2)
        ct_dsKH3 = chiTiet_DSKhachHang(machiTietDSKhachHang='333', name='Huy', address='Bình Tân', phone='6666666',
                                       CCCD='777777', LoaiKhach=2, maPhieuThuePhong=3, maPhieuDatPhong=3)
        db.session.add_all([ct_dsKH1, ct_dsKH2, ct_dsKH3])
        db.session.commit()

        hd1 = hoaDon(TongTien='2500000')
        hd2 = hoaDon(TongTien='2500000')
        hd3 = hoaDon(TongTien='2500000')
        db.session.add_all([hd1, hd2, hd3])
        db.session.commit()

        hd_ttp1 = hoaDon_ThongTinPhong(maHoaDon='1', maPhong='1')
        hd_ttp2 = hoaDon_ThongTinPhong(maHoaDon='2', maPhong='2')
        hd_ttp3 = hoaDon_ThongTinPhong(maHoaDon='3', maPhong='3')
        db.session.add_all([hd_ttp1, hd_ttp2, hd_ttp3])
        db.session.commit()



        # phieuDatPhong1 = phieuDatPhong(ngayNhanPhong='2022-11-26', ngayTraPhong='2022-11-29', maKhachHang=1)
        # db.session.add(phieuDatPhong1)
        # db.session.commit()

        pdt_ttp1 = ThongTinPhong_phieuDatPhong(maPhieuDatPhong=1, maPhong=1)
        pdt_ttp2 = ThongTinPhong_phieuDatPhong(maPhieuDatPhong=1, maPhong=2)
        pdt_ttp3 = ThongTinPhong_phieuDatPhong(maPhieuDatPhong=2, maPhong=3)
        pdt_ttp4 = ThongTinPhong_phieuDatPhong(maPhieuDatPhong=2, maPhong=4)
        db.session.add_all([pdt_ttp1, pdt_ttp2, pdt_ttp3, pdt_ttp4])
        db.session.commit()





