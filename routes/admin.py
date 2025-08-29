from flask import Blueprint, request, render_template, redirect
from dotenv import load_dotenv
import os

from utils.security import create_jwt_token
from utils.security import validateadmin

from controllers.ImageController import ImageController
from controllers.AdminController import AdminController

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
def signout():
	return render_template("admin/signout.html")

@admin.route("/dashboard", methods = ["POST", "GET"])
@validateadmin
def dashboard():
	p = request.args.get("p")
	page = 1
	if p:
		page = int(p)

	imgs, n_imgs = ImageController.get_imgs_count(None, page)

	return render_template("admin/dashboard.html", images = imgs, n_images = n_imgs)

@admin.route("/add_new_image")
@validateadmin
def add_new_image():
	return render_template("admin/add_new_image.html")

@admin.route("/add_new_image/upload", methods = ["POST"])
@validateadmin
def upload():
	file = request.files["file"]
	cat = request.form.get("cat")
	price = 0 # request.form.get("price")

	if file.filename == "" \
		 or cat == "0" \
		 or price is None:
		return render_template("admin/add_new_image.html", msg = "Invalid input")

	saved = AdminController.save_image(file, cat, price)

	return redirect(f"/dashboard?p=1&token={ request.args.get('token') }") \
		if saved \
		else render_template("admin/add_new_image.html", msg = "Error")

@admin.route("/messages")
@validateadmin
def messages():
	return render_template("admin/messages.html")
