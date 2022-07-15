import jwt
from config import JWT_TOKEN_SECRET, JWT_ALG


def get_user_token(user):
    token = jwt.encode({"user_id": user.id}, JWT_TOKEN_SECRET, algorithm=JWT_ALG)
    return token


def decode_token(token):
    return jwt.decode(token, JWT_TOKEN_SECRET, algorithms=[JWT_ALG])
