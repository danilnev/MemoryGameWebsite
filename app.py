from flask import Flask, render_template, request, redirect
from models import Base, User, Record
from database import engine, Session

app = Flask(__name__)
session = Session()

Base.metadata.create_all(engine)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/records')
def records():
    return render_template('records.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


if __name__ == '__main__':
    app.run(debug=True)
