from Hotel import db, app, admin, dao, login, controllers

app.add_url_rule('/', 'index', controllers.index)
app.add_url_rule('/contact', 'contact', controllers.contact)
app.add_url_rule('/about', 'about', controllers.about)
app.add_url_rule('/services', 'services', controllers.services)
app.add_url_rule('/rooms', 'rooms', controllers.rooms)
app.add_url_rule('/detail_room', 'detail_room', controllers.detail_room)
app.add_url_rule('/register', 'register', controllers.register, methods=['get', 'post'])
app.add_url_rule('/logout', 'logout_my_user', controllers.logout_my_user)
app.add_url_rule('/employee/login', 'login_page', controllers.login_page, methods=['get', 'post'])
app.add_url_rule('/employee/index', 'employee_index', controllers.employee_index)
app.add_url_rule('/employee/search', 'employee_search', controllers.employee_search, methods=['get', 'post'])
app.add_url_rule('/employee/laphoadon', 'employee_pay', controllers.employee_pay, methods=['GET', 'POST'])
app.add_url_rule('/employee/luuHoaDon', 'luu_hoa_don', controllers.luu_hoa_don, methods=['GET', 'POST'])
app.add_url_rule('/employee/lapphieuthuephong/<int:phieuDatPhong_id>', 'employee_lapphieuthuephong', controllers.employee_lapphieuthuephong)
app.add_url_rule('/employee/phieuThuePhong', 'phieuThuePhong', controllers.phieuThuePhong)
app.add_url_rule('/employee/book', 'employee_book', controllers.employee_book, methods=['GET', 'POST'])
app.add_url_rule('/thanhToanDatPhong', 'pay_customer', controllers.pay_customer, methods=['GET', 'POST'])
app.add_url_rule('/employee/lap_phieu_thue_phong', 'lap_phieu_thue_phong', controllers.lap_phieu_thue_phong, methods=['GET', 'POST'])
app.add_url_rule('/api/soPhong/<int:loaiPhong_id>', 'load_so_phong', controllers.load_so_phong, methods=['GET'])
app.add_url_rule('/api/book/<int:loaiPhong_id>', 'api_so_phong', controllers.api_so_phong, methods=['GET'])


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True)