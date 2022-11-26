from Hotel import db, app
from Hotel.models import ThongTinPhong, UserRole, LoaiPhong
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask import redirect
from flask_login import logout_user, current_user

admin = Admin(app=app, name="Trang quản trị", template_mode='bootstrap4')


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class AuthenticatedView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class StatsView(AuthenticatedView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')


class LogoutView(AuthenticatedView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')


admin.add_view(AuthenticatedModelView(ThongTinPhong, db.session, name='Thông tin phòng'))
admin.add_view(AuthenticatedModelView(LoaiPhong, db.session, name='Loại phòng'))
admin.add_view(StatsView(name='Thống Kê - Báo Cáo'))
admin.add_view(LogoutView(name='Đăng xuất'))