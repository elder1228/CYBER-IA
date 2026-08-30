from backend.app.crypto import generate_key, encrypt_bytes
from pathlib import Path

if __name__ == '__main__':
    key = generate_key()
    path = Path('example.txt')
    if not path.exists():
        path.write_text('exemplo de conteudo secreto')
    data = path.read_bytes()
    token = encrypt_bytes(key, data)
    out = Path('example.txt.enc')
    out.write_bytes(token)
    print('Encrypted to', out)
    print('Key (keep secret):', key.decode())
