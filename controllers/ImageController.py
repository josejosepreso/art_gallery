import json

from utils.JSONJoin import JSONJoin

N_SHOW_IMAGES = 8;

class ImageController:
	@staticmethod
	def get_imgs(filter: str = None, page: int = 1):
		data = None
		cats = None

		try:
			with open("db/imgs.json", "r") as f:
				data = json.load(f)
		except Exception:
				return []
		try:
			with open("db/categories.json", "r") as f:
				cats = json.load(f)
		except Exception:
				return []

		data = JSONJoin.inner(data, cats, "category_id", "name", "category")

		if page == -1:
			return data

		return data[ N_SHOW_IMAGES * (page - 1) : N_SHOW_IMAGES * page ]

	@staticmethod
	def get_imgs_count(filter: str = None, page: int = 1):
		return ImageController.get_imgs(filter, page), ImageController.get_count(filter)

	@staticmethod
	def get_all():
		return ImageController.get_imgs(None, -1)

	@staticmethod
	def get_count(filter: str = None):
		return len(ImageController.get_all())
