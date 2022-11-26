from flask import render_template, redirect, request
from Hotel import db, app, admin, dao, login
from flask_login import login_user


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
    return  render_template('services.html')


@app.route('/rooms')
def rooms():
    return render_template('rooms.html')


# @app.route('/register')
# def register():
#     return render_template('register.html')


# @app.route('/login')
# def login():
#     return render_template('login.html')

@app.route('/login-admin', methods=['post'])
def login_admin():
    username = request.form['username']
    password = request.form['password']

    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True)