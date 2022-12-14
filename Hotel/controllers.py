from flask import render_template, redirect, request, url_for, session, jsonify, flash
from Hotel import db, app, admin, dao, login
from flask_login import login_user, logout_user, current_user, login_required
from Hotel.models import UserRole
from Hotel.decorator import annonynous_user
import cloudinary.uploader


def index():
    rooms = dao.get_all_loai_phong()
    images = dao.get_all_images()
    return render_template('index.html', rooms=rooms, images=images)


def contact():
    return render_template('contact.html')


def about():
    return render_template('about.html')


def services():
    return render_template('services.html')


def rooms():
    rooms = dao.get_all_loai_phong()
    images = dao.get_all_images()
    return render_template('rooms.html', rooms=rooms, images=images)


def detail_room():
    return render_template('detailRoom.html')


def register():
    err_msg = ''
    if request.method == 'POST':
        password = request.form['password']
        confirm = request.form['confirm']
        if password.__eq__(confirm):
            avatar = ''
            if request.files:
                res = cloudinary.uploader.upload(request.files['avatar'])
                avatar = res['secure_url']

            try:
                dao.register(name=request.form['name'],
                             password=password,
                             username=request.form['username'], phoneNumber=request.form['number'], avatar=avatar,
                             address=request.form['address'], CCCD=request.form['CCCD'])
                flash('Đăng ký thành công thành công', 'success')
                return redirect('/employee/login')
            except:
                err_msg = 'Đã có lỗi xảy ra! Vui lòng quay lại sau!'
        else:
            err_msg = 'Mật khẩu KHÔNG khớp!'

    return render_template('register.html', err_msg=err_msg)


@annonynous_user
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)
            session['roles'] = str(current_user.user_role)
            if current_user.user_role == UserRole.ADMIN:
                return redirect('/admin')
            elif current_user.user_role == UserRole.EMPLOYEE:
                return redirect(url_for('employee_index'))
            return redirect('/')

    return render_template('login.html')


@login_required
def employee_index():
    return render_template('/employee/index.html')


def logout_my_user():
    logout_user()
    return redirect("/employee/login")


def employee_search():
    if request.method == 'POST':
        thongTin = request.form['thongTin']
        luaChon = request.form['luaChon']

        khachhang = dao.load_Khach_Hang(luaChon=luaChon, thongTin=thongTin)
        list = []
        for l in khachhang:
            list.append(l[4])
        return render_template('/employee/search.html', khachhang=khachhang, list=list)

    if request.args.get("ma"):
        cacphong = dao.cac_phong_get_id(request.args.get("ma"))
        return render_template('/employee/search.html', cacphong=cacphong)
    return render_template('/employee/search.html')


def employee_pay():
    if request.method == 'POST':
        maPhieuThue = request.form['maPhieuThue']
        is_paid = False
        khach_hang = None
        if maPhieuThue != '':
            kiemTra_hoadon = dao.hoa_don(maPhieuThue)
            if kiemTra_hoadon:
                is_paid = True
                return render_template('/employee/pay.html', is_paid=is_paid)
            else:
                is_paid = False

            phieuThue = dao.get_phieu_thue_by_id(maPhieuThue)
            loaiPhong_phieuThue = dao.get_loai_phong_id(phieuThue.loaiPhong_id)
            if phieuThue is not None:
                khach_hang = dao.get_khach_hang_theo_phieu_thue(phieuThue.maKhachHang)

        return render_template('/employee/pay.html', khach_hang=khach_hang, phieuThue=phieuThue,
                               loaiPhong_phieuThue=loaiPhong_phieuThue, is_paid=is_paid)
    return render_template('/employee/pay.html')


def luu_hoa_don():
    if request.method == 'POST':
        maPhieuThuePhong = request.form['maPhieuThuePhong']
        tongTien = request.form['tongTien']
        price = tongTien[0: len(tongTien) - 2]

        try:
            dao.load_hoa_don(maPhieuThuePhong=maPhieuThuePhong, tongTien=price)
            flash('Lưu hóa đơn thành công', 'success')
            return redirect('/employee/laphoadon')
        except:
            flash('Đặt phòng thất bại', 'error')
    return render_template('/employee/pay.html')


def employee_lapphieuthuephong(phieuDatPhong_id):
    phieuDatPhong = dao.get_phieu_dat_phong_by_id(ma_phieu_dat_phong=phieuDatPhong_id)

    return render_template('/employee/lapphieuthuephong.html', phieuDatPhong=phieuDatPhong)


def phieuThuePhong():
    return render_template('/employee/lapPhieuThuePhong.html')


def employee_book():
    if request.method == 'POST':
        e_name = request.form.getlist('name')
        e_CCCD = request.form.getlist('CCCD')
        e_address = request.form.getlist('address')
        e_name_check_in = request.form['e_name_check_in']
        e_CCCD_check_in = request.form['e_CCCD_check_in']
        e_phone_check_in = request.form['e_phone_check_in']
        e_address_check_in = request.form['e_address_check_in']
        e_ngayNhanPhong = request.form['e_ngayNhanPhong']
        e_ngayTraPhong = request.form['e_ngayTraPhong']
        select_LoaiKhach_id = request.form.getlist('select_LoaiKhach_id')
        e_select_loaiPhong_id = request.form['e_select_loaiPhong_id']
        priceRoom = request.form['priceRoom']

        p = priceRoom[0: len(priceRoom) - 1]

        price = float(p.replace('.', ''))

        try:
            dao.load_nhan_vien_dat_phong(name=e_name, address=e_address,
                                         CCCD=e_CCCD, loaiKhach_id=select_LoaiKhach_id, e_name=e_name_check_in,
                                         e_address=e_address_check_in, e_phone=e_phone_check_in, e_CCCD=e_CCCD_check_in,
                                         ngayNhanPhong=e_ngayNhanPhong, ngayTraPhong=e_ngayTraPhong,
                                         loaiPhong_id=e_select_loaiPhong_id, thanhToan=price)
            flash('Đặt phòng thành công', 'success')
            return redirect('/employee/book')
        except:
            flash('Đặt phòng thất bại', 'error')
    loaiPhong = dao.get_all_loai_phong()
    return render_template('/employee/book.html', loaiPhong=loaiPhong)


def load_so_phong(loaiPhong_id):
    soPhong = dao.get_all_so_phong(loaiPhongID=loaiPhong_id)
    return jsonify(
        {'soPhong': soPhong}
    )


@login_required
def pay_customer():
    if request.method == 'POST':
        name = request.form.getlist('name')
        CCCD = request.form.getlist('CCCD')
        address = request.form.getlist('address')
        loaiKhach = request.form.getlist('loaiKhach')
        ngayNhanPhong = request.form['ngayNhan']
        ngayTraPhong = request.form['ngayTra']
        loaiPhong_id = request.form['loaiPhong_id']
        tongTienKhachHang = request.form['tongTienKhachHang']
        p = tongTienKhachHang[0: len(tongTienKhachHang) - 1]

        price = float(p.replace('.', ''))

        kt = dao.get_tinh_trang_phong(loaiPhong=loaiPhong_id)

        try:
            if len(kt) <= 0:
                flash('Hết phòng, vui lòng chọn loại phòng khác', 'error')
            else:
                tkkh = dao.get_khach_hang_va_tai_khoan_by_id(current_user.id)
                dao.load_khach_hang_dat_phong(name=name, address=address,
                                    CCCD=CCCD, loaiKhach_id=loaiKhach, khachHang_id=tkkh[0].KhachHang_id,
                                    ngayNhanPhong=ngayNhanPhong, ngayTraPhong=ngayTraPhong, loaiPhong_id=loaiPhong_id,
                                    thanhTien=price)
                flash('Đặt phòng thành công', 'success')
            return redirect('/thanhToanDatPhong')
        except:
            flash('Đặt phòng thất bại', 'error')

    loaiPhong = dao.get_all_loai_phong()
    return render_template('payCustomer.html', loaiPhong=loaiPhong)


def lap_phieu_thue_phong():
    if request.method == 'POST':
        name = request.form.getlist('name')
        CCCD = request.form.getlist('CCCD')
        address = request.form.getlist('address')
        loaiKhach_id = request.form.getlist('loaiKhach_id')
        maKhachHang = request.form['maKhachHang']
        ngayNhanPhong = request.form['ngayNhan']
        ngayTraPhong = request.form['ngayTra']
        loaiPhong_id = request.form['loaiPhong_id']
        thanhTien = request.form['thanhTien']

        p = thanhTien[0: len(thanhTien) - 1]

        price = float(p.replace('.', ''))

        try:
            dao.get_phieu_thue_phong(name=name, address=address, CCCD=CCCD, maKhachHang=maKhachHang,
                                     ngayNhanPhong=ngayNhanPhong, ngayTraPhong=ngayTraPhong,
                                     loaiPhong_id=loaiPhong_id, thanhTien=price, loaiKhach_id=loaiKhach_id)
            flash('Lưu phiếu thành công', 'success')
            return redirect('/employee/lap_phieu_thue_phong')
        except:
            flash('Đặt phòng thất bại', 'error')

    return render_template('/employee/lapphieuthuephong.html')


def api_so_phong(loaiPhong_id):
    soPhongList = dao.get_all_so_phong(loaiPhong_Id=loaiPhong_id)

    # soPhongList => ['001', '002', '003']

    soPhongId = []
    for c in soPhongList:
        soPhongId.append(c.soPhong)

    return jsonify(
        {'soPhongArr': soPhongId}
    )

