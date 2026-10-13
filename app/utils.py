from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


def hash(password: str):
    return password_hash.hash(password)


def verify_password(password, hashed):
    return password_hash.verify(password, hashed)
