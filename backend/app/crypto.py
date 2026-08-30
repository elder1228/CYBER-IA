from cryptography.fernet import Fernet

def generate_key() -> bytes:
    return Fernet.generate_key()

def encrypt_bytes(key: bytes, data: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(data)

def decrypt_bytes(key: bytes, token: bytes) -> bytes:
    f = Fernet(key)
    return f.decrypt(token)
