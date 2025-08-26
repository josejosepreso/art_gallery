from flask import Flask

#
from routes.public import public

app = Flask(__name__)

#
app.register_blueprint(public)
