from flask import Blueprint, render_template, request

from controllers.ImageController import ImageController

public = Blueprint("public", __name__)

@public.route("/")
def root():
	p = request.args.get("p")
	page = 1
	if p:
		page = int(p)

	imgs = ImageController.get_imgs(None, page)
	all_imgs = ImageController.get_all()
	n_imgs = ImageController.get_count()

	return render_template("index.html", images = imgs, n_images = n_imgs, all_images = all_imgs)

@public.route("/login")
def login():
	return render_template("login.html")
