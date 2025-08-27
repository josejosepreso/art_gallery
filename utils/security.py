import jwt
import os
from datetime import datetime, timedelta
from functools import wraps
from dotenv import load_dotenv
from flask import request

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

def create_jwt_token():
	expiration = datetime.utcnow() + timedelta(hours = 1)
	token = jwt.encode({ "exp": expiration }, SECRET_KEY, algorithm="HS256")
	return token

def validateadmin(func):
	@wraps(func)
	def wrapper( *args, **kwargs ):
		# authorization: str = request.headers.get("Authorization")
		authorization: str = request.args.get("token")

		if not authorization:
			return {"error": "Missing Authorization header"}, 401

		authorization = f"bearer { authorization }"

		try:
			schema, token = authorization.split()
			if schema.lower() != "bearer":
				return {"error": "Invalid token schema"}, 401

			payload = jwt.decode( token , SECRET_KEY , algorithms=["HS256"] )
			exp = payload.get("exp")

			if not exp or datetime.utcfromtimestamp(exp) < datetime.utcnow():
				return {"error": "Token expired"}, 401

		except (jwt.ExpiredSignatureError, jwt.DecodeError, ValueError) as e:
			return {"error": f"Token error: {str(e)}"}, 401

		return func( *args, **kwargs )
	return wrapper
