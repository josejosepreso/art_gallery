from flask import Flask

#
from routes.public import public
from routes.admin import admin

app = Flask(__name__)

#
app.register_blueprint(public)

app.register_blueprint(admin)
