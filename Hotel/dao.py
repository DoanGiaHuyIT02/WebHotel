from Hotel.models import TaiKhoan, LoaiPhong, hinhAnhPhong, ThongTinPhong, khachHang, LoaiKhach,\
    nhanVien, TaiKhoan_KhachHang, phieuDatPhong, phieuThuePhong, ThongTinPhong_phieuDatPhong, chiTiet_DSKhachHang,\
    chiTiet_DSKH_PhieuThue
from Hotel import db
import hashlib


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return TaiKhoan.query.filter(TaiKhoan.username.__eq__(username.strip()),
                             TaiKhoan.password.__eq__(password)).first()


def register(name, username, password, phoneNumber, avatar, address, CCCD):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = TaiKhoan(name=name, username=username.strip(), password=password, phoneNumber=phoneNumber, avatar=avatar)
    db.session.add(u)
    db.session.commit()

    kh = khachHang(name=name, address=address, phone=phoneNumber, CCCD=CCCD)
    db.session.add(kh)
    db.session.commit()

    tk_kh = TaiKhoan_KhachHang(KhachHang_id=kh.MaKhachHang, taiKhoan_id=u.id)
    db.session.add(tk_kh)
    db.session.commit()


def load_CTDSKH(name, phone, CCCD, address, loaiKhach_id, phieuThue_id):
    DSKH = chiTiet_DSKhachHang(name=name, address=address, phone=phone, CCCD=CCCD, loaiKhach_id=loaiKhach_id, phieuThue_id=phieuThue_id)
    db.session.add(DSKH)


def load_khach_hang_dat_phong(name, CCCD, address, loaiKhach_id, khachHang_id, ngayNhanPhong, ngayTraPhong,
                              loaiPhong_id, thanhTien):
        pdp = phieuDatPhong(ngayNhanPhong=ngayNhanPhong, ngayTraPhong=ngayTraPhong, loaiPhong_id=loaiPhong_id,
                            maKhachHang=khachHang_id, thanhTien=thanhTien)
        db.session.add(pdp)
        db.session.commit()
        for l in range(len(name)):
            c = chiTiet_DSKhachHang(name=name[l], address=address[l],
                                    CCCD=CCCD[l], loaiKhach_id=loaiKhach_id[l], maPhieuDatPhong=pdp.maPhieuDatPhong)
            db.session.add(c)
        db.session.commit()


def load_nhan_vien_dat_phong(name, CCCD, address, loaiKhach_id, e_name, e_address, e_phone, e_CCCD, ngayNhanPhong,
                             ngayTraPhong, loaiPhong_id, thanhToan):
    kh = khachHang(name=e_name, address=e_address, phone=e_phone, CCCD=e_CCCD)
    db.session.add(kh)
    db.session.commit()
    pdp = phieuDatPhong(ngayNhanPhong=ngayNhanPhong, ngayTraPhong=ngayTraPhong, loaiPhong_id=loaiPhong_id,
                        maKhachHang=kh.MaKhachHang, thanhTien=thanhToan)
    db.session.add(pdp)
    db.session.commit()
    for e in range(len(name)):
        c = chiTiet_DSKhachHang(name=name[e], address=address[e],
                                CCCD=CCCD[e], loaiKhach_id=loaiKhach_id[e], maPhieuDatPhong=pdp.maPhieuDatPhong)
        db.session.add(c)
    db.session.commit()


def get_phieu_thue_phong(name, CCCD, address, loaiKhach_id, ngayNhanPhong, ngayTraPhong, loaiPhong_id, thanhTien):
    ptp = phieuThuePhong(ngayNhanPhong=ngayNhanPhong, ngayTraPhong=ngayTraPhong, loaiPhong_id=loaiPhong_id,
                         maKhachHang=loaiKhach_id, thanhTien=thanhTien)
    db.session.add(ptp)
    db.session.commit()

    for kh in range(len(name)):
        kh = chiTiet_DSKH_PhieuThue(name=name[kh], address=address[kh], CCCD=CCCD[kh], loaiKhach_id=loaiKhach_id[kh],
                                    maPhieuThuePhong=ptp.maPhieuThuePhong)
        db.session.add(kh)
    db.session.commit()


def load_TTP_PDP(loaiPhong_id, phieuDatPhong_id):
    TTP_PDP = ThongTinPhong_phieuDatPhong(phieuDatPhong_id=phieuDatPhong_id, loaiPhong_id=loaiPhong_id)
    db.session.add(TTP_PDP)
    db.session.commit()


def get_user_by_id(user_id):
    return TaiKhoan.query.get(user_id)


def get_all_loai_phong():
    return LoaiPhong.query.all()


def get_tinh_trang_phong(loaiPhong=None):
    query = ThongTinPhong.query.filter(ThongTinPhong.tinhTrang.__eq__(True))

    if loaiPhong:
        query = query.filter(ThongTinPhong.loaiPhong_id.__eq__(loaiPhong))

    return query.all()


def get_all_images():
    return hinhAnhPhong.query.all()


def get_khach_hang_va_tai_khoan_by_id(taikhoan_id):
    tk_kh = TaiKhoan_KhachHang.query.filter(TaiKhoan_KhachHang.taiKhoan_id.__eq__(taikhoan_id)).all()
    return tk_kh


def get_all_so_phong(loaiPhong_Id):
    # Database => Model => Python App => Query (filter) id = loaiPhong_Id => List all()
    return ThongTinPhong.query.filter(ThongTinPhong.loaiPhong_id.__eq__(loaiPhong_Id)).all()


def load_Khach_Hang(luaChon=None, thongTin=None):
    query = db.session.query(khachHang.MaKhachHang, khachHang.name, phieuDatPhong.ngayNhanPhong,
                             phieuDatPhong.ngayTraPhong, phieuDatPhong.maPhieuDatPhong)
    if luaChon:
        if luaChon == 'ten':
            query = query.join(phieuDatPhong, phieuDatPhong.maKhachHang.__eq__(khachHang.MaKhachHang))\
                .filter(khachHang.name.contains(thongTin))
        if luaChon == 'sdt':
            query = query.join(phieuDatPhong, phieuDatPhong.maKhachHang.__eq__(khachHang.MaKhachHang))\
                .filter(khachHang.phone.contains(thongTin))
        if luaChon == 'cccd':
            query = query.join(phieuDatPhong, phieuDatPhong.maKhachHang.__eq__(khachHang.MaKhachHang))\
                .filter(khachHang.CCCD.contains(thongTin))

    return query.all()


def phieu_dat_phong_by_khach_hang_id(khachhang_id):
    return phieuDatPhong.query.filter(maKhachHang=khachhang_id)


def cac_phong_get_id(phong_id):
    return ThongTinPhong.query.get(phong_id)


def get_phieu_dat_phong_by_id(ma_phieu_dat_phong):
    return db.session.query(phieuDatPhong.maPhieuDatPhong, phieuDatPhong.ngayNhanPhong, phieuDatPhong.ngayTraPhong,
                            phieuDatPhong.loaiPhong_id, chiTiet_DSKhachHang.name, chiTiet_DSKhachHang.address,
                            chiTiet_DSKhachHang.CCCD, chiTiet_DSKhachHang.loaiKhach_id, khachHang.name,
                            LoaiKhach.loaiKhach, LoaiPhong.loaiPhong, phieuDatPhong.thanhTien)\
        .join(chiTiet_DSKhachHang, chiTiet_DSKhachHang.maPhieuDatPhong.__eq__(phieuDatPhong.maPhieuDatPhong))\
        .join(LoaiKhach, LoaiKhach.loaiKhachId.__eq__(chiTiet_DSKhachHang.loaiKhach_id))\
        .join(LoaiPhong, LoaiPhong.loaiPhongId.__eq__(phieuDatPhong.loaiPhong_id))\
        .join(khachHang, khachHang.MaKhachHang.__eq__(phieuDatPhong.maKhachHang))\
        .filter(phieuDatPhong.maPhieuDatPhong.__eq__(ma_phieu_dat_phong)).all()







