from flask import render_template, redirect, request, url_for,session
from Hotel import db, app, admin, dao, login
from flask_login import login_user, logout_user, current_user, login_required
from Hotel.models import UserRole
from Hotel.decorator import annonynous_user
import cloudinary.uploader


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/services')
def services():
    return render_template('services.html')


# @app.route('/rooms')
# def rooms():
#     rooms = dao.get_all_rooms()
#     return render_template('rooms.html',     rooms=rooms)


# @app.route('/login_my_user', methods=['get', 'post'])
# @annonynous_user
# def login_my_user():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#
#         user = dao.auth_user(username=username, password=password)
#         if user:
#             login_user(user=user)
#
#             # n = request.args.get('next')
#             # return redirect(n if n else '/')
#
#     return render_template('login.html')

# @app.route('/login_my_user', methods=['GET', 'POST'])
# def login_my_user():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#
#         tk = dao.auth_user(username=username, password=password)
#         if tk:
#             login_user(user=tk)
#             return redirect('/')
#     return render_template('login.html')


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


@app.route('/employee/search')
def employee_search():
    return render_template('/employee/search.html')


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)



if __name__ == '__main__':
    app.run(debug=True)