from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import os
from .crypto import generate_key, encrypt_bytes, decrypt_bytes
from .ai_adapter import analyze_text, chat_with_assistant
from sklearn.ensemble import IsolationForest
import joblib
import uuid

app = FastAPI(title="CYBER-IA API")
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Simple in-memory store for logs (for POC)
LOG_STORE = []

@app.post('/generate-key')
def api_generate_key():
    key = generate_key()
    return {"key": key.decode()}

@app.post('/encrypt')
async def api_encrypt(file: UploadFile = File(...)):
    content = await file.read()
    key = generate_key()  # In prod, use KMS and persist
    token = encrypt_bytes(key, content)
    filename = f"{uuid.uuid4().hex}.enc"
    path = os.path.join(DATA_DIR, filename)
    with open(path, 'wb') as f:
        f.write(token)
    return {"file": filename, "key": key.decode()}

@app.post('/decrypt')
async def api_decrypt(key: str, filename: str):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    with open(path, 'rb') as f:
        token = f.read()
    plain = decrypt_bytes(key.encode(), token)
    return JSONResponse(content={"content": plain.decode(errors='ignore')})

@app.post('/upload-logs')
async def upload_logs(payload: dict):
    # Expect JSON with 'logs' field as string
    logs = payload.get('logs')
    if not logs:
        raise HTTPException(status_code=400, detail="No logs provided")
    LOG_STORE.append(logs)
    return {"status": "ok", "stored": len(LOG_STORE)}

@app.get('/analyze')
def analyze():
    # Very simple anomaly detector over log lengths for POC
    if not LOG_STORE:
        return {"anomalies": []}
    import numpy as np
    lens = np.array([len(l) for l in LOG_STORE]).reshape(-1,1)
    clf = IsolationForest(contamination=0.1, random_state=42)
    preds = clf.fit_predict(lens)
    anomalies = [LOG_STORE[i] for i,v in enumerate(preds) if v==-1]
    return {"anomalies": anomalies}

@app.post('/chat')
async def chat(query: dict):
    prompt = query.get('prompt')
    if not prompt:
        raise HTTPException(status_code=400, detail="No prompt")
    resp = chat_with_assistant(prompt)
    return {"response": resp}
