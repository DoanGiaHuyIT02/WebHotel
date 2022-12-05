from flask import render_template, redirect, request, url_for, session, jsonify
from Hotel import db, app, admin, dao, login
from flask_login import login_user, logout_user, current_user, login_required
from Hotel.models import UserRole
from Hotel.decorator import annonynous_user
import cloudinary.uploader


@app.route('/')
def index():
    rooms = dao.get_all_loai_phong()
    images = dao.get_all_images()
    return render_template('index.html', rooms=rooms, images=images)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/rooms')
def rooms():
    rooms = dao.get_all_loai_phong()
    images = dao.get_all_images()
    return render_template('rooms.html', rooms=rooms, images=images)


@app.route('/detail_room')
def detail_room():
    return render_template('detailRoom.html')


@app.route('/register', methods=['get', 'post'])
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
                             username=request.form['username'], phoneNumber=request.form['number'], avatar=avatar)

                return redirect('/')
            except:
                err_msg = 'Đã có lỗi xảy ra! Vui lòng quay lại sau!'
        else:
            err_msg = 'Mật khẩu KHÔNG khớp!'

    return render_template('register.html', err_msg=err_msg)


@app.route('/employee/login', methods=['get', 'post'])
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


@app.route('/employee/index')
@login_required
def employee_index():
    return render_template('/employee/index.html')


@app.route('/logout')
def logout_my_user():
    logout_user()
    return redirect("/employee/login")


@app.route('/employee/search', methods=['get', 'post'])
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


@app.route('/employee/lapphieuthuephong')
def employee_lapphieuthuephong():
    return render_template('/employee/lapphieuthuephong.html')


@app.route('/employee/book')
def employee_book():
    loaiPhong = dao.get_all_loai_phong()
    soPhong = dao.get_all_so_phong()
    return render_template('/employee/book.html', loaiPhong=loaiPhong, soPhong=soPhong)


@app.route('/employee/pay')
def employee_pay():
    return render_template('/employee/payCustomer.html')


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


@app.route('/api_get_phong_dat/')
def api_get_phong_dat():
    data = request.json
    phongDaDat = dao.get_all_loai_phong(data['maDatPhong'])
    return jsonify(
        {'maPhong': phongDaDat.maPhong, 'soPhong': phongDaDat.soPhong}
    )


@app.route('/thanh_toan')
def thanh_toan():
    loaiPhong = dao.get_all_loai_phong()
    return render_template('payCustomer.html', loaiPhong=loaiPhong)


@app.route('/thanhToanDatPhong', methods=['GET', 'POST'])
@login_required
def test():
    if request.method == 'POST':
        name = request.form.getlist('name')
        phone = request.form.getlist('phone')
        CCCD = request.form.getlist('CCCD')
        address = request.form.getlist('address')
        loaiKhach = request.form.getlist('loaiKhach')
        ngayNhanPhong = request.form['ngayNhan']
        ngayTraPhong = request.form['ngayTra']

        tkkh = dao.get_khach_hang_va_tai_khoan_by_id(current_user.id)
        dao.load_khach_hang_dat_phong(name=name, address=address, phone=phone,
                                CCCD=CCCD, loaiKhach_id=loaiKhach, khachHang_id=tkkh[0].KhachHang_id,
                                ngayNhanPhong=ngayNhanPhong, ngayTraPhong=ngayTraPhong)
        return redirect('/thanhToanDatPhong')

    loaiPhong = dao.get_all_loai_phong()
    return render_template('test.html', loaiPhong=loaiPhong)


if __name__ == '__main__':
    app.run(debug=True)