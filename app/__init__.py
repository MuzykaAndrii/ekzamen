from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)

from app.api.blueprint import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from app import views, models
