from flask import Flask
from config import Configuration

from pages.blueprint import pages  




app = Flask(__name__)
app.config.from_object(Configuration)



app.register_blueprint(pages, url_prefix='/homepage')

from flask_pymongo import PyMongo
mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/site")
db = mongodb_client.db

