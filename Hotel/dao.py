from Hotel.models import TaiKhoan, LoaiPhong, hinhAnhPhong, ThongTinPhong, khachHang, LoaiKhach,\
    nhanVien, TaiKhoan_KhachHang, phieuDatPhong, phieuThuePhong, ThongTinPhong_phieuDatPhong, chiTiet_DSKhachHang
from Hotel import db
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


def load_CTDSKH(name, phone, CCCD, address, loaiKhach_id, phieuThue_id):
    DSKH = chiTiet_DSKhachHang(name=name, address=address, phone=phone, CCCD=CCCD, loaiKhach_id=loaiKhach_id,\
                               phieuThue_id=phieuThue_id)
    db.session.add(DSKH)


def load_khach_hang_dat_phong(name, phone, CCCD, address, loaiKhach_id, khachHang_id, ngayNhanPhong, ngayTraPhong):
    print(khachHang_id)
    pdp = phieuDatPhong(ngayNhanPhong=ngayNhanPhong, ngayTraPhong=ngayTraPhong, maKhachHang=khachHang_id)
    db.session.add(pdp)
    db.session.commit()
    for l in range(len(name)):
        c = chiTiet_DSKhachHang(name=name[l], address=address[l], phone=phone[l],
                                CCCD=CCCD[l], loaiKhach_id=loaiKhach_id[l], maPhieuDatPhong=pdp.maPhieuDatPhong)
        db.session.add(c)
    db.session.commit()


def load_loai_khach(loaiKhach):
    loaiKhach = LoaiKhach(loaiKhach=loaiKhach)
    db.session.add(loaiKhach)
    db.session.commit()


def load_TTP_PDP(loaiPhong_id, phieuDatPhong_id):
    TTP_PDP = ThongTinPhong_phieuDatPhong(phieuDatPhong_id=phieuDatPhong_id, loaiPhong_id=loaiPhong_id)
    db.session.add(TTP_PDP)
    db.session.commit()


def get_user_by_id(user_id):
    return TaiKhoan.query.get(user_id)


def get_all_loai_phong():
    return LoaiPhong.query.all()


def get_all_so_phong():
    return ThongTinPhong.query.all()


def get_all_images():
    return hinhAnhPhong.query.all()


def get_khach_hang_va_tai_khoan_by_id(taikhoan_id):
    tk_kh = TaiKhoan_KhachHang.query.filter(TaiKhoan_KhachHang.taiKhoan_id.__eq__(taikhoan_id)).all()
    return tk_kh


def load_Khach_Hang(luaChon=None, thongTin=None):
    query = db.session.query(khachHang.MaKhachHang, khachHang.name, phieuDatPhong.ngayNhanPhong, phieuDatPhong.ngayTraPhong, phieuDatPhong.maPhieuDatPhong)

    if luaChon:
        if luaChon == 'ten':
            query = query.join(phieuDatPhong, phieuDatPhong.maKhachHang.__eq__(khachHang.MaKhachHang)).filter(khachHang.name.contains(thongTin))

        if luaChon == 'sdt':
            query = query.join(phieuDatPhong, phieuDatPhong.maKhachHang.__eq__(khachHang.MaKhachHang)).filter(khachHang.phone.contains(thongTin))
        if luaChon == 'cccd':
            query = query.join(phieuDatPhong, phieuDatPhong.maKhachHang.__eq__(khachHang.MaKhachHang)).filter(
                khachHang.CCCD.contains(thongTin))

    return query.all()


def phieu_dat_phong_by_khach_hang_id(khachhang_id):
    return phieuDatPhong.query.filter(maKhachHang=khachhang_id)


def cac_phong_get_id(phong_id):
    return ThongTinPhong.query.get(phong_id)







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


