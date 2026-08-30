const base = '' // set if frontend served from different origin

async function request(path, opts){
  const url = base + path
  const res = await fetch(url, opts)
  return res.json().catch(()=>null)
}

// Key generation
document.getElementById('btn-gen-key').addEventListener('click', async ()=>{
  const r = await request('/generate-key',{method:'POST'})
  document.getElementById('key-output').textContent = JSON.stringify(r,null,2)
})

// Encrypt file
document.getElementById('btn-encrypt').addEventListener('click', async ()=>{
  const f = document.getElementById('file-input').files[0]
  if(!f){ alert('Escolha um ficheiro'); return }
  const fd = new FormData(); fd.append('file', f)
  const r = await fetch('/encrypt', {method:'POST', body: fd})
  const j = await r.json()
  document.getElementById('encrypt-result').textContent = JSON.stringify(j,null,2)
})

// Decrypt file
document.getElementById('btn-decrypt').addEventListener('click', async ()=>{
  const key = document.getElementById('decrypt-key').value
  const filename = document.getElementById('decrypt-filename').value
  if(!key || !filename){ alert('Informe chave e filename'); return }
  const res = await fetch(`/decrypt?key=${encodeURIComponent(key)}&filename=${encodeURIComponent(filename)}`,{method:'POST'})
  const j = await res.json()
  document.getElementById('decrypt-result').textContent = JSON.stringify(j,null,2)
})

// Upload logs
document.getElementById('btn-upload-logs').addEventListener('click', async ()=>{
  const logs = document.getElementById('logs').value
  const r = await fetch('/upload-logs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({logs})})
  const j = await r.json()
  document.getElementById('analysis-result').textContent = JSON.stringify(j,null,2)
})

// Analyze
document.getElementById('btn-analyze').addEventListener('click', async ()=>{
  const r = await fetch('/analyze')
  const j = await r.json()
  document.getElementById('analysis-result').textContent = JSON.stringify(j,null,2)
})

// Chat
document.getElementById('btn-chat').addEventListener('click', async ()=>{
  const prompt = document.getElementById('prompt').value
  const res = await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({prompt})})
  const j = await res.json()
  document.getElementById('chat-response').textContent = JSON.stringify(j,null,2)
})
