def test_encrypt_decrypt():
    from backend.app.crypto import generate_key, encrypt_bytes, decrypt_bytes
    key = generate_key()
    data = b"mensagem secreta"
    token = encrypt_bytes(key, data)
    assert decrypt_bytes(key, token) == data
