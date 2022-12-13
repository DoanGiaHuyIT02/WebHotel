from Hotel import db, app, dao
from Hotel.models import ThongTinPhong, UserRole, LoaiPhong, TaiKhoan, hinhAnhPhong
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask import redirect, request
from flask_login import logout_user, current_user
import hashlib


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class AuthenticatedView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class LogoutView(AuthenticatedView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/')


class accountView(AuthenticatedModelView):
    def create_model(self, form):
        pw = form.password.data
        password = str(hashlib.md5(pw.strip().encode('utf-8')).hexdigest())
        u = TaiKhoan(name=form.name.data, username=form.username.data, password=password, phoneNumber=form.phoneNumber.data,
                     avatar=form.avatar.data,
                     active=form.active.data, user_role=form.user_role.data)
        db.session.add(u)
        db.session.commit()
        return True


class StatsView(AuthenticatedView):
    @expose('/')
    def index(self):
        stats = dao.stats_revenue_by_prod(month=request.args.get('month'), year=request.args.get('year'))
        tongSoPhong = dao.count_loai_phong_trong_phieu_thue_phong(month=request.args.get('month'),
                                                                  year=request.args.get('year'))
        tongDoanhThu = dao.total_doanh_thu(month=request.args.get('month'), year=request.args.get('year'))
        return self.render('admin/stats.html', stats=stats, tongSoPhong=tongSoPhong,
                           tongDoanhThu=tongDoanhThu)

# ,LuaChon_loaiPhong=request.args.get('LuaChon_loaiPhong'),

# class MyAdminView(AdminIndexView):
#    @expose('/')
#    def index(self):
#        stats = dao.count_room_by_cate()
#        return self.render('admin/index.html', stats=stats)


admin = Admin(app=app, name="Trang quản trị", template_mode='bootstrap4')

admin.add_view(AuthenticatedModelView(ThongTinPhong, db.session, name='Thông tin phòng'))
admin.add_view(accountView(TaiKhoan, db.session, name='Tài khoản'))
admin.add_view(AuthenticatedModelView(LoaiPhong, db.session, name='Loại phòng'))
admin.add_view(AuthenticatedModelView(hinhAnhPhong, db.session, name='Hình ảnh phòng'))
admin.add_view(StatsView(name='Thống Kê - Báo Cáo'))
admin.add_view(LogoutView(name='Đăng xuất'))