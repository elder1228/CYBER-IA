# KMS adapter (POC)
# In production, implement calls to AWS KMS, Azure Key Vault, or GCP KMS.
# This module provides a minimal interface so the rest of the code can call `encrypt_with_kms`/`decrypt_with_kms`.

import os

KMS_PROVIDER = os.environ.get('KMS_PROVIDER', 'local')


def encrypt_with_kms(plaintext: bytes) -> dict:
    # Return dict with ciphertext and metadata
    if KMS_PROVIDER == 'aws':
        # implement boto3 KMS encrypt
        raise NotImplementedError("AWS KMS integration not implemented in POC")
    # local: return plaintext base64 or raw
    import base64
    return {"ciphertext": base64.b64encode(plaintext).decode(), "provider": "local"}


def decrypt_with_kms(ciphertext_b64: str) -> bytes:
    if KMS_PROVIDER == 'aws':
        raise NotImplementedError("AWS KMS integration not implemented in POC")
    import base64
    return base64.b64decode(ciphertext_b64)
