import os
import openai

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY


def analyze_text(text: str) -> str:
    # placeholder for more advanced analysis
    summary = f"Length: {len(text)} chars."
    return summary


def chat_with_assistant(prompt: str) -> str:
    # Basic wrapper: if OPENAI_API_KEY is set, call OpenAI; otherwise return a canned response
    if OPENAI_API_KEY:
        try:
            resp = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role":"user","content":prompt}],
                max_tokens=300
            )
            return resp['choices'][0]['message']['content']
        except Exception as e:
            return f"AI call failed: {e}"
    return f"(POC-assistant) Received prompt of {len(prompt)} chars."
