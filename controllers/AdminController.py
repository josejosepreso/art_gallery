import os
import json

UPLOAD_FOLDER = "static/img"
ALLOWED_EXTENSIONS = {  "jpg", "png" }

class AdminController:
	@staticmethod
	def __allowed_filename(filename):
		return '.' in filename and \
			filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

	@staticmethod
	def save_image(file, cat: str, price: str):
		filename = file.filename
		if not AdminController.__allowed_filename(filename):
			return False

		try:
			with open("db/imgs.json", "r+") as f:
				imgs = json.load(f)
				imgs.insert(0, { "filename": file.filename, "price": price, "category": cat })
				f.seek(0)
				f.write(json.dumps(imgs))
				f.truncate()
		except Exception as e:
				return False

		file.save(os.path.join(UPLOAD_FOLDER, filename))
		return True

	@staticmethod
	def delete_img(filename: str):
		try:
			with open("db/imgs.json", "r+") as f:
				imgs = json.load(f)

				for i, img in enumerate(imgs):
					if img["filename"] == filename:
						imgs.pop(i)
						break

				f.seek(0)
				f.write(json.dumps(imgs))
				f.truncate()
		except Exception as e:
				print(e)
				return False

		try:
			os.remove(os.path.join(UPLOAD_FOLDER, filename))
		except Exception:
			return False

		return True
