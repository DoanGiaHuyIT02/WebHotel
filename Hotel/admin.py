from Hotel import db, app
from Hotel.models import ThongTinPhong
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView

admin = Admin(app=app, name="Trang quản trị", template_mode='bootstrap4')


class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')


admin.add_view(ModelView(ThongTinPhong, db.session, name='Thông tin phòng'))
admin.add_view(StatsView(name='Thống Kê - Báo Cáo'))