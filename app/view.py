from app import app
from flask import render_template
from app import db


@app.route('/')
def index():
    return 'Home'

@app.route('/login')
def login():
    return render_template('index.html')

@app.route('/homepage')
def home():
    return render_template('home.html')

@app.route("/add_one")
def add_one():
    db.site.insert_one({'title': "todo title", 'body': "todo body"})
    return 'OK'