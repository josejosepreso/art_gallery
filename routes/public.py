from flask import Blueprint, render_template

from controllers.ImageController import ImageController

public = Blueprint("public", __name__)

@public.route("/")
def _():
		imgs = ImageController.get_all()
		return render_template("index.html", images = imgs)
