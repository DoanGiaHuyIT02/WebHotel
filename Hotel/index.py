from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from Hotel import db, app


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


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)