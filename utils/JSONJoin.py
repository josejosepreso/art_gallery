class JSONJoin:
	@staticmethod
	def inner(jsonA: list, jsonB: list, field: str, jsonBField: str, alias: str = None):
		if field not in jsonA[0].keys() \
			 or field not in jsonB[0].keys() \
			 or jsonBField in jsonB[0].keys():
			pass

		lookup = { e[field]: e[jsonBField] for e in jsonB }

		if alias is None:
			alias = field

		result = []
		for entry in jsonA:
			entry[alias] = lookup[entry[field]]
			result.append(entry)

		return result
