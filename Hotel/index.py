from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from Hotel import db, app


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)