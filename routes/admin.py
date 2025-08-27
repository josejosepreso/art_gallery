from flask import Blueprint, request, render_template
from dotenv import load_dotenv
import os

from utils.security import create_jwt_token
from utils.security import validateadmin

from controllers.ImageController import ImageController

load_dotenv()

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

from controllers.AdminController import AdminController

admin = Blueprint("admin", __name__)

@admin.route("/auth", methods = ["POST"])
def auth():
	password = request.form.get("password")

	if not password:
		return render_template("login.html", msg = "Error")

	if password != ADMIN_PASSWORD:
		return render_template("login.html", msg = "Incorrect password.")

	token = create_jwt_token()

	return render_template("admin/auth.html", token = token)

@admin.route("/signout", methods = ["POST", "GET"])
@validateadmin
def signout():
	return render_template("admin/signout.html")

@admin.route("/dashboard", methods = ["POST", "GET"])
@validateadmin
def dashboard():
	imgs = ImageController.get_all()
	return render_template("admin/dashboard.html", images = imgs)
