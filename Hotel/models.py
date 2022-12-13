from sqlalchemy import Column, Integer, String, Float, Boolean, Text, ForeignKey, Enum, DATE, DATETIME
from sqlalchemy.orm import relationship
from Hotel import db, app
from enum import Enum as UserEnum
from flask_login import UserMixin
from datetime import datetime, date


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
    phieuDatPhong_id = relationship('phieuDatPhong', backref='loaiphong', lazy=True)
    phieuThuePhong_id = relationship('phieuThuePhong', backref='loaiphong', lazy=True)


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


class LoaiKhach(db.Model):
    __tablename__ = 'loaikhach'
    loaiKhachId = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    loaiKhach = Column(String(50))
    ChiTiet_DSKH = relationship('chiTiet_DSKhachHang', backref='loaikhach', lazy=True)
    ChiTiet_DSKH_phieuthue = relationship('chiTiet_DSKH_PhieuThue', backref='loaikhach', lazy=True)


class khachHang(db.Model):
    __tablename__ = 'khachhang'
    MaKhachHang = Column(Integer,  primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    address = Column(String(200))
    phone = Column(String(20))
    CCCD = Column(String(20))
    taiKhoanKhachHang_id = relationship('TaiKhoan_KhachHang', backref='khachhang', lazy=True)
    phieuDatPhong = relationship('phieuDatPhong', backref='khachhang', lazy=True)
    phieuThuePhong = relationship('phieuThuePhong', backref='khachhang', lazy=True)


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
    namSinh = Column(DATE, nullable=False)
    ngayVaoLam = Column(DATE, nullable=False)
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
    thanhTien = Column(Float(20), nullable=False)
    loaiPhong_id = Column(Integer, ForeignKey(LoaiPhong.loaiPhongId), nullable=False)
    maKhachHang = Column(Integer, ForeignKey(khachHang.MaKhachHang), nullable=False)
    chiTiet_DSKhachHang = relationship('chiTiet_DSKhachHang', backref='phieudatphong', lazy=True)


class phieuThuePhong(db.Model):
    __tablename__ = 'phieuThuePhong'
    maPhieuThuePhong = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ngayNhanPhong = Column(DATETIME, nullable=False)
    ngayTraPhong = Column(DATETIME, nullable=False)
    thanhTien = Column(Float(20), nullable=False)
    loaiPhong_id = Column(Integer, ForeignKey(LoaiPhong.loaiPhongId), nullable=False)
    maKhachHang = Column(Integer, ForeignKey(khachHang.MaKhachHang), nullable=False)
    chiTiet_DSKH_PhieuThue = relationship('chiTiet_DSKH_PhieuThue', backref='phieuthuephong', lazy=True)
    hoaDon_id = relationship('hoaDon', backref='phieuthuephong', lazy=True)


class chiTiet_DSKhachHang(db.Model):
    __tablename__ = 'chiTiet_DSKhachHang'
    machiTietDSKhachHang = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    address = Column(String(200))
    CCCD = Column(String(20))
    loaiKhach_id = Column(Integer, ForeignKey(LoaiKhach.loaiKhachId), nullable=False)
    maPhieuDatPhong = Column(Integer, ForeignKey(phieuDatPhong.maPhieuDatPhong), nullable=False)


class chiTiet_DSKH_PhieuThue(db.Model):
    __tablename__ = 'chiTiet_dskh_phieuthue'
    chiTiet_DSKH_PhieuThue_ID = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    address = Column(String(200))
    CCCD = Column(String(20))
    loaiKhach_id = Column(Integer, ForeignKey(LoaiKhach.loaiKhachId), nullable=False)
    maPhieuThuePhong = Column(Integer, ForeignKey(phieuThuePhong.maPhieuThuePhong), nullable=False)


class hoaDon(db.Model):
    __tablename__ = 'HoaDon'
    maHoaDon = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    TongTien = Column(Float, nullable=False)
    maPhieuThuePhong = Column(Integer, ForeignKey(phieuThuePhong.maPhieuThuePhong), unique=True, nullable=False)
    hoaDon_ThongTinPhong = relationship('hoaDon_ThongTinPhong', backref='hoadon', lazy=True)


class hoaDon_ThongTinPhong(db.Model):
    __tablename__ = 'hoaDon_ThongTinPhong'
    hoaDon_ThongTinPhong_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    maHoaDon = Column(Integer, ForeignKey(hoaDon.maHoaDon), nullable=False)
    maPhong = Column(Integer, ForeignKey(ThongTinPhong.maPhong), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()

        import hashlib
        password = str(hashlib.md5('123456'.encode('utf-8')).hexdigest())
        u = TaiKhoan(name='Đoàn Gia Huy', username='huy', password=password, phoneNumber='0123456789',
                     avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     active=True, user_role=UserRole.ADMIN)
        e1 = TaiKhoan(name='Nguyên Thụy', username='thuy', password=password, phoneNumber='0123456789',
                     avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     active=True, user_role=UserRole.EMPLOYEE)
        e2 = TaiKhoan(name='Đức Hiếu', username='hieu', password=password, phoneNumber='0123456789',
                     avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     active=True, user_role=UserRole.EMPLOYEE)
        c = TaiKhoan(name='Minh Thành', username='thanh', password=password, phoneNumber='0123456789',
                     avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     active=True, user_role=UserRole.USER)
        c2 = TaiKhoan(name='Kim Tài', username='tai', password=password, phoneNumber='0123456789',
                     avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     active=True, user_role=UserRole.USER)
        c3 = TaiKhoan(name='Trần Đức Hiếu', username='hieu1', password=password, phoneNumber='0123456789',
                      avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                      active=True, user_role=UserRole.USER)
        c4 = TaiKhoan(name='Quang Tới', username='toi', password=password, phoneNumber='0123456789',
                      avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                      active=True, user_role=UserRole.USER)
        db.session.add_all([u,e1, e2, c, c2, c3, c4])
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

        k1 = khachHang(name="Minh Thành", address='371 Nguyễn Kiệm', phone='01234536', CCCD='1456789')
        k2 = khachHang(name='Kim Tài', address='483 Nguyễn Kiệm', phone='01233456', CCCD='14567895653')
        k3 = khachHang(name='Đức Hiếu', address='456 Nguyễn Kiệm', phone='01232456', CCCD='14567898132')
        k4 = khachHang(name='Quang Tới', address='459 Nguyễn Kiệm', phone='01523456', CCCD='1456789568')
        db.session.add_all([k1, k2, k3, k4])
        db.session.commit()

        nv1 = nhanVien(name='Kim Tài', address='123 Nguyễn Kiệm', phone='01649552', CCCD='072202123',
                       namSinh=datetime(2002, 3, 1), ngayVaoLam=datetime(2020, 10, 10), email='kt@gmail.com', taiKhoan=2)
        nv2 = nhanVien(name='Nguyên Thụy', address='124 Nguyễn Kiệm', phone='01674952', CCCD='07220256123',
                       namSinh=datetime(2002, 4, 1), ngayVaoLam=datetime(2021, 10, 20), email='nt@gmail.com', taiKhoan=3)
        nv3 = nhanVien(name='Đức Hiếu', address='125 Nguyễn Kiệm', phone='01645952', CCCD='07220212123',
                       namSinh=datetime(2002, 5, 1), ngayVaoLam=datetime(2022, 10, 20), email='dt@gmail.com', taiKhoan=4)
        db.session.add_all([nv1, nv2, nv3])
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

        phieuDP1 = phieuDatPhong(ngayNhanPhong=datetime(2022, 12, 3), ngayTraPhong=datetime(2022, 12, 5), maKhachHang=1,
                                 loaiPhong_id=1, thanhTien=3500000)
        phieuDP2 = phieuDatPhong(ngayNhanPhong=datetime(2022, 12, 4), ngayTraPhong=datetime(2022, 12, 6), maKhachHang=2,
                                 loaiPhong_id=2, thanhTien=4000000)
        phieuDP3 = phieuDatPhong(ngayNhanPhong=datetime(2022, 12, 5), ngayTraPhong=datetime(2022, 12, 7), maKhachHang=3,
                                 loaiPhong_id=3, thanhTien=5000000)
        db.session.add_all([phieuDP1, phieuDP2, phieuDP3])
        db.session.commit()

        phieuTP1 = phieuThuePhong(ngayNhanPhong=datetime(2022, 12, 3), ngayTraPhong=datetime(2022, 12, 5), maKhachHang=1,
                                  loaiPhong_id=1, thanhTien=3500000)
        phieuTP2 = phieuThuePhong(ngayNhanPhong=datetime(2022, 12, 4), ngayTraPhong=datetime(2022, 12, 6), maKhachHang=1,
                                  loaiPhong_id=1, thanhTien=3500000)
        phieuTP3 = phieuThuePhong(ngayNhanPhong=datetime(2022, 12, 5), ngayTraPhong=datetime(2022, 12, 7), maKhachHang=1,
                                  loaiPhong_id=1, thanhTien=3500000)
        db.session.add_all([phieuTP1, phieuTP2, phieuTP3])
        db.session.commit()

        ct_dsKH1 = chiTiet_DSKhachHang(name='Báo Hiếu', address='Tân Bình',
                                       CCCD='87545624', loaiKhach_id=1, maPhieuDatPhong=1)
        ct_dsKH2 = chiTiet_DSKhachHang(name='Thành', address='Nguyễn Kiệm',
                                       CCCD='202556155', loaiKhach_id=1, maPhieuDatPhong=2)
        ct_dsKH3 = chiTiet_DSKhachHang(name='Huy', address='Bình Tân',
                                       CCCD='777777', loaiKhach_id=2, maPhieuDatPhong=3)
        db.session.add_all([ct_dsKH1, ct_dsKH2, ct_dsKH3])
        db.session.commit()

        hd1 = hoaDon(TongTien='2500000', maPhieuThuePhong=1)
        hd2 = hoaDon(TongTien='2500000', maPhieuThuePhong=2)
        hd3 = hoaDon(TongTien='2500000', maPhieuThuePhong=3)
        db.session.add_all([hd1, hd2, hd3])
        db.session.commit()

        hd_ttp1 = hoaDon_ThongTinPhong(maHoaDon='1', maPhong='1')
        hd_ttp2 = hoaDon_ThongTinPhong(maHoaDon='2', maPhong='2')
        hd_ttp3 = hoaDon_ThongTinPhong(maHoaDon='3', maPhong='3')
        db.session.add_all([hd_ttp1, hd_ttp2, hd_ttp3])
        db.session.commit()


        tk_kh = TaiKhoan_KhachHang(KhachHang_id=1, taiKhoan_id=4)
        tk_kh1 = TaiKhoan_KhachHang(KhachHang_id=2, taiKhoan_id=5)
        tk_kh2 = TaiKhoan_KhachHang(KhachHang_id=3, taiKhoan_id=6)
        tk_kh3 = TaiKhoan_KhachHang(KhachHang_id=4, taiKhoan_id=7)
        db.session.add_all([tk_kh, tk_kh1, tk_kh2, tk_kh3])
        db.session.commit()







