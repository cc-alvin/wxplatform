from flask_sqlalchemy import SQLAlchemy
import app_config

app = app_config.init()
db = SQLAlchemy(app)