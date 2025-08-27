import json

N_SHOW_IMAGES = 8;

class ImageController:
	@staticmethod
	def get_imgs(filter: str = None, page: int = 1):
		data = None
		try:
			with open("db/imgs.json", "r") as f:
				data = json.load(f)
		except Exception:
				pass
		if page == -1:
			return data
		return data[ N_SHOW_IMAGES * (page - 1) : N_SHOW_IMAGES * page ]

	@staticmethod
	def get_all():
		return ImageController.get_imgs(None, -1)

	@staticmethod
	def get_count(filter: str = None):
		return len(ImageController.get_all())
