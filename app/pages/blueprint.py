from flask import Blueprint
from flask import render_template

pages = Blueprint('pages', __name__, template_folder = 'templates')

pages.route('/')
def index():
    return render_template('pages/index.html')