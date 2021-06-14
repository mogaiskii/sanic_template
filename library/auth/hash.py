import hashlib


def get_password_hash(key, password) -> str:
    return hashlib.pbkdf2_hmac('sha512', password.encode(), key.encode(), 100000).hex()
