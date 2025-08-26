import json

class ImageController:
	@staticmethod
	def get_all():
		data = None
		try:
			with open("db/imgs.json", "r") as f:
				data = json.load(f)
		except Exception:
				pass
		return data
